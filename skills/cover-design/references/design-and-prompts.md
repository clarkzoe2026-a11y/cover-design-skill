# 配色与提示词

## 四套现成配色（内部参考，不让用户挑）

已有品牌色或上文指定色优先；没有指定时，从下面四套完整协调配色里选一套。名字给普通人理解用，色号只用于写提示词，不要求用户懂或先做选择。

| 名字 | 近纸白纸面 | 字与版画刻线 | 标签强调（保守起点） | 大致感觉 |
| --- | --- | --- | --- | --- |
| 苔绿纸 | #F2F6EF | #26352C | #B9CE9E | 清爽、自然 |
| 雾蓝纸 | #F1F5F8 | #293F54 | #A8C3D6 | 安静、理性 |
| 暖米橙纸 | #FCFAF6 | #4A3B2F | #DDB98C | 温和、亲切 |
| 淡紫纸 | #F4F1F8 | #3B3350 | #C4B2DC | 柔和、轻快 |

四套统一在**接近纸白的浅底**上，只带一点微弱色相与细纸纹，深色字/刻线保持对比，强调色只用于标签或一小块纸片；纸面不要整片铺饱和色，也不要加重灰斑。**配色不固定为青色**：四套各自保留色相，用户指定方向时按方向微调即可。四角默认干净，不额外加角落撕纸；内部标签、底部流程纸条与连接纸带保留可见的自然撕边、细纤维和轻纸影；干净四角不等于去掉内部撕纸。表内强调色为保守起点，顶部标签可在同色系内适量提高饱和度、作为小面积亮点，保持深字可读，避免荧光或向全画面扩散。生成色号是指导值，不能仅凭提示词声称图片每个像素严格符合色号。

轮换只用于**可见上下文中彼此独立的新任务**：这类任务未指定颜色时可换一套，避免连续重复；**不声称严格随机，也不依赖跨会话记忆**。**同一主题默认保留已有配色** —— 一个多比例批次共用一套，「只改字」「只改色（含只提浅背景）」或基于现有图继续调整都沿用原配色，只做明度/色相内的微调，不重新选色；只有用户明确说「换个颜色」才换一套预设并锁住文案、构图、字重和比例，「蓝一点」「暖一点」按方向在预设内微调。不额外生成色板图。

暖色背景以 **#FCFAF6** 为起点：暖感主要由深棕刻线、象牙纸片和小面积橙色标签承担，底色只留微弱暖相，不铺成米黄。顶部亮点可参考苔绿 #B7D66C、雾蓝 #85B9DF、暖橙 #E6A354；保持同色系、小面积和深字可读，不提高全图饱和度。

## 一句话请求怎么进提示词

- **只有标题**：标题逐字写进 `EXACT TEXT`，不加标签、副标题、数字、功能、结论或身份；插画只画这个标题能支持的主题，不要求用户补全文。
- **有链接**：先读取正文或可靠本地正文，再走有正文分支；读取失败说明缺口，不把未读正文当成仅标题任务。
- **有正文或摘要**：提炼精准短标题；据实选主题标签、说明或简洁流程，每层各补一条新信息，不硬凑四层；实操文章把实际步骤压缩为底部流程，替代「完整实操」这类空泛重复。仅标题示例中的「不加其他文案」不适用于此分支。不先把脚本文案交给用户审批。
- **完全不给参数**：默认一张 4:3 + 一套现成配色；只有明确说「竖版」「宽屏」「三个版本」才改比例。
- **无论哪条分支**：把文案与层级、主隐喻、字体、留白与边距、背景质感、配色、比例**一次性写进同一条提示词**再生成；不设生成前文案审批关卡，也不承诺一次成功。生成后逐字核对文案并看缩略图，按 SKILL.md 的「检查与交付」自检。
- **16:9先读取[量化版式基线](ratios-and-edits.md#16-9-量化版式基线)**，把外框、各层范围、字形高度与行间净距一起写进完整提示词；不只写「中等字号／多留白」。换比例或长标题时重新设定；文字区域占半幅不等于字形撑满，字图可用纸片叠合联结。

### 示例 A · 仅标题、零参数

```text
Create ONE finished 4:3 Chinese article cover from a blank canvas.
Text-first editorial design, engraved / halftone concept collage,
tactile matte paper, soft cut-paper shadows. This is an independent cover,
not a website screenshot or a device mockup.

BACKGROUND: almost paper-white with only a faint low-saturation color tint
and fine paper grain; deep ink keeps its contrast. All four corners stay
clean uninterrupted paper, no torn-corner decoration. Small paper pieces
belong to the illustration only, not to extra copy.

TYPE: designed contemporary sans-serif for ALL copy, including Chinese,
Latin letters and digits. Main headline is a crisp Bold-700-looking HEITI / grotesk; any supplied
supporting lines use visibly slimmer Regular-400-looking strokes; NO serifs, no Songti, no Ming, no calligraphy.
Antique engraving applies ONLY to the illustration and paper texture.

EXACT TEXT:
Main headline: "把散落笔记变成可复用知识库"
No other copy. Preserve every Chinese character; do not add labels,
subtitles, numbers, claims, identities or extra text.

HIERARCHY: The headline is the first thing read at thumbnail size.
Use a relaxed MEDIUM-size headline, not giant edge-to-edge black lettering,
with natural line breaks and consistent alignment. With only one line of
copy, arrange the headline, illustration, margins and white space as one
harmonious whole; generous outer margins on all four sides. Type has a
left-hand compositional territory of roughly half the canvas, but the
LETTERS do not have to fill it. Type and illustration belong to a single
layered paper composition with a subtle paper connection or gentle overlap
at the edges, not two isolated panels with a rigid gutter. Keep the
illustration quieter than the headline and clear of the Chinese strokes.
(All percentages and sizes here are illustrative for this 4:3 canvas only.)

PALETTE: near-paper-white mist blue #F1F5F8, deep slate-blue #293F54 for
text and etched lines, a small low-saturation blue #A8C3D6 paper accent.
No exact pixel matching claims.

MEANINGFUL SCENE: one core transition only — scattered loose notes are
gathered into a few labeled paper drawers, then one sheet is taken out
and used. One cohesive paper collage, the same result shown ONCE, not a
row of isolated icons or repeated outcomes. Do not invent any real product,
person, URL, statistic or conclusion.

REFERENCES: Use the supplied image for etched-paper technique and editorial
quality only. Do not copy its title, palette or subject automatically.
```

### 示例 B · 有正文的实操文章（四层互补文案 + 单一隐喻）

下面用**另一主题**演示分层写法，不复用任何固定标题或机械主体。

```text
Generate ONE finished 16:9 Chinese article cover from a blank canvas.
Fresh composition, text-first editorial design, engraved / halftone paper
collage, soft cut-paper shadows.

BACKGROUND: almost paper-white, faint low-saturation warm tint, fine paper
grain, deep ink contrast; clean corners, no torn-corner decoration.
The internal label, footer and connecting paper keep natural torn edges,
fine paper fibers and soft shadows; they are not smooth digital cards.

TYPE: designed contemporary sans-serif for ALL copy — crisp bold HEITI
headline with a Bold-700 appearance, Medium-500 label, Regular-400 context
and process with visibly slimmer strokes. No serifs anywhere. Do not fake
weight differences with transparency or gray text; colored label paper
already provides emphasis. Any illustration example text is also Regular.
Engraving is for illustration and paper only.

EXACT COPY, four complementary levels (each adds one piece of information):
small label: 效率方法
context line directly below, smaller: 一次录音到一页结论
main headline, two balanced short lines: 一段录音 / 一页纪要
small bottom process (the article's actual steps, compressed):
转写 · 提炼 · 分点 · 校对
No other text. Preserve all Chinese characters exactly. Do not substitute
a vague "从录音到纪要" long line or repeat the word "完整实操".

LAYOUT CONTRACT for this short-headline 16:9 canvas:
Whole content including paper spans x=8–90%W, y=14–87%H.
Label x=9–34%, y=15–24%; context directly below at x=10–48%, y=27–32%.
Two headline lines within x=9–45%, y=36–72%; visible glyph height
14–16%H per line, gap about 3%H. Label glyphs 4.8–5.5%H,
context 4–4.7%H, footer 3.3–3.8%H.
One secondary illustration x=51–90%, y=27–79%.
Footer torn-paper strip x=8–61%, y=78–87%.
Coordinate origin is top-left. These are coordinated territories, not
a quota to fill with lettering. Link type and image through a quiet paper
edge in the transition area; never cover a stroke. Do not shrink the whole
composition to a tiny center cluster or make giant edge-to-edge type.
Adjust for long titles or other ratios; check actual output, not prompt
compliance by assertion.

PALETTE: near-paper-white warm #FCFAF6 paper, deep #4A3B2F ink, a small
#DDB98C label accent as a starting point; the small label may be a little
more saturated within the same hue to add one controlled highlight.
Keep deep ink legible, no fluorescent color or overall saturation boost.
No exact pixel matching claims.

MEANINGFUL SCENE: ONE core transition — a single waveform paper strip feeds
into one folded summary sheet that emerges with a few neat bullet lines.
One result shown ONCE. Do not draw each process step as a separate object,
no stacked machines, film strips, multiple frames, screens or hands.
A different article needs a different subject and action.

Factual meaning comes only from the article. Do not add unsupported claims
or any additional words.
```

示例 B 的文案、隐喻和数值都只是演示；换主题必须换主体与动作，不把某一篇文章的装置、标题或分层方式当成全主题模板。

## 内容变了，图就应变

- 知识库：散落纸页被整理进分类抽屉，再取出使用。
- 文章转视频（仅此一例）：一张文章页进入一个小型转换装置，输出一张视频卡片，同一结果只出现一次。
- 静图转视频：一张静止小鸟图变为展翅的连续画面。
- 会议录音整理：一条波形纸带收进一张折好的纪要纸。
- 网站迁移：把同一个网站模型从旧展台移到自有服务器。
- 域名备案：给网站挂上地址牌，再完成登记。

这些是叙事起点，不是预制素材库。每篇只表达一个核心转变，同一结果只出现一次；不把正文每步都画出来，不堆机器、胶卷或多个视频帧。换主题就换主体与动作，不把上面某一台装置换字复用到所有文章。不要把抽象「AI」「效率」硬塞进无关机械臂、芯片或机器人；标题没提到的内容不要画进去。
