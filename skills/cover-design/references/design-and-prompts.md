# 配色与提示词

## 几套现成配色（内部参考，不让用户挑）

已有品牌色或上文指定色优先；没有指定时，从下面几套完整协调配色里选一套。名字是给普通人理解用的，色号只用于写提示词，不要求用户懂或先做选择。

| 名字 | 纸面 | 字与版画刻线 | 强调 | 大致感觉 |
| --- | --- | --- | --- | --- |
| 苔绿纸 | #EDF2DF | #26352C | #DDFB78 | 清爽、自然 |
| 雾蓝纸 | #E3EBF2 | #293F54 | #9FC0D8 | 安静、理性 |
| 暖米橙纸 | #F3E9DC | #4A3B2F | #E8A45C | 温和、亲切 |
| 淡紫纸 | #EEE9F4 | #3B3350 | #C9B3E6 | 柔和、轻快 |

几套都是浅底深字：深色字负责可读，强调色只用于标签或一小块纸片。浅色字直接放在浅纸上可能对比不足，应改为深字配浅色底。生成色号是指导值，不能仅凭提示词声称图片每个像素严格符合色号。

轮换只用于**可见上下文中彼此独立的新任务**：这类任务未指定颜色时可换一套，避免连续重复；**不声称严格随机，也不依赖跨会话记忆**。**同一主题默认保留已有配色** —— 一个多比例批次共用一套，「只改字」或基于现有图继续调整都沿用原配色，不重新选色；只有用户明确说「换个颜色」才换一套预设并锁住文案、构图、字重和比例，「蓝一点」「暖一点」按方向在预设内微调。不额外生成色板图。

## 一句话请求怎么进提示词

- **只有标题**：标题逐字写进 `EXACT TEXT`，不加标签、副标题、数字、功能、结论或身份；插画只画这个标题能支持的主题，不要求用户补全文。
- **有正文或摘要**：先提炼一句核心标题，其余文字不硬凑；不先把脚本文案交给用户审批。
- **完全不给参数**：默认一张 4:3 + 一套现成配色；只有明确说「竖版」「宽屏」「三个版本」才改比例。

仅标题、零参数的提示词示例：

```text
Create ONE finished 4:3 Chinese article cover.
Art direction: text-first editorial design, engraved / halftone concept collage,
tactile matte paper, soft cut-paper shadows, generous breathing room.
This is an independent cover, not a website screenshot or a device mockup.

EXACT TEXT:
Main headline: “把散落笔记变成可复用知识库”
No other copy. Preserve every Chinese character; do not add labels,
subtitles, numbers, claims, identities or extra text.

HIERARCHY:
The headline is the first thing read at thumbnail size. Clear bold Chinese
sans-serif, natural line breaks, consistent alignment, roughly left half for
type, illustration secondary, 7–8% safe margins, a quiet gap between them.

PALETTE:
Pale paper #E3EBF2, deep slate-blue #293F54 for text and etched lines,
a small muted blue #9FC0D8 paper accent. No exact pixel matching claims.

MEANINGFUL SCENE:
Scattered loose notes are gathered into a few labeled paper drawers,
then one sheet is taken out and used. One cohesive paper collage,
not a row of isolated icons. Do not invent any real product, person,
URL, statistic or conclusion.

REFERENCES:
Use the supplied image for etched-paper technique and editorial quality only.
Do not copy its title, palette or subject automatically.
```

## 内容变了，图就应变

- 知识库：散落纸页被整理进分类抽屉，再取出使用。
- 静图转视频：一张静止小鸟图变为展翅的连续画面。
- 网站迁移：把同一个网站模型从旧展台移到自有服务器。
- 域名备案：给网站挂上地址牌，再完成登记。

这些是叙事起点，不是预制素材库。不要把抽象「AI」「效率」硬塞进无关机械臂、芯片或机器人；标题没提到的内容不要画进去。
