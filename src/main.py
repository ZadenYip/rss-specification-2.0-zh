from __future__ import annotations

import argparse
import hashlib
import re
from urllib.parse import urljoin, urlparse
from pathlib import Path

import httpx
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as html_to_markdown

DEFAULT_URL = "https://www.rssboard.org/rss-specification"
DEFAULT_OUTPUT = "rss-specification-2.0.md"
DEFAULT_ASSETS_DIR = "assets"

REMOVE_TAGS = {
    "script",
    "style",
    "noscript",
    "iframe",
    "svg",
    "canvas",
    "form",
    "button",
    "input",
    "footer",
}

MAIN_SELECTORS = [
    "div.specification",
    "main",
    "article",
    "#main",
    "#content",
    "#main-content",
    ".main",
    ".content",
    ".post",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a webpage and convert its main content to Markdown."
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"Source URL (default: {DEFAULT_URL})",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Output Markdown file path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP timeout in seconds (default: 30)",
    )
    parser.add_argument(
        "--assets-dir",
        default=DEFAULT_ASSETS_DIR,
        help=f"Directory for downloaded images (default: {DEFAULT_ASSETS_DIR})",
    )
    return parser.parse_args()


def fetch_html(url: str, timeout: float) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }
    with httpx.Client(follow_redirects=True, timeout=timeout, headers=headers) as client:
        response = client.get(url)
        response.raise_for_status()
        response.encoding = response.encoding or "utf-8"
        return response.text


def find_main_content(soup: BeautifulSoup) -> Tag:
    for selector in MAIN_SELECTORS:
        found = soup.select_one(selector)
        if found:
            return found

    body = soup.body
    if body:
        return body

    return soup


def clean_content(node: Tag) -> Tag:
    cleaned = BeautifulSoup(str(node), "html.parser")

    for tag_name in REMOVE_TAGS:
        for tag in cleaned.find_all(tag_name):
            tag.decompose()

    for tag in cleaned.find_all(attrs={"style": True}):
        del tag["style"]

    for comment_like in cleaned.find_all(string=lambda t: isinstance(t, str) and "display:none" in t):
        comment_like.extract()

    return cleaned


def convert_to_markdown(html_fragment: str) -> str:
    md = html_to_markdown(
        html_fragment,
        heading_style="ATX",
        bullets="-",
        escape_asterisks=False,
        escape_underscores=False,
        strip=["span"],
    )
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"\s\[\*\]\([^)]+\)", "", md)
    # Prevent markdown renderers from treating XML element names as HTML tags.
    md = re.sub(r"(?<!`)<(\/?[A-Za-z][A-Za-z0-9:_-]*)>(?!`)", r"`<\1>`", md)
    md = re.sub(r"(!\[[^\]]*\]\([^)]+\))(?=[A-Za-z0-9])", r"\1\n\n", md)
    md = normalize_markdown_tables(md)
    md = normalize_contents_anchors(md)
    return md.strip() + "\n"


def safe_image_name(url: str, used_names: set[str]) -> str:
    parsed = urlparse(url)
    original = Path(parsed.path).name or "image"
    stem = Path(original).stem or "image"
    suffix = Path(original).suffix.lower() or ".img"
    clean_stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem).strip("-") or "image"
    candidate = f"{clean_stem}{suffix}"
    if candidate not in used_names:
        used_names.add(candidate)
        return candidate

    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    candidate = f"{clean_stem}-{digest}{suffix}"
    used_names.add(candidate)
    return candidate


def localize_images(
    markdown_body: str,
    source_url: str,
    assets_dir: Path,
    timeout: float,
) -> str:
    assets_dir.mkdir(parents=True, exist_ok=True)
    used_names: set[str] = set()
    cache: dict[str, str] = {}

    def replace_image(match: re.Match[str]) -> str:
        alt = match.group(1)
        src = match.group(2).strip()
        absolute_src = urljoin(source_url, src)
        if absolute_src in cache:
            return f"![{alt}]({cache[absolute_src]})"

        filename = safe_image_name(absolute_src, used_names)
        local_path = assets_dir / filename
        try:
            with httpx.Client(follow_redirects=True, timeout=timeout) as client:
                resp = client.get(absolute_src)
                resp.raise_for_status()
            local_path.write_bytes(resp.content)
            local_ref = f"{assets_dir.name}/{filename}"
            cache[absolute_src] = local_ref
            return f"![{alt}]({local_ref})"
        except Exception:
            return f"![{alt}]({absolute_src})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_image, markdown_body)


def slugify_markdown_heading(text: str) -> str:
    normalized = text.replace("\\<", "").replace(">", "")
    normalized = normalized.replace("`", "")
    normalized = normalized.lower()
    normalized = re.sub(r"[^a-z0-9\s-]", "", normalized)
    normalized = re.sub(r"\s+", "-", normalized.strip())
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized


def normalize_contents_anchors(md: str) -> str:
    lines = md.splitlines()
    in_contents = False

    for idx, line in enumerate(lines):
        if line.strip() == "#### Contents":
            in_contents = True
            continue

        if not in_contents:
            continue

        if line.startswith("#### "):
            break

        match = re.match(r"^- \[(.+?)\]\(#.+\)$", line)
        if not match:
            continue

        link_text = match.group(1)
        anchor = slugify_markdown_heading(link_text)
        if anchor:
            lines[idx] = f"- [{link_text}](#{anchor})"

    return "\n".join(lines)


def normalize_markdown_tables(md: str) -> str:
    lines = md.splitlines()
    i = 0
    while i + 2 < len(lines):
        row0 = lines[i].strip()
        row1 = lines[i + 1].strip()
        row2 = lines[i + 2].strip()
        if (
            row0.startswith("|")
            and row0.endswith("|")
            and re.fullmatch(r"\|\s*(?:\|\s*)+\|", row0) is not None
            and re.fullmatch(r"\|\s*[:-]+(?:\s*\|\s*[:-]+)+\s*\|", row1) is not None
            and row2.startswith("|")
            and row2.endswith("|")
            and re.fullmatch(r"\|\s*(?:\|\s*)+\|", row2) is None
        ):
            lines[i] = lines[i + 2]
            del lines[i + 2]
        i += 1
    return "\n".join(lines)


def build_markdown_document(url: str, soup: BeautifulSoup, markdown_body: str) -> str:
    page_title = (soup.title.string or "RSS Specification").strip() if soup.title else "RSS Specification"
    header = [
        f"# {page_title}",
        "",
        f"- Source: {url}",
        "",
    ]
    return "\n".join(header) + markdown_body


def main() -> None:
    args = parse_args()

    html = fetch_html(args.url, args.timeout)
    soup = BeautifulSoup(html, "html.parser")
    main_content = find_main_content(soup)
    cleaned = clean_content(main_content)
    markdown_body = convert_to_markdown(str(cleaned))
    markdown_body = localize_images(
        markdown_body=markdown_body,
        source_url=args.url,
        assets_dir=Path(args.assets_dir),
        timeout=args.timeout,
    )
    markdown_doc = build_markdown_document(args.url, soup, markdown_body)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_doc, encoding="utf-8")

    print(f"Saved Markdown to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
