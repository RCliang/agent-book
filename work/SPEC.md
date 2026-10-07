# 《Agentic AI 指南》演示文稿 · 设计系统与片段制作规范 v1.0

你(子代理)的任务:阅读指定的书籍章节文本,把章节内容**忠实提炼**为演示幻灯片 HTML 片段。
本规范是唯一权威:只使用这里给出的类名与结构,不要自造 CSS/JS,不要外部资源。

## 一、设计概念:夜航图(Night Chart)

全书是一条「从 LLM 基础 → 强化学习对齐 → 推理 → 评估 → 智能体」的学习航线。
视觉=深靛蓝夜航图:航图网格、坐标刻度、三色信标、每章一条航线(stroke 动画)。
气质:严谨的工程手册 + 精美的航海图。**克制**:动效只用在航线绘制与块级入场,不做花哨装饰。

### 调色板(CSS 变量,已在壳中定义,直接用 var() 引用)
| 变量 | 值 | 用途 |
|---|---|---|
| `--paper` | #EAF0FA | 主文本 |
| `--muted` | #93A6C8 | 次文本/正文 |
| `--faint` | #5E739A | 弱化标注 |
| `--verm` | #FF5238 | 朱砂:关键词、强调数字、下划线 |
| `--amber` | #FFC24B | 航标金:节点、数字、徽标 |
| `--cyan` | #4EC9D4 | 信标青:图表线条、箭头、标签 |
| `--ink0` | #0A1424 | 最深底色(代码块底) |
| `--ink1` | #0E1930 | 面板底 |
| `--ink2` | #14213B | 卡片底 |
| `--line` | rgba(150,180,255,.14) | 边框 |
| `--verm-bg` | rgba(255,82,56,.09) | 朱砂浅底(callout) |
| `--cyan-bg` | rgba(78,201,212,.08) | 青浅底 |

### 字体(壳已定义)
- 展示标题(章节名):`--serif`(宋体系),自动应用在 `.k-h`
- 正文:`--sans`(苹方/思源黑),自动应用
- 标注/数字/代码/眉题:`--mono`,用 `.k-eyebrow .k-tag .k-num .k-code` 或 `font-family:var(--mono)`

## 二、幻灯片骨架(必须严格照抄结构)

画布固定 1280×720,被壳居中缩放。**内容必须放得下**:正文区高度约 400px(头部约 190px + 底栏 34px 之后)。

```html
<section class="slide" id="c21a" data-part="5" data-crumb="PART V · RAG" data-title="RAG:检索增强生成">
  <header class="s-head">
    <div class="k-eyebrow"><span class="tag">PART V · CH 02</span><span class="dim">书 p292-314</span></div>
    <h2 class="k-h">检索增强生成 <em>RAG</em></h2>
    <p class="k-lede">一段 1-2 句的导语,概括本章要旨,≤ 90 字。</p>
  </header>
  <div class="s-body">
    <!-- 内容区,见组件词表 -->
  </div>
  <div class="route">…本章航线 SVG,见第四节…</div>
  <footer class="s-foot"><span>《Agentic AI 指南》中文版 v1.1.0</span><span class="dot">·</span><span>p292-314</span></footer>
</section>
```

规则:
- `<section>` 上必须有唯一 `id`、`data-part`(1-6)、`data-crumb`(眉题短语,如 `PART II · PPO`)、`data-title`(导航/目录用短标题,≤ 14 字)。
- 一页幻灯片只讲一个主题;**宁可拆两页,不要塞爆**。
- 所有可引数据必须来自书文本,并在 `data-crumb` 旁或 `.s-foot` 标注书页码(pXXX)。
- 禁止 emoji、禁止外部图片/字体/CDN、禁止 `<style>` `<script>`、禁止 lorem。代码示例用 `.k-code`,每段 ≤ 6 行。

## 三、组件词表(只有这些,自由组合)

```html
<div class="grid3">                 <!-- 三列网格;另有 grid2 grid4 -->
  <div class="k-card fu" style="--d:.05s">
    <div class="k-card-t">卡片标题</div>
    <div class="k-card-b">正文 ≤ 60 字,可含 <b class="hl">朱砂强调</b> 与 <span class="cy">青强调</span>。</div>
  </div>
</div>

<div class="k-num"><b>4-16</b><span>GRPO 组大小(经验值)</span></div>   <!-- 大数字+小标签,可放卡片内 -->

<ul class="k-flow">                  <!-- 流程链:项间自动加箭头 -->
  <li>编排器生成计划</li><li>Worker 并行执行</li><li>结果聚合</li>
</ul>

<table class="k-table">              <!-- 紧凑表格:thead 用 mono 小字 -->
  <thead><tr><th>方法</th><th>是否需要 critic</th></tr></thead>
  <tbody><tr><td>PPO</td><td>需要</td></tr></tbody>
</table>

<p class="k-quote">引用/金句,serif 斜体感<span class="k-cite">— 书 p136</span></p>

<div class="k-callout"><b>要点</b> 一句话关键提醒/反直觉结论,≤ 50 字。</div>

<div class="k-code"><pre>prompt = "..."</pre></div>

<div class="k-compare">              <!-- 左右对比,中间 VS -->
  <div class="k-col"><div class="k-card-t">在线 DPO</div><div class="k-card-b">…</div></div>
  <div class="vs">VS</div>
  <div class="k-col"><div class="k-card-t">离线 DPO</div><div class="k-card-b">…</div></div>
</div>

<span class="k-tag">RLHF</span> <span class="k-tag cy">TRL</span> <span class="k-tag am">2024</span>  <!-- 小徽标 -->

<div class="fig"><svg viewBox="0 0 860 400" role="img" aria-label="…">…</svg>
  <div class="figcap">图:标题与一句话解读</div></div>
```

入场动画:给主块加 `class="fu"` 与 `style="--d:.1s"`(0~.45s 内交错)。**不要**给所有小元素都加。

## 四、签名元素:章节航线(route band)

每页底部(在 `.s-foot` 之上)有一条本章「航线」:一条曲线串起 3-5 个本章概念节点。
**写法固定**(节点为圆点+等宽小标签,上下交替 y=26/54):

```html
<div class="route"><svg viewBox="0 0 1160 80" preserveAspectRatio="xMidYMid meet">
  <path class="route-path" pathLength="1" d="M20,44 C180,10 340,74 520,44 S900,10 1140,44"/>
  <g class="rn" style="--d:.25s" transform="translate(180,32)"><circle r="4.5"/><text y="-10">分词</text></g>
  <g class="rn" style="--d:.55s" transform="translate(520,44)"><circle r="4.5"/><text y="-10">注意力</text></g>
  <g class="rn" style="--d:.85s" transform="translate(860,26)"><circle r="4.5"/><text y="-10">解码</text></g>
</svg></div>
```

- path 端点固定 `M20,44` 与 `x=1140`;中间用平滑 C/S 曲线;节点圆心放**在路径上**(估算即可,y 在 12-72 之间)。
- 每页 3-5 个节点;节点文字 ≤ 6 字;不要与其他元素重叠的担心——route 独占底部条带。
- 若页面已有 `.fig` 大图且空间紧张,route 仍须保留(它是签名,不可省)。

### SVG 图(.fig 内)绘制规则
- viewBox 用 `0 0 860 400` 或 `0 0 860 340`;线条 `stroke="var(--cyan)"` 宽 1.5-2;填充面 `fill="var(--cyan-bg)"` / `var(--verm-bg)`;
- 文本默认样式已由壳的 CSS 提供(13px 苹方、paper 色),只需写 `<text x y>内容</text>`;次要文本加 `class="mut"`,等宽数字/坐标加 `class="m"`;需要调大小时写内联 `style="font-size:16px;font-weight:700"`;
- 强调节点:圆 `fill="var(--ink0)" stroke="var(--amber)"`,强调路径 `stroke="var(--verm)"`;
- 箭头用 marker 或手绘小三角 `fill="var(--cyan)"`;
- 可动元素加 `class="draw"`(线条描画)或 `class="pop"`(节点浮现),最多 6 个动效元素;
- 结构类图(架构/流水线/拓扑)优先:框+箭头+分区,不画 3D、不画渐变。

## 五、内容提炼准则(最重要的三条)

1. **忠实原文**:所有事实、数字、公式、术语(中英对照)必须来自章节文本;不得编造;术语首次出现给英文,如「组相对策略优化(GRPO)」。
2. **提炼为讲义,不是压缩原文**:每页回答「这一章最重要的一件事是什么」,再配 2-4 个支撑点;数字优先(显存 O(N²)→O(N)、clip ε=0.2、β 0.1-0.5、group 4-16 这类);反直觉结论放进 `.k-callout`。
3. **每页必须有一张图或一个表**:结构图(`.fig` SVG)、对比表(`.k-table`)、或流程链(`.k-flow`)至少其一;`.fig` 大图每页最多一张。

### 页面类型模板(按内容选)
- **概念页**:lede + 左侧 2-3 卡片 + 右侧 `.fig` 结构图 + route
- **算法页**:lede + `.k-flow`(步骤链) + 关键公式卡(`.k-code` 或 SVG 内数学文本) + 复杂度/超参 `.k-num` 行 + route
- **对比页**:lede + `.k-table`(3-5 行) 或 `.k-compare` + `.k-callout` 选型结论 + route
- **全景页**(大章第二页):lede + grid4 卡片(子领域速览) + route

## 六、产出与自检清单

- 每个片段文件只含 1 个 `<section>`(除非任务明确要 2 个),UTF-8,无 BOM。
- 自检:① id/crumb/title 齐全 ② route 存在 ③ 图或表至少其一 ④ 无外部资源 ⑤ 卡片正文 ≤ 60 字 ⑥ 页码已标 ⑦ 汉字标点(「」·——)。
- 文件写到任务指定的绝对路径。不要动其他文件。

## 七、代码讲解页(代码实战)规范

在概念页之外,本管线新增「代码实战」页:取书中真实代码示例,重排缩进后配上逐点讲解。

### 骨架
```html
<section class="slide" id="c27codea" data-part="5" data-crumb="PART V · 代码 22" data-title="MCP Server:FastMCP">
  <header class="s-head">
    <div class="k-eyebrow"><span class="tag am">CODE</span><span class="dim">Listing 22.1 · 书 p406-407</span><span class="tag c">Python</span><span class="tag c">mcp[cli]</span></div>
    <h2 class="k-h">…标题…<span class="en">…副题…</span></h2>
    <p class="k-lede">一句话:这段代码演示什么、对应书中哪个机制。≤ 80 字。</p>
  </header>
  <div class="s-body">
    <div class="split-58">
      <div class="k-code tall fu" style="--d:.05s"><pre>…代码,≤ 22 行…</pre></div>
      <div class="col">
        <div class="k-card fu" style="--d:.15s"><div class="k-card-t"><span class="no">①</span>讲解标题</div><div class="k-card-b">为什么这样写、对应书中哪个机制、常见坑。≤ 70 字。</div></div>
        <!-- 共 3-4 张 -->
      </div>
    </div>
    <div class="k-callout g fu" style="--d:.4s"><b>运行</b>依赖与安装命令 · 启动命令 · 预期输出(一句话)。</div>
  </div>
  <div class="route">…标准航线 band…</div>
  <footer class="s-foot">…</footer>
</section>
```

### 硬性规则
1. **代码忠实原书**:来自章节文本中的 Listing/代码块;允许:重排缩进、为省行数删去与本页讲解无关的分支(以 `...` 注释标示)、加 ①②③ 序号注释。不允许:改写逻辑、编造书中没有的 API。
2. 代码 ≤ 22 行(不含空行可放宽到 26);长代码拆两页或用 `...` 截断,优先保留讲解点所在行。
3. 讲解卡 3-4 张,编号 ①②③ 与代码内注释**一一对应**;每张 ≤ 70 字,讲「为什么」,不复述代码字面。
4. `.k-callout.g`(青色)写「运行」:安装/启动命令 + 预期输出一句话。命令用书中的(如 `mcp run notes_server.py`)。
5. 高亮 span:`<span class="c">` 注释、`<span class="k">` 关键字/装饰器、`<span class="s">` 字符串、`<span class="f">` 函数/方法名。整段代码外不要加高亮时保持纯文本。
6. data-crumb 用 `PART … · 代码 NN`(NN=书章号);data-title ≤ 14 字;其余(route/页脚/fu 动效)与概念页一致。
