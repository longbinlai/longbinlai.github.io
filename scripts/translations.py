"""Human-authored Chinese interface and profile translations."""
from html import escape
from html.parser import HTMLParser
from urllib.parse import urljoin

TEXT = {
'Connect ↗':'联系我 ↗','Ideas, projects, and life beyond the code.':'聊聊想法、项目，以及代码之外的生活。','Follow along, or drop me a message.':'关注动态，也欢迎私信交流。',
'Xiaohongshu':'小红书','Scan to follow my notes on AI and everyday life.':'扫码关注，分享 AI 探索与日常生活。','Enlarge QR code ↗':'放大二维码 ↗',
'Enlarge Xiaohongshu QR code':'放大小红书二维码','Xiaohongshu QR code for Robin 同学 AI 生活':'Robin 同学 AI 生活的小红书二维码','Find me on Xiaohongshu':'在小红书找到我','Close QR code':'关闭二维码','Save QR code ↓':'保存二维码 ↓',

'← All talks':'← 全部报告','Talks & courses':'报告与课程','Materials':'资料','Explore this presentation':'查看演示资料','Open the slides or course using the links below.':'通过下方入口打开演示文稿或交互课程。','Presentation resources':'演示资料','Overview':'内容介绍',
'Presentation materials for NeuG, a graph-native data engine for agentic applications.':'NeuG 的演示资料，介绍面向智能体应用的图原生数据引擎。',
'The slides are maintained in a dedicated GitHub repository.':'演示文稿在独立的 GitHub 仓库中维护。',
'Learn how large language models run on GPUs through an interactive course with a course outline and playback and reading controls.':'通过交互课程了解大模型如何在 GPU 上运行，包含课程目录以及播放与阅读界面。',
'The course content is in Chinese. Open the original interactive HTML course from the materials section above.':'课程正文为中文，可通过上方资料入口打开完整的交互式 HTML 课程。',

'How Large Language Models Run on GPUs':'大模型在 GPU 运行时怎么一回事',
'Open course ↗':'打开课程 ↗','An interactive course on large language model inference on GPUs.':'关于大模型在 GPU 上运行与推理的交互式课程。',
'Talks':'报告','Presentations & materials':'报告与演示资料',
'Presentation materials for NeuG.':'NeuG 项目的演示资料。',
'Talks, courses, and presentation materials.':'报告、课程与演示资料汇总。',
'Related paper ↗':'相关论文 ↗',

'Presentation materials':'演示资料','NeuG Slides':'NeuG 演示文稿','Explore the NeuG presentation repository.':'查看 NeuG 演示文稿仓库。','View slides repository ↗':'查看演示文稿仓库 ↗',
'Portrait of Longbin Lai':'Longbin Lai 的照片','Work':'项目','Research':'研究','Writing':'文章','About':'关于',
'Skip to content':'跳转到正文','Main navigation':'主导航','Longbin Lai home':'返回首页',
'Research & Engineering':'研究与工程','Researcher & engineer · Graphs / Data / AI':'研究与工程 · 图 / 数据 / 人工智能',
'Building systems that make':'构建数据系统，','connected data useful.':'释放关联数据的价值。',
'Staff Engineer at Token Foundry. My work spans graph databases, distributed processing, query optimization, and applications of large language models.':'现任 Token Foundry Staff Engineer，研究与工程工作涵盖图数据库、分布式处理、查询优化，以及大语言模型应用。',
'Email ↗':'邮件 ↗','Google Scholar ↗':'谷歌学术 ↗','CV ↗':'简历 ↗',
'01 / Engineering':'01 / 工程实践','Systems & open source':'系统与开源','All projects ↗':'全部项目 ↗',
'Featured open-source project':'精选开源项目',
'A graph-native data engine for agentic applications. Graph, vector, and full-text retrieval over the same transactional data, embedded in your application or running as a service.':'面向智能体应用的图原生数据引擎。在同一份事务数据上统一进行图、向量与全文检索，可嵌入应用，也可作为独立服务运行。',
'Explore NeuG ↗':'了解 NeuG ↗','Source code ↗':'源代码 ↗',
'STRUCTURE':'图结构','SEMANTICS':'语义','KEYWORDS':'关键词',
'02 / Research':'02 / 学术研究','Selected publications':'代表论文','All publications ↗':'全部论文 ↗',
'03 / Notes':'03 / 思考与记录','Recent writing':'近期文章','All writing ↗':'全部文章 ↗',
'04 / Background':'04 / 个人背景','A little about me':'关于我','Education':'教育经历','Research interests':'研究兴趣',
'PhD in Computer Science and Engineering':'计算机科学与工程博士','Master in Computer Engineering':'计算机工程硕士','BSc in Information Security':'信息安全学士',
'University of New South Wales, Sydney · 2017':'新南威尔士大学，悉尼 · 2017',
'Shanghai Jiao Tong University · 2013':'上海交通大学 · 2013','Shanghai Jiao Tong University · 2010':'上海交通大学 · 2010',
'Big Data Management · Graph Database · Distributed Processing · Query Optimizations · Large Language Models':'大数据管理 · 图数据库 · 分布式处理 · 查询优化 · 大语言模型',
'Get in touch':'联系我','Let’s connect.':'期待交流。','Research, open source, and conversations about data systems.':'欢迎交流学术研究、开源项目与数据系统。',
'Graphs, systems, and the ideas between them.':'探索图、系统，以及连接它们的思想。',
'Research archive':'研究成果','Publications':'学术论文','Graph data management, distributed computing, and query optimization.':'图数据管理、分布式计算与查询优化。',
'Search publications':'搜索论文','Filter by year':'按年份筛选','Search by title, author, or venue':'搜索标题、作者或会议期刊','All years':'全部年份',
'No matching publications. Try another title, author, or year.':'没有找到匹配的论文，请尝试其他标题、作者或年份。',
'Notes & perspectives':'记录与观点','Open source & systems':'开源与系统','Projects':'项目',
'← Home':'← 返回首页','← Home':'← 返回首页','Abstract':'摘要（英文原文）',
'publication':'学术论文','project':'项目','post':'文章','talk':'报告','courses':'课程','slides':'幻灯片',
'Code ↗':'代码 ↗','Docs ↗':'文档 ↗','Slides ↗':'幻灯片 ↗','Video ↗':'视频 ↗','Blog ↗':'博客 ↗',
'Graph, vector, and full-text retrieval connected in one data engine':'同一数据引擎连接图、向量和全文检索',
'GRAPH DATABASE / DISTRIBUTED SYSTEM':'图数据库 / 分布式系统',
'Graph Database / Distributed System':'图数据库 / 分布式系统',
'Graph Database / Query Language':'图数据库 / 查询语言',
'Distributed System / Query Execution Engine':'分布式系统 / 查询执行引擎',
'Graph Database / Graph Pattern Matching':'图数据库 / 图模式匹配',
'A Graph-Native Query Optimization Framework':'图原生查询优化框架',
'Interactive Graph Pattern Matching':'交互式图模式匹配',
'Interactive Analysis on Distributed Graphs Using Gremlin Language':'基于 Gremlin 的分布式图交互分析',
'A High-Throughput Transactional Graph Database':'高吞吐事务图数据库',
'Distributed Pattern Matching System with Cypher':'基于 Cypher 的分布式模式匹配系统',
'We develop GLogS system, allowing users to interactively submit queries using a declarative language, which will be compiled and automatically optimized, and eventually executed on the GAIA dataflow engine.':'GLogS 支持用户使用声明式语言交互提交图查询，自动完成编译与优化，并在 GAIA 数据流引擎上执行。',
'GOpt is built on top of a unified intermediate representation (IR) that is capable of capturing both graph and relational operations, thereby streamlining the optimization of graph queries.':'GOpt 基于统一中间表示（IR），同时表达图操作与关系操作，从而在同一框架中优化复杂图查询。',
'GAIA (former name, Pegasus) is a distributed data-parallel compute engine based on the cyclic dataflow computation model. GAIA serves as the computation engine, lying at the core of the GraphScope system. Users can construct the computation via a directed acyclic graph (DAG), and easily run the job on their laptop or even a distributed environment across a cluster of computers.':'GAIA（原名 Pegasus）是基于循环数据流模型的分布式数据并行计算引擎，也是 GraphScope 的核心计算引擎。用户可以通过有向无环图构建计算任务，并在笔记本或分布式集群中运行。',
'GraphScope Interactive is a specialized construction of GraphScope Flex, designed to handle concurrent graph queries at an impressive speed. Its primary goal is to process as many queries as possible within a given timeframe, emphasizing a high query throughput rate.':'GraphScope Interactive 基于 GraphScope Flex 构建，面向高并发图查询，通过高效执行提升查询吞吐量。',
'To develop a graph pattern matching system in the distributed context, while gluing together the academic results of optimal join algorithms and industrial efforts of query language':'将最优连接算法的研究成果与工业查询语言相结合，构建分布式图模式匹配系统。',
'Page not found':'页面未找到','This page has moved.':'这个页面已迁移。',
}

BIO = '''<p>我先后于 2010 年和 2013 年获得上海交通大学学士与硕士学位，随后在澳大利亚新南威尔士大学计算机科学与工程学院数据库组攻读博士，师从<a href="https://www.acem.sjtu.edu.cn/en/faculty/linxuemin.html">林学民教授</a>与<a href="https://www.uts.edu.au/staff/lu.qin">覃路教授</a>，于 2017 年 3 月获得博士学位。<a href="http://unsworks.unsw.edu.au/fapi/datastream/unsworks:45376/SOURCE02?view=true">博士论文 ↗</a></p><p>加入阿里巴巴后，我参与构建服务于电商平台的大规模图数据分析系统，也是 <a href="https://github.com/alibaba/graphscope">GraphScope</a> 开源项目的主要贡献者之一。相关工作包括分布式图查询数据流系统 GAIA、交互式图模式匹配系统 GLogS，以及统一图查询优化框架 GOpt。目前，我在 Token Foundry 开展大语言模型创新应用的研究与开发。</p>'''

class Translator(HTMLParser):
    def __init__(self, route):
        super().__init__(convert_charrefs=True)
        self.route=route
        self.parts=[]
    def handle_starttag(self, tag, attrs):
        out=[]
        for key,value in attrs:
            if value is None:out.append(key);continue
            if tag=='html' and key=='lang':value='zh-CN'
            elif key in ['aria-label','placeholder','alt']:value=TEXT.get(value,value)
            elif tag=='a' and key=='href':
                if value.startswith('/') and not value.startswith('//') and not value.startswith(('/files/','/assets/','/images/')) and '.pdf' not in value and '.bib' not in value and '.html' not in value:
                    value='/zh'+value
                elif not value.startswith(('/', '#')) and '://' not in value and not value.startswith('mailto:'):
                    value=urljoin(self.route,value)
            elif tag in ['img','source'] and key=='src' and not value.startswith(('/', 'http','data:')):value=urljoin(self.route,value)
            elif tag=='link' and key=='href' and value.startswith('https://longbinlai.github.io'):
                value=value.replace('https://longbinlai.github.io','https://longbinlai.github.io/zh',1)
            elif tag=='meta' and key=='content' and value.startswith('https://longbinlai.github.io'):
                value=value.replace('https://longbinlai.github.io','https://longbinlai.github.io/zh',1)
            out.append(f'{key}="{escape(value,quote=True)}"')
        self.parts.append('<'+tag+(' '+' '.join(out) if out else '')+'>')
    def handle_endtag(self,tag):self.parts.append('</'+tag+'>')
    def handle_data(self,data):
        stripped=data.strip()
        translated=TEXT.get(stripped,stripped)
        if stripped.startswith('Related publication · '): translated=stripped.replace('Related publication', '关联论文')
        if stripped: data=data.replace(stripped,translated,1)
        self.parts.append(escape(data,quote=False))
    def handle_entityref(self,name):self.parts.append('&'+name+';')
    def handle_charref(self,name):self.parts.append('&#'+name+';')
    def handle_decl(self,decl):self.parts.append('<!'+decl+'>')
    def handle_comment(self,data):self.parts.append('<!--'+data+'-->')

def chinese(document,route,biography=''):
    if biography:document=document.replace(biography,BIO)
    t=Translator(route);t.feed(document)
    result=''.join(t.parts)
    result=result.replace('href="/zh/zh'+route+'" class="language-toggle"','href="'+route+'" class="language-toggle"').replace('aria-label="切换到中文"','aria-label="Switch to English"').replace('>中文</a>','>EN</a>')
    return result
