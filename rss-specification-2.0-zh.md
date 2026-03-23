# RSS 2.0 规范

### RSS 2.0 规范

编者注：这是 RSS 2.0 规范的当前版本，由 RSS Advisory Board 于 2009 年 3 月 30 日发布，版本号为 2.0.11。RSS 规范的当前版本将始终可通过[此链接](https://www.rssboard.org/rss-specification)访问，所有变更均已被[记录](https://www.rssboard.org/rss-change-notes)，其他历史修订版本也已被[归档](https://www.rssboard.org/rss-history)。


<!-- #### Contents -->
#### 目录

<!-- - [What is RSS?](#what-is-rss)
- [Sample files](#sample-files)
- [About this document](#about-this-document)
- [Required channel elements](#required-channel-elements)
- [Optional channel elements](#optional-channel-elements)
- [Elements of `<item>`](#elements-of-item)
- [Comments](#comments)
- [Extending RSS](#extending-rss)
- [Roadmap](#roadmap)
- [License and authorship](#license-and-authorship) -->

- [什么是 RSS？](#what-is-rss)
- [示例文件](#sample-files)
- [关于本文档](#about-this-document)
- [必需的 channel 子元素](#required-channel-elements)
- [可选的 channel 子元素](#optional-channel-elements)
- [`<item>` 的元素](#elements-of-item)
- [补充说明](#comments)
- [扩展 RSS](#extending-rss)
- [未来规划图](#roadmap)
- [许可与作者信息](#license-and-authorship)

<span id="what-is-rss"></span>

<!-- #### What is RSS -->
#### 什么是 RSS？

<!-- RSS is a Web content syndication format. -->
RSS 是一种 Web 内容聚合（syndication）格式。

<!-- Its name is an acronym for ***R**eally **S**imple **S**yndication.* -->
RSS 的名字是 ***R**eally **S**imple **S**yndication* 的首字母缩写，可译为「简易信息聚合」。

<!-- RSS is a dialect of XML. All RSS files must conform to the XML 1.0 [specification](http://www.w3.org/TR/REC-xml), as published on the World Wide Web Consortium (W3C) website. -->
RSS 是 XML 的一种方言。所有 RSS 文件都必须符合万维网联盟（W3C）网站发布的 XML 1.0 [规范](http://www.w3.org/TR/REC-xml)。

<!-- A summary of [RSS version history](https://www.rssboard.org/rss-history). -->
关于 RSS 版本历史的摘要见[这里](https://www.rssboard.org/rss-history)。

<!-- At the top level, a RSS document is a `<rss>` element, with a mandatory attribute called version, that specifies the version of RSS that the document conforms to. If it conforms to this specification, the version attribute must be 2.0. -->
在顶级层级， RSS 文档是一个 `<rss>` 元素，并带有名为 version 的必需属性，用于指明该文档所遵循的 RSS 版本。如果该文档符合本规范，则 version 属性必须是 2.0。

<!-- Subordinate to the `<rss>` element is a single `<channel>` element, which contains information about the channel (metadata) and its contents. -->
`<rss>` 元素下包含着一个唯一的 `<channel>` 元素，其中承载了关于频道的信息（元数据）及其内容。

<span id="sample-files"></span>

<!-- #### sample-files -->
#### 示例文件 

<!-- Here are sample files for: RSS [0.91](https://www.rssboard.org/files/sample-rss-091.xml), [0.92](https://www.rssboard.org/files/sample-rss-092.xml) and [2.0](https://www.rssboard.org/files/sample-rss-2.xml). -->
这里是 RSS [0.91](https://www.rssboard.org/files/sample-rss-091.xml)、[0.92](https://www.rssboard.org/files/sample-rss-092.xml) 和 [2.0](https://www.rssboard.org/files/sample-rss-2.xml) 的示例文件。

<!-- Note that the sample files may point to documents and services that no longer exist. The 0.91 sample was created when the 0.91 docs were written. Maintaining a trail of samples seems like a good idea. -->
请注意，这里的示例文件所指向的文档与服务可能已经不存在。0.91 的示例是在 0.91 文档编写时创建的。保留这样一条示例演进轨迹，似乎是个不错的做法。

<span id="about-this-document"></span>

<!-- #### About this document -->
#### 关于本文档

<!-- ![A bouquet of flowers, the symbol of RSS 2.0](assets/flowers.gif) -->
![一束鲜花，RSS 2.0 的象征](assets/flowers.gif)

<!-- This document represents the current status of RSS, incorporating all changes and additions starting with the basic spec for [RSS 0.91](https://www.rssboard.org/rss-0-9-1) (June 2000) and follows [RSS 0.92](https://www.rssboard.org/rss-0-9-2) (December 2000), [RSS 2.0](https://www.rssboard.org/rss-2-0) (August 2002), and [RSS 2.0.1](https://www.rssboard.org/rss-2-0-1) (July 2003). Change notes are [here](https://www.rssboard.org/rss-change-notes). -->
本文档代表 RSS 的当前状态，纳入了从 [RSS 0.91](https://www.rssboard.org/rss-0-9-1)（2000 年 6 月）基础规范开始的所有更改与补充，并沿袭了 [RSS 0.92](https://www.rssboard.org/rss-0-9-2)（2000 年 12 月）、[RSS 2.0](https://www.rssboard.org/rss-2-0)（2002 年 8 月）以及 [RSS 2.0.1](https://www.rssboard.org/rss-2-0-1)（2003 年 7 月）的内容。变更说明见[这里](https://www.rssboard.org/rss-change-notes)。

<!-- First we document the required and optional sub-elements of `<channel>`; and then document the sub-elements of `<item>`. The final sections answer frequently asked questions, and provide a roadmap for future evolution, and guidelines for extending RSS. -->
本文首先会说明 `<channel>` 下的必需与可选子元素；接着说明 `<item>` 下的各个子元素。最后几个章节将回答常见问题，并给出未来演进路线图以及扩展 RSS 的指导原则。

<!-- The [RSS Profile](https://www.rssboard.org/rss-profile) contains a set of recommendations for how to create RSS documents that work best in the wide and diverse audience of client software that supports the format. -->
[RSS Profile](https://www.rssboard.org/rss-profile) 包含了一些建议，指导了如何创建一个 RSS 文档，让其能在广泛而多样的 RSS 客户端软件中有最佳的适配效果。

<!-- RSS documents can be tested for validity in the [RSS Validator](https://www.rssboard.org/rss-validator/). -->
RSS 文档可以使用 [RSS Validator](https://www.rssboard.org/rss-validator/) 进行有效性测试。

<span id="required-channel-elements"></span>

<!-- #### Required channel elements -->
#### 必需的 channel 子元素

<!-- Here's a list of the required channel elements, each with a brief description, an example, and where available, a pointer to a more complete description. -->
下边列出了一些必需的 channel 子元素；每个元素都附有简要的说明、示例以及视情况下会给出指向更完整说明的链接。

<!-- | Element | Description | Example |
| --- | --- | --- |
| title | The name of the channel. It's how people refer to your service. If you have an HTML website that contains the same information as your RSS file, the title of your channel should be the same as the title of your website. | GoUpstate.com News Headlines |
| link | The URL to the HTML website corresponding to the channel. | http://www.goupstate.com/ |
| description | Phrase or sentence describing the channel. | The latest news from GoUpstate.com, a Spartanburg Herald-Journal Web site. | -->
| 元素 | 中文说明 | 示例 |
| --- | --- | --- |
| title | 频道的名称，也就是人们用来称呼你的服务的名字。如果你有一个与 RSS 文件包含相同信息的 HTML 网站，那么该频道的 title 应与网站标题保持一致。 | GoUpstate.com News Headlines |
| link | 与该频道对应的 HTML 网站 URL。 | http://www.goupstate.com/ |
| description | 用于描述该频道的短语或句子。 | The latest news from GoUpstate.com, a Spartanburg Herald-Journal Web site. |

<span id="optional-channel-elements"></span>
<!-- #### Optional channel elements -->

#### 可选的 channel 子元素

<!-- Here's a list of optional channel elements. -->
以下列出了可选的 channel 子元素。

<!-- | Element | Description | Example |
| --- | --- | --- |
| language | The language the channel is written in. This allows aggregators to group all Italian language sites, for example, on a single page. A list of allowable values for this element, as provided by Netscape, is [here](https://www.rssboard.org/rss-language-codes). You may also use [values defined](http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes) by the W3C. | en-us |
| copyright | Copyright notice for content in the channel. | Copyright 2002, Spartanburg Herald-Journal |
| managingEditor | Email address for person responsible for editorial content. | geo@herald.com (George Matesky) |
| webMaster | Email address for person responsible for technical issues relating to channel. | betty@herald.com (Betty Guernsey) |
| pubDate | The publication date for the content in the channel. For example, the *New York Times* publishes on a daily basis, the publication date flips once every 24 hours. That's when the pubDate of the channel changes. All date-times in RSS conform to the Date and Time Specification of [RFC 822](http://asg.web.cmu.edu/rfc/rfc822.html), with the exception that the year may be expressed with two characters or four characters (four preferred). | Sat, 07 Sep 2002 00:00:01 GMT |
| lastBuildDate | The last time the content of the channel changed. | Sat, 07 Sep 2002 09:42:31 GMT |
| category | Specify one or more categories that the channel belongs to. Follows the same rules as the `<item>`-level [category](#ltcategorygtSubelementOfLtitemgt) element. More [info](#syndic8). | `<category>`Newspapers`</category>` |
| generator | A string indicating the program used to generate the channel. | MightyInHouse Content System v2.3 |
| docs | A URL that points to the [documentation](https://www.rssboard.org/rss-specification) for the format used in the RSS file. It's probably a pointer to this page. It's for people who might stumble across an RSS file on a Web server 25 years from now and wonder what it is. | https://www.rssboard.org/rss-specification |
| cloud | Allows processes to register with a cloud to be notified of updates to the channel, implementing a lightweight publish-subscribe protocol for RSS feeds. More info [here](#ltcloudgtSubelementOfLtchannelgt). | <cloud domain="rpc.sys.com" port="80" path="/RPC2" registerProcedure="pingMe" protocol="soap"/> |
| ttl | ttl stands for time to live. It's a number of minutes that indicates how long a channel can be cached before refreshing from the source. More info [here](#ltttlgtSubelementOfLtchannelgt). | `<ttl>`60`</ttl>` |
| image | Specifies a GIF, JPEG or PNG image that can be displayed with the channel. More info [here](#ltimagegtSubelementOfLtchannelgt). |  |
| rating | The [PICS](http://www.w3.org/PICS/) rating for the channel. |  |
| textInput | Specifies a text input box that can be displayed with the channel. More info [here](#lttextinputgtSubelementOfLtchannelgt). |  |
| skipHours | A hint for aggregators telling them which hours they can skip. This element contains up to 24 `<hour>` sub-elements whose value is a number between 0 and 23, representing a time in GMT, when aggregators, if they support the feature, may not read the channel on hours listed in the `<skipHours>` element. The hour beginning at midnight is hour zero. |  |
| skipDays | A hint for aggregators telling them which days they can skip. This element contains up to seven `<day>` sub-elements whose value is Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. Aggregators may not read the channel during days listed in the `<skipDays>` element. |  | -->
| 元素 | 中文说明 | 示例 |
| --- | --- | --- |
| language |频道所使用的语言。比如，这使聚合器（aggregators）可以把所有意大利语站点归到同一个页面中。Netscape 提供的可用取值列表见[这里](https://www.rssboard.org/rss-language-codes)，你也可以使用 W3C [定义的值](http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes)。 | en-us |
| copyright |频道内容的版权声明。 | Copyright 2002, Spartanburg Herald-Journal |
| managingEditor | 负责编辑内容的人员的电子邮箱地址。 | geo@herald.com (George Matesky) |
| webMaster | 负责频道技术问题的人员的电子邮箱地址。 | betty@herald.com (Betty Guernsey) |
| pubDate |频道内容的发布日期。例如，**New York Times** 按日发布内容，其 pubDate 大约每 24 小时更新一次。也就是在那个时间点，channel 的 pubDate 会变化。RSS 中所有日期时间都遵循 [RFC 822](http://asg.web.cmu.edu/rfc/rfc822.html) 的日期时间规范，唯一的例外是年份既可以写成两位，也可以写成四位，推荐四位。 | Sat, 07 Sep 2002 00:00:01 GMT |
| lastBuildDate |频道内容最后一次发生变更的时间。 | Sat, 07 Sep 2002 09:42:31 GMT |
| category | 指定该频道所属的一个或多个分类。规则与 `<item>` 层级的 [category](#ltcategorygtSubelementOfLtitemgt) 元素相同。更多信息见[这里](#syndic8)。 | `<category>`Newspapers`</category>` |
| generator | 指明生成该频道所用程序的字符串。 | MightyInHouse Content System v2.3 |
| docs | 指向该 RSS 文件所使用格式对应[文档](https://www.rssboard.org/rss-specification)的 URL。它大概率就是指向本页，供那些在 25 年后偶然在 Web 服务器上发现 RSS 文件的人了解其含义。 | https://www.rssboard.org/rss-specification |
| cloud | 允许进程向 cloud 注册，以便在频道更新时收到通知，从而为 RSS feed 实现一种轻量级的发布—订阅协议。更多信息见[这里](#ltcloudgtSubelementOfLtchannelgt)。 | <cloud domain="rpc.sys.com" port="80" path="/RPC2" registerProcedure="pingMe" protocol="soap"/> |
| ttl | ttl 即 time to live，表示频道在从源站重新刷新之前可以被缓存的分钟数。更多信息见[这里](#ltttlgtSubelementOfLtchannelgt)。 | `<ttl>`60`</ttl>` |
| image | 指定一个可与频道一同显示的 GIF、JPEG 或 PNG 图片。更多信息见[这里](#ltimagegtSubelementOfLtchannelgt)。 |  |
| rating |频道的 [PICS](http://www.w3.org/PICS/) 分级。 |  |
| textInput | 指定一个可与频道一起显示的文本输入框。更多信息见[这里](#lttextinputgtSubelementOfLtchannelgt)。 |  |
| skipHours | 给聚合器的提示，告知哪些小时可以跳过不抓取。该元素最多可包含 24 个 `<hour>` 子元素，其值为 0 到 23 的数字，表示 GMT 时间中的某个小时。若聚合器支持该特性，则可在 `<skipHours>` 列出的小时内不读取该频道。午夜开始的那个小时记为 0。 |  |
| skipDays | 给聚合器的提示，告知哪些日期可以跳过不抓取。该元素最多可包含七个 `<day>` 子元素，其值可以是 Monday、Tuesday、Wednesday、Thursday、Friday、Saturday 或 Sunday。聚合器可在 `<skipDays>` 列出的日期内不读取该频道。 |  |

---
<!-- ##### `<image>` sub-element of `<channel>` -->
##### `<channel>` 的 `<image>` 子元素

<!-- `<image>` is an optional sub-element of `<channel>`, which contains three required and three optional sub-elements. -->
`<image>` 是 `<channel>` 的一个可选子元素，其中包含三个必需子元素和三个可选子元素。

<!-- `<url>` is the URL of a GIF, JPEG or PNG image that represents the channel. -->
`<url>` 是代表该频道的 GIF、JPEG 或 PNG 图片的 URL。

<!-- `<title>` describes the image, it's used in the ALT attribute of the HTML `<img>` tag when the channel is rendered in HTML. -->
`<title>` 用于描述该图片；当频道被渲染为 HTML 时，它会被用于 HTML `<img>` 标签的 ALT 属性。

<!-- `<link>` is the URL of the site, when the channel is rendered, the image is a link to the site. (Note, in practice the image `<title>` and `<link>` should have the same value as the channel's `<title>` and `<link>`. -->
`<link>` 是站点的 URL；当频道被渲染时，这张图片会作为指向该站点的链接。（注意，在实践中，图片的 `<title>` 和 `<link>` 应当与频道自身的 `<title>` 和 `<link>` 保持一致。）

<!-- Optional elements include `<width>` and `<height>`, numbers, indicating the width and height of the image in pixels. `<description>` contains text that is included in the TITLE attribute of the link formed around the image in the HTML rendering. -->
可选元素还包括 `<width>` 和 `<height>`，它们是数值，表示图片以像素为单位的宽度和高度。`<description>` 则包含一段文本，在 HTML 渲染时会被放入包裹该图片的链接的 TITLE 属性中。

<!-- Maximum value for width is 144, default value is 88. -->
`<width>` 的最大值为 144，默认值为 88。

<!-- Maximum value for height is 400, default value is 31. -->
`<height>` 的最大值为 400，默认值为 31。

---
<!-- ##### `<cloud>` sub-element of `<channel>` -->
##### `<channel>` 的 `<cloud>` 子元素

<!-- `<cloud>` is an optional sub-element of `<channel>`. -->
`<cloud>` 是 `<channel>` 的一个可选子元素。

<!-- It specifies a web service that supports the rssCloud interface which can be implemented in HTTP-POST, XML-RPC or SOAP 1.1. -->
它指定了一个支持 rssCloud 接口的 Web 服务，该接口可以通过 HTTP-POST、XML-RPC 或 SOAP 1.1 来实现。

<!-- Its purpose is to allow processes to register with a cloud to be notified of updates to the channel, implementing a lightweight publish-subscribe protocol for RSS feeds. -->
其目的是允许进程向 cloud 注册，以便在频道更新时收到通知，从而为 RSS feed 实现一种轻量级的发布—订阅协议。

<!-- <cloud domain="rpc.sys.com" port="80" path="/RPC2" registerProcedure="myCloud.rssPleaseNotify" protocol="xml-rpc" /> -->
`<cloud domain="rpc.sys.com" port="80" path="/RPC2" registerProcedure="myCloud.rssPleaseNotify" protocol="xml-rpc" />`

<!-- In this example, to request notification on the channel it appears in, you would send an XML-RPC message to rpc.sys.com on port 80, with a path of /RPC2. The procedure to call is myCloud.rssPleaseNotify. -->
在这个示例中，如果你想请求接收该频道的更新通知，就需要向 `rpc.sys.com` 的 80 端口发送一条 XML-RPC 消息，路径为 `/RPC2`，调用的过程名是 `myCloud.rssPleaseNotify`。

<!-- A full explanation of this element and the rssCloud interface is [here](https://www.rssboard.org/rsscloud-interface). -->
关于该元素及 rssCloud 接口的完整说明见[这里](https://www.rssboard.org/rsscloud-interface)。

---

<!-- ##### `<ttl>` sub-element of `<channel>` -->
##### `<channel>` 的 `<ttl>` 子元素

<!-- `<ttl>` is an optional sub-element of `<channel>`. -->
`<ttl>` 是 `<channel>` 的一个可选子元素。

<!-- ttl stands for time to live. It's a number of minutes that indicates how long a channel can be cached before refreshing from the source. This makes it possible for RSS sources to be managed by a file-sharing network such as Gnutella. -->
ttl 是 time to live 的缩写，表示频道在重新从源站刷新之前可以被缓存多少分钟。这使得 RSS 源可以通过类似 Gnutella 的文件共享网络来管理。

<!-- Example: -->
示例：
`<ttl>60</ttl>`

---

<!-- ##### `<textInput>` sub-element of `<channel>` -->
##### `<channel>` 的 `<textInput>` 子元素

<!-- A channel may optionally contain a `<textInput>` sub-element, which contains four required sub-elements. -->
一个频道可以选择性地包含 `<textInput>` 子元素，其中包含四个必需子元素。

<!-- `<title>` -- The label of the Submit button in the text input area. -->
`<title>` —— 文本输入区域中提交按钮的标签。

<!-- `<description>` -- Explains the text input area. -->
`<description>` —— 对文本输入区域的说明。

<!-- `<name>` -- The name of the text object in the text input area. -->
`<name>` —— 文本输入区域中该文本对象的名称。

<!-- `<link>` -- The URL of the CGI script that processes text input requests. -->
`<link>` —— 处理文本输入请求的 CGI 脚本 URL。

<!-- The purpose of the `<textInput>` element is something of a mystery. You can use it to specify a search engine box. Or to allow a reader to provide feedback. Most aggregators ignore it. -->
`<textInput>` 元素的用途多少有些神秘。你可以用它来指定一个搜索框，或者允许读者提交反馈。不过，大多数聚合器都会忽略它。


<span id="elements-of-item"></span>

---

<!-- #### Elements of `<item>` -->
#### `<item>` 的元素

<!-- A channel may contain any number of `<item>`s. An item may represent a "story" -- much like a story in a newspaper or magazine; if so its description is a synopsis of the story, and the link points to the full story. An item may also be complete in itself, if so, the description contains the text (entity-encoded HTML is allowed; see [examples](https://www.rssboard.org/rss-encoding-examples)), and the link and title may be omitted. All elements of an item are optional, however at least one of title or description must be present. -->
一个频道可以包含任意数量的 `<item>`。一个 item 可以表示一则「报道」，类似报纸或杂志中的一篇文章；在这种情况下，它的 description 是该报道的摘要，而 link 指向完整内容。一个 item 也可以本身就是完整内容；在这种情况下，description 中直接包含正文（允许使用实体编码（entity-encoded）后的 HTML，见[示例](https://www.rssboard.org/rss-encoding-examples)），而 link 和 title 可以省略。item 的所有元素都属于可选项，但 title 与 description 至少必须出现一个。

<!-- | Element | Description | Example |
| --- | --- | --- |
| title | The title of the item. | Venice Film Festival Tries to Quit Sinking |
| link | The URL of the item. | http://nytimes.com/2004/12/07FEST.html |
| description | The item synopsis. | `<description>`Some of the most heated chatter at the Venice Film Festival this week was about the way that the arrival of the stars at the Palazzo del Cinema was being staged.`</description>` |
| author | Email address of the author of the item. [More](#ltauthorgtSubelementOfLtitemgt). |  |
| category | Includes the item in one or more categories. [More](#ltcategorygtSubelementOfLtitemgt). |  |
| comments | URL of a page for comments relating to the item. [More](#ltcommentsgtSubelementOfLtitemgt). |  |
| enclosure | Describes a media object that is attached to the item. [More](#ltenclosuregtSubelementOfLtitemgt). |  |
| guid | A string that uniquely identifies the item. [More](#ltguidgtSubelementOfLtitemgt). |  |
| pubDate | Indicates when the item was published. [More](#ltpubdategtSubelementOfLtitemgt). |  |
| source | The RSS channel that the item came from. [More](#ltsourcegtSubelementOfLtitemgt). |  | -->
| 元素 | 中文说明 | 示例 |
| --- | --- | --- |
| title | item 的标题。 | Venice Film Festival Tries to Quit Sinking |
| link | item 的 URL。 | http://nytimes.com/2004/12/07FEST.html |
| description | item 的摘要。 | `<description>`Some of the most heated chatter at the Venice Film Festival this week was about the way that the arrival of the stars at the Palazzo del Cinema was being staged.`</description>` |
| author | item 作者的电子邮箱地址。更多信息见[这里](#ltauthorgtSubelementOfLtitemgt)。 |  |
| category | 将 item 纳入一个或多个分类。更多信息见[这里](#ltcategorygtSubelementOfLtitemgt)。 |  |
| comments | 指向与该 item 相关评论页面的 URL。更多信息见[这里](#ltcommentsgtSubelementOfLtitemgt)。 |  |
| enclosure | 描述附加到该 item 的媒体对象。更多信息见[这里](#ltenclosuregtSubelementOfLtitemgt)。 |  |
| guid | 唯一标识该 item 的字符串。更多信息见[这里](#ltguidgtSubelementOfLtitemgt)。 |  |
| pubDate | 表明该 item 的发布时间。更多信息见[这里](#ltpubdategtSubelementOfLtitemgt)。 |  |
| source | 该 item 所来源的 RSS 频道。更多信息见[这里](#ltsourcegtSubelementOfLtitemgt)。 |  |


<!-- ##### `<source>` sub-element of `<item>` -->
##### `<item>` 的 `<source>` 子元素

<!-- `<source>` is an optional sub-element of `<item>`. -->
`<source>` 是 `<item>` 的一个可选子元素。

<!-- Its value is the name of the RSS channel that the item came from, derived from its `<title>`. It has one required attribute, url, which links to the XMLization of the source. -->
它的值是该 item 所来源 RSS 频道的名称，通常取自该频道的 `<title>`。它有一个必需属性 `url`，用于链接到该来源的 XML 形式。

<!-- <source url="http://www.tomalak.org/links2.xml">Tomalak's Realm`</source>` -->
`<source url="http://www.tomalak.org/links2.xml">Tomalak's Realm</source>`

<!-- The purpose of this element is to propagate credit for links, to publicize the sources of news items. It can be used in the Post command of an aggregator. It should be generated automatically when forwarding an item from an aggregator to a weblog authoring tool. -->
该元素的目的在于为链接传播署名，并公开新闻条目的来源。它可以用于聚合器的 Post 命令；当一个 item 从聚合器转发到博客写作工具时，理应由系统自动生成这个元素。

---

<!-- ##### `<enclosure>` sub-element of `<item>` -->
##### `<item>` 的 `<enclosure>` 子元素

<!-- `<enclosure>` is an optional sub-element of `<item>`. -->
`<enclosure>` 是 `<item>` 的一个可选子元素。

<!-- It has three required attributes. url says where the enclosure is located, length says how big it is in bytes, and type says what its type is, a standard MIME type. -->
它有三个必需属性。`url` 表示 enclosure 所在的位置，`length` 表示它的字节大小，`type` 表示它的类型，即一个标准 MIME type。

<!-- The url must be an http url. -->
该 `url` 必须是一个 http URL。

<!-- <enclosure url="http://www.scripting.com/mp3s/weatherReportSuite.mp3" length="12216320" type="audio/mpeg" /> -->
`<enclosure url="http://www.scripting.com/mp3s/weatherReportSuite.mp3" length="12216320" type="audio/mpeg" />`

<!-- A use-case narrative for this element is [here](https://www.rssboard.org/rss-enclosures-use-case). -->
关于该元素的使用场景说明见[这里](https://www.rssboard.org/rss-enclosures-use-case)。

<!-- ##### `<category>` sub-element of `<item>` -->

---

##### `<item>` 的 `<category>` 子元素

<!-- `<category>` is an optional sub-element of `<item>`. -->
`<category>` 是 `<item>` 的一个可选子元素。

<!-- It has one optional attribute, domain, a string that identifies a categorization taxonomy. -->
它有一个可选属性 `domain`，是一个用于标识分类标准（categorization taxonomy）的字符串。

<!-- The value of the element is a forward-slash-separated string that identifies a hierarchic location in the indicated taxonomy. Processors may establish conventions for the interpretation of categories. Two examples are provided below: -->
该元素的值是一个以正斜杠分隔的字符串，用于表示在指定分类标准中的层级位置。处理器可以自行建立对这些分类的解释约定。下面给出两个示例：

`<category>Grateful Dead</category>`

<!-- <category domain="http://www.fool.com/cusips">MSFT`</category>` -->
`<category domain="http://www.fool.com/cusips">MSFT</category>`

<!-- You may include as many category elements as you need to, for different domains, and to have an item cross-referenced in different parts of the same domain. -->
你可以根据需要包含任意数量的 category 元素，以支持不同的 domain，并使同一个 item 在同一 domain 的不同部分中被交叉引用。

---

<!-- ##### `<pubDate>` sub-element of `<item>` -->
##### `<item>` 的 `<pubDate>` 子元素

<!-- `<pubDate>` is an optional sub-element of `<item>`. -->
`<pubDate>` 是 `<item>` 的一个可选子元素。

<!-- Its value is a [date](http://asg.web.cmu.edu/rfc/rfc822.html), indicating when the item was published. If it's a date in the future, aggregators may choose to not display the item until that date. -->
它的值是一个[日期](http://asg.web.cmu.edu/rfc/rfc822.html)，用于表明该 item 的发布时间。如果这个日期在未来，聚合器可以选择在该日期到来之前不显示该 item。

`<pubDate>Sun, 19 May 2002 15:21:36 GMT</pubDate>`

---

<!-- ##### `<guid>` sub-element of `<item>` -->
##### `<item>` 的 `<guid>` 子元素

<!-- `<guid>` is an optional sub-element of `<item>`. -->
`<guid>` 是 `<item>` 的一个可选子元素。

<!-- guid stands for globally unique identifier. It's a string that uniquely identifies the item. When present, an aggregator may choose to use this string to determine if an item is new. -->
guid 是 globally unique identifier 的缩写，即「全局唯一标识符」。它是一个能够唯一标识该 item 的字符串。存在该元素时，聚合器可以选择用它来判断某个 item 是否为新内容。

`<guid>http://some.server.com/weblogItem3207</guid>`

<!-- There are no rules for the syntax of a guid. Aggregators must view them as a string. It's up to the source of the feed to establish the uniqueness of the string. -->
guid 的语法没有强制规则。聚合器必须把它当作普通字符串来看待。至于该字符串是否唯一，则由订阅源的提供方（source of the feed）负责保证。

<!-- If the guid element has an attribute named isPermaLink with a value of true, the reader may assume that it is a permalink to the item, that is, a url that can be opened in a Web browser, that points to the full item described by the `<item>` element. An example: -->
如果 guid 元素带有名为 `isPermaLink` 的属性，且其值为 `true`，那么读取方可以认为它是该 item 的永久链接，也就是一个可在 Web 浏览器中打开并指向 `<item>` 所描述完整内容的 URL。示例如下：

`<guid isPermaLink="true">http://inessential.com/2002/09/01.php#a2</guid>`

<!-- isPermaLink is optional, its default value is true. If its value is false, the guid may not be assumed to be a url, or a url to anything in particular. -->
`isPermaLink` 是可选属性，其默认值为 `true`。如果其值为 `false`，则不能假定 guid 是一个 URL，也不能假定它特指某个具体资源。

---

<!-- ##### `<comments>` sub-element of `<item>` -->
##### `<item>` 的 `<comments>` 子元素

<!-- `<comments>` is an optional sub-element of `<item>`. -->
`<comments>` 是 `<item>` 的一个可选子元素。

<!-- If present, it is the url of the comments page for the item. -->
如果存在，它就是该 item 的评论页面 URL。

`<comments>`http://ekzemplo.com/entry/4403/comments`</comments>`

<!-- More about comments [here](https://www.rssboard.org/rss-weblog-comments-use-case). -->
关于 comments 的更多说明见[这里](https://www.rssboard.org/rss-weblog-comments-use-case)。

---

<!-- ##### `<author>` sub-element of `<item>` -->
##### `<item>` 的 `<author>` 子元素

<!-- `<author>` is an optional sub-element of `<item>`. -->
`<author>` 是 `<item>` 的一个可选子元素。

<!-- It's the email address of the author of the item. For newspapers and magazines syndicating via RSS, the author is the person who wrote the article that the `<item>` describes. For collaborative weblogs, the author of the item might be different from the managing editor or webmaster. For a weblog authored by a single individual it would make sense to omit the `<author>` element. -->
它是该 item 作者的电子邮箱地址。对于通过 RSS 分发内容的报纸和杂志来说，author 就是撰写 `<item>` 所描述文章的人。对于协作式博客，item 的作者可能与 managing editor 或 webmaster 不同。对于由单一作者维护的博客，省略 `<author>` 元素通常也是合理的。

`<author>lawyer@boyer.net (Lawyer Boyer)</author>`


<span id="comments"></span>

<!-- #### Comments -->
#### 补充说明

<!-- RSS places restrictions on the first non-whitespace characters of the data in `<link>` and `<url>` elements. The data in these elements must begin with an [IANA-registered](http://www.iana.org/assignments/uri-schemes) URI scheme, such as http://, https://, news://, mailto: and ftp://. Prior to RSS 2.0, the specification only allowed http:// and ftp://, however, in practice other URI schemes were in use by content developers and supported by aggregators. Aggregators may have limits on the URI schemes they support. Content developers should not assume that all aggregators support all schemes. -->
RSS 对 `<link>` 和 `<url>` 元素中数据的首个非空白字符作出了限制。这些元素中的数据必须以一个[IANA 注册](http://www.iana.org/assignments/uri-schemes)的 URI scheme 开头，例如 `http://`、`https://`、`news://`、`mailto:` 和 `ftp://`。在 RSS 2.0 之前，规范只允许 `http://` 和 `ftp://`；但在实践中，内容开发者已在使用其他 URI scheme，聚合器也提供了支持。聚合器可能会对其支持的 URI scheme 进行限制，因此内容开发者不应假定所有聚合器都支持所有 scheme。

<!-- In RSS 0.91, various elements are restricted to 500 or 100 characters. There can be no more than 15 `<items>` in a 0.91 `<channel>`. There are no string-length or XML-level limits in RSS 0.92 and greater. Processors may impose their own limits, and generators may have preferences that say no more than a certain number of `<item>`s can appear in a channel, or that strings are limited in length. -->
在 RSS 0.91 中，若干元素被限制为最多 500 或 100 个字符。0.91 版本的 `<channel>` 中，`<items>` 的数量不能超过 15 个。而在 RSS 0.92 及更高版本中，不再对字符串长度或 XML 层级施加此类限制。处理器可以自行设定限制，生成器也可能有自己的偏好，例如规定频道中最多只能出现一定数量的 `<item>`，或者字符串长度必须受限。

<!-- In RSS 2.0, a provision is made for linking a channel to its identifier in a cataloging system, using the channel-level category feature, described above. For example, to link a channel to its Syndic8 identifier, include a category element as a sub-element of `<channel>`, with domain "Syndic8", and value the identifier for your channel in the Syndic8 database. The appropriate category element for Scripting News would be <category domain="Syndic8">1765`</category>`. -->
在 RSS 2.0 中，规范通过前文提到的频道级 category 特性，提供了一种把频道链接到某个编目系统（cataloging system）标识符的方法。比如，要把某个频道链接到它在 Syndic8 中的标识符，就可以在 `<channel>` 下加入一个 category 子元素，其 `domain` 为 `Syndic8`，其值为该频道在 Syndic8 数据库中的标识符。对于 Scripting News，对应的 category 元素应为 `<category domain="Syndic8">1765</category>`。

<!-- A frequently asked question about `<guid>`s is how do they compare to `<link>`s. Aren't they the same thing? Yes, in some content systems, and no in others. In some systems, `<link>` is a permalink to a weblog item. However, in other systems, each `<item>` is a synopsis of a longer article, `<link>` points to the article, and `<guid>` is the permalink to the weblog entry. In all cases, it's recommended that you provide the guid, and if possible make it a permalink. This enables aggregators to not repeat items, even if there have been editing changes. -->
关于 `<guid>` 的一个常见问题是：它与 `<link>` 相比有什么区别？它们难道不是同一回事吗？在某些内容系统中，是的；而在另一些系统中，则不是。在某些系统里，`<link>` 就是博客条目的永久链接；但在另一些系统中，每个 `<item>` 只是长文章的摘要，`<link>` 指向文章本身，而 `<guid>` 才是博客条目的永久链接。无论如何，都建议你提供 guid，并且如果可能的话，让它成为永久链接。这样一来，即使条目内容后来经过编辑，聚合器也能避免重复显示。

<!-- If you have questions about the RSS 2.0 format, please post them on the [RSS-Public](http://groups.yahoo.com/group/rss-public) mailing list. The list, maintained by the RSS Advisory Board, serves as a support resource for users, authors and developers who are creating and using content in the format. -->
如果你对 RSS 2.0 格式有疑问，请将问题发布到 [RSS-Public](http://groups.yahoo.com/group/rss-public) 邮件列表。该列表由 RSS Advisory Board 维护，是面向使用、创作和开发该格式内容的用户、作者与开发者的支持资源。

<span id="extending-rss"></span>

<!-- #### Extending RSS -->
#### 扩展 RSS

<!-- RSS originated in 1999, and has strived to be a simple, easy to understand format, with relatively modest goals. After it became a popular format, developers wanted to extend it using modules defined in namespaces, as [specified](http://www.w3.org/TR/REC-xml-names/) by the W3C. -->
RSS 诞生于 1999 年，一直努力保持为一种简单、易懂的格式，而设计目标也相对克制。随着它日渐流行，开发者开始希望按照 W3C [规定](http://www.w3.org/TR/REC-xml-names/)的方式，使用在命名空间中定义的模块对其进行扩展。

<!-- RSS 2.0 adds that capability, following a simple rule. A RSS feed may contain elements and attributes not described on this page, only if those elements and attributes are defined in a namespace. -->
RSS 2.0 增加了这种能力，并遵循一条简单规则：一个 RSS feed 只有在这些元素和属性被定义在某个命名空间中时，才可以包含本页未描述的元素和属性。

<!-- The elements defined in this document are not themselves members of a namespace, so that RSS 2.0 can remain compatible with previous versions in the following sense -- a version 0.91 or 0.92 file is also a valid 2.0 file. If the elements of RSS 2.0 were in a namespace, this constraint would break, a version 0.9x file *would not* be a valid 2.0 file. -->
本文档中定义的元素本身并不属于任何命名空间。这样做是为了让 RSS 2.0 在如下意义上继续与旧版本兼容：一个 0.91 或 0.92 版本的文件，同样也是合法的 2.0 文件。如果 RSS 2.0 的这些元素本身位于命名空间中，那么这一兼容性约束就会被打破，0.9x 版本文件**将不再**是合法的 2.0 文件。

<span id="roadmap"></span>
<!-- #### Roadmap -->

#### 未来规划图
<!-- RSS is by no means a perfect format, but it is very popular and widely supported. Having a settled spec is something RSS has needed for a long time. The purpose of this work is to help it become a unchanging thing, to foster growth in the market that is developing around it, and to clear the path for innovation in new syndication formats. Therefore, the RSS spec is, for all practical purposes, frozen at version 2.0.1. We anticipate possible 2.0.2 or 2.0.3 versions, etc. only for the purpose of clarifying the specification, not for adding new features to the format. Subsequent work should happen in modules, using namespaces, and in completely new syndication formats, with new names. -->

RSS 绝非完美格式，但它非常流行且受到广泛支持。拥有一个稳定定型的规范，是 RSS 长期以来一直需要的事情。这项工作的目的，是帮助它成为一种相对恒定不变的事物，促进围绕它形成的市场继续增长，并为新的聚合格式创新扫清道路。因此，就实际意义而言，RSS 规范在 2.0.1 版本上已经被冻结。未来即便出现 2.0.2、2.0.3 等版本，其目的也只会是澄清规范，而不是为该格式增加新特性。后续工作应通过命名空间中的模块，或者通过全新的、拥有新名称的聚合格式来展开。

<span id="license-and-authorship"></span>

<!-- #### License and authorship -->
#### 许可与作者信息
[![](assets/creative-commons-logo.gif)](https://creativecommons.org/licenses/by-sa/1.0/)

<!-- This document is authored by the [RSS Advisory Board](https://www.rssboard.org/) and is offered under the terms of the Creative Commons [Attribution/Share Alike](https://creativecommons.org/licenses/by-sa/1.0/) license. It is a derivative work of an [original document](https://www.rssboard.org/rss-2-0-1) titled RSS 2.0 published by the Berkman Klein Center for Internet & Society authored by Dave Winer. -->

本文档由 [RSS Advisory Board](https://www.rssboard.org/) 编写，并依据 Creative Commons [Attribution/Share Alike](https://creativecommons.org/licenses/by-sa/1.0/) 许可协议提供。它是对一份名为 RSS 2.0 的[原始文档](https://www.rssboard.org/rss-2-0-1)的衍生作品；该原始文档由 Dave Winer 编写，并由 Berkman Klein Center for Internet & Society 发布。

---

> 主要译者 GPT-5.4，校对 HyFren  
> 原文：[RSS 2.0 Specification (Current)](https://www.rssboard.org/rss-specification)  
> 翻译时间：2026 年 3 月 23 日