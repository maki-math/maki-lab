# 上传指南

​		

> 这是一份用于maki_lab网站课程文本内容的后台上传，编辑与维护的技术文档。
>
> version **0.1**	by **Revot_wyq	date 2020/12/4**

------

### 开始

​	我们推荐使用**typora**进行写作。在typora中使用markdown和LaTeX两种标记语言，尽管它们不能被浏览器直接解析，但可以通过正则表达式~~或者手动慢慢改~~将markdown标签替换为浏览器使用的html标签，搭配LaTeX的渲染脚本，在web页面中展示开发组作者们写作的内容。

### Markdown主题

​	Markdown拥有不同的主题，由一些css样式表所定义，因而可以更换或自定义。要使得在web的显示效果与编辑器中预览效果一致，只需在html中以外部样式表引用的方式引入相应的markdown主题。本文暂时使用typora默认主题[typora_markdown主题库](http://theme.typora.io/)之一的github_theme 。

​	因为我们的网站主要展示的是学术内容，与一般网页的markdown内容不同，相应适合的主题也会有差异。后期可以根据用户们的反馈，优化采用的主题，以实现更佳的阅读体验。还可以增添如定义/定理/证明之类markdown默认语法中不存在的标签。

### MD转换HTML

​	转换的工作可以用一段正则代码来实现。可以用后端脚本在服务器中完成，也可以用前端脚本在浏览器中完成。但为了减轻服务器的压力，和不同浏览器浏览的稳定性，我们最好还是在上传到服务器之前，就用软件转换为html。

| 名称   | markdown       | html                         |
| ------ | -------------- | ---------------------------- |
| 标题   | \#             | \<h1>\</h1>                  |
| 换行   | 双空格或回车   | \<br/>                       |
| 分割线 | ***            | \<hr/>                       |
| 删除线 | \~~内容\~~     | \<del>\</del>                |
| 区块   | >              | \<blockquote>\</blodckquote> |
| 代码   | 四个空格       | \<code>\</code>              |
| 超链接 | \[标题]\(地址) | \<a href="地址">标题\</a>    |
| 表格   | 竖线和短横线   | \<table>\</table>            |

### 使用typora转换

​	typora可以把写好的markdown文档导出成HTML。请按照以下步骤操作：

- 找到选项	**文件**>**偏好设置**>**markdown**>**公式**>**当复制或导出为无格式的HTML时**

  将其更改为	**使用LaTeX 代码**

- **文件**>**导出**>**HTML(without styles)**

### 解析LaTeX

​	相比于在文本中插入公式图片，渲染LaTeX代码显然是更好的显示数学公式的方式。typora中内置的解析器是mathjax，是最早的应用于web端的LaTeX解析器。但是在一些浏览器中，其效果并不理想。使用mathjax解析速度较慢，会先显示LaTeX原始代码，卡顿一下之后才渲染成适合阅读的公式。这种卡顿在网页中包含大量数学公式时，尤为明显。所以我们决定采用更快更轻量的KaTeX作为解析器。

​	 目前我们使用的KaTeX配置如下：

```HTML
<!--使用cdn的镜像-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.css" integrity="sha384-AfEj0r4/OFrOo5t7NnNe46zW/tFgW6x/bCJG8FqQCEo3+Aro6EYUG4+cU+KJWu/X" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.js" integrity="sha384-g7c+Jr9ZivxKLnZTDUhnkOnsh30B4H0rpLUpJ4jAIKs4fnJI+sEnkvrMWph2EDg4" crossorigin="anonymous"></script> 
    <!--定义分界符delimiters属性-->
    <script defer>
        let katex_config = {
            delimiters: 
            [
                {left: "$$", right: "$$", display: true},
                {left: "$", right: "$", display: false},
                {left: "\\(", right: "\\)", display: false},
                {left: "\\[", right: "\\]", display: true}
            ],
            ignoredTags:
            ["script", "noscript", "style", "textarea", "pre", "code", "option"]
        }
    </script>
    <!--启用自动渲染,指定渲染id为contents的DOM元素-->
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/contrib/auto-render.min.js" integrity="sha384-mll67QQFJfxn0IYznZYonOWZ644AWYC+Pt2cHqMaRhXVrursRwvLnLaebdGIlYNa" crossorigin="anonymous"
    onload="renderMathInElement(document.getElementById('contents'),katex_config);"></script>
```

### 如何使用

- 复制以上代码到HTML的头部
- 创建一个用来放置内容的DOM（文本对象模型）元素，一般是\<div>，将其id改为“contents”，只有在这个元素内部的文本，才会被KaTeX解析。
- 将typora导出的HTML代码中，\<body>标签包含的代码，复制到上一步创建的**id="contents"**元素中。

- KaTeX会检索其中由分界符包含的字段，将其判定为LaTeX代码，并渲染为适合阅读的公式样式。

- 我们定义了四种可用的定界符：

  ​	双美元符**\$$**或反斜线加方括号**\\\[**用来标记行间公式

  ```latex
  这是一个$$\int^{+\infin}_{-\infin}e^{\frac{-x^2}{c^2}}dx=c\sqrt{\pi}$$行间公式
  ```

  这是一个$$\int^{+\infin}_{-\infin}e^{\frac{-x^2}{c^2}}dx=c\sqrt{\pi}$$行间公式

  ​	单美元符**\$**或反斜线加圆括号**\\\(**用于标记行内公式

  ```
  这是一个$\int^{+\infin}_{-\infin}e^{\frac{-x^2}{c^2}}dx=c\sqrt{\pi}$行内公式
  ```

  这是一个$\int^{+\infin}_{-\infin}e^{\frac{-x^2}{c^2}}dx=c\sqrt{\pi}$行内公式

### KaTeX支持的规范

​	LaTeX拥有大量的符号，经历了多个不同的细分版本，这使得不同的LaTeX解析器支持的写作规范都略有不同。在网页中，一旦检索到无法识别的LaTeX语法，解析器将会停止，接下来的所有LaTeX代码都将不会被渲染。所以，请尽量使用KaTeX支持的格式进行写作，在上传之前请务必确保使用的语法符合规范。

​	要查询KaTeX支持的规范，[点击这里](https://katex.org/docs/support_table.html#symbols)