# 比例适配与定点修改

## 自然说法怎么落到比例

没指定时**默认只生成一张 4:3**，不默认生成一堆图消耗额度。用户明确的比例或平台规格优先。

| 用户的自然说法 | 生成 |
| --- | --- |
| 没提比例 | 一张 4:3 |
| 「竖版」 | 一张 3:4 |
| 「宽屏」「视频横封面」 | 一张 16:9 |
| 「三个版本」「全部常用比例」 | 4:3、3:4、16:9 各一张，分别重新构图 |

一个多比例批次是同一套文案、同一套配色、三套构图；不要只把第一张拉宽或裁切当成三个版本。布局表里的方位、占比、字号、边距都只是该画幅的**起始示例**，换比例或标题长度要重新设定，不硬编码到所有画幅。

## 16:9 量化版式基线

适用于浅纸版画、左文右图、短主标题的横版；来自已获用户通过的样本，不是行业标准。左上为原点，x按画布宽度、y按高度计算。先固定整组信息，再安排内部层级；区域是容器，不要求字形铺满。

| 区域 | x范围 | y范围 |
| --- | --- | --- |
| 整组内容外框（含纸片） | 8%–90% | 14%–87% |
| 左侧文字分配区 | 9%–59% | 15%–86% |
| 标签 | 9%–34% | 15%–24% |
| 标签下方的说明 | 10%–48% | 27%–32% |
| 两行短主标题 | 9%–45% | 36%–72% |
| 右侧核心插画 | 51%–90% | 27%–79% |
| 底部流程／摘要纸条 | 8%–61% | 78%–87% |

实际字形高度：主标题每行约14%–16%H，标签4.8%–5.5%H，说明4%–4.7%H，底部3.3%–3.8%H；两行主标题字形间净距约3%H。以1672×940为例，分别约132–150px、45–52px、38–44px、31–36px，行间净距约28px。这是字形可见高度，不等于某排版软件的font-size。

**字重与信息优先级**：使用同一现代无衬线家族，先分配层级再定字号；彩色纸片已承担标签强调，标签文字不再叠加粗黑。

| 层级 | 字重外观方向 | 与主标题的关系 |
| --- | --- | --- |
| 主标题 | Bold，约700的视觉感 | 唯一最强文字，开放字腔，避免900式堵黑 |
| 标签 | Medium，约500 | 色块负责亮点，笔画居中 |
| 主题说明 | Regular，约400 | 明显细于主标题，保持深字可读 |
| 底部摘要／流程 | Regular，约400 | 分隔点也不加粗，不做成多个卖点标题 |
| 插画内的例句／标记 | Regular，约400；关键单字最多Medium | 只解释插画，不成为另一处标题 |

数值是生成方向，不代表栅格成图包含可验证的真实font-weight。复核同一字高下的可视笔画差异，Regular大致比主标题细约35%–45%，标签居中；不要通过灰字或透明度冒充细字。保留整体占区与清楚的垂直停顿，不为降密度把整组缩成中央小团。标签约46–50px、说明38–41px、摘要33–36px可作1672×941下的起点，换字数／比例时重新协调。

3–4字一行的标题按此起步；两行保持相同字号，不把较短一行拉宽对齐。长标题优先依正文精准压缩；用户锁定原话则自然分行并适量减字号，不删改指定文字。标签／说明／摘要缺省时重排其余元素，不留空槽、不硬造文案。字图可在x约48%–59%的过渡带用安静纸面联结，不盖字形笔画。

标签以同色系较鲜明的颜色小面积提亮、保持深字可读；标签、底部纸条与连接纸带保留自然撕边、细纤维及浅纸影。画布四角干净不等于把内部纸片做成平滑卡片。

**生成后复核**：先看整组是否接近目标外框，再看局部。深色有效信息包围框可参考左界8%–11%、上界15%–19%、右界87%–92%、下界82%–86%，包围框面积约50%–58%。同法比较的已通过样本约52%和57%；过空候选约36%–39%。这里是包围框面积，不是墨色像素覆盖率；阈值与纸张颜色会影响测量，超范围触发人工复核，不能据此自动裁切或判定美感。

需要数值辅助时可用同一口径比较：每2像素采样，亮度阈值145，行列至少8个深色样本，浅底与浅纸片排除；也可目测区域，不强制安装图像依赖。原生生成只能近似执行百分比，报告实际偏差，不冒称精确坐标。严格坐标交付需要单独采用确定性排版，不把提示词当成精确排版工具。

4:3与3:4需按画幅重新构图，不能直接套用本表。用户明确指定的布局和参考优先。

## 同一内容，三种构图

| 比例 | 起始布局 | 关注点 |
| --- | --- | --- |
| 4:3 | 左侧文字，右侧中等大小拼贴 | 长标题先保证可读，必要时缩小插画 |
| 16:9 | 左文右图为起点，扩展有意义的场景与间隔 | 不拉伸字形、不额外填满装饰 |
| 3:4 | 标题在上、完整场景在下 | 手、纸签、主物别被裁掉，底部说明留安全区 |

左文右图 / 上文下图只是起点，不是强制两栏：字图可通过纸片延伸与适度叠合成为一个整体，文字压在安静图面上时保持清晰，不设硬性分隔带。文字区域占半幅不等于字形撑满，16:9先检查上面的整组外框，再协调局部大小；既不靠巨黑字填满，也不同时扩大边距、缩小字号和插画。用户指定的参考和文字效果优先；不能为了套表而破坏标题。

横版转竖版的重新构图示例（每个比例单独生成，可作风格参考，不裁切拉伸）：

```text
Generate a fresh 3:4 portrait composition of the same article cover,
not a crop or stretch. Keep its exact approved wording, palette and
engraved-paper style. Place label and headline in the upper portion; put
the complete meaningful scene underneath with comfortable breathing room.
Type and illustration may meet through a small paper connection or gentle
overlap, with no rigid divider. Keep the headline the strongest element.
Preserve all illustration subjects and safe margins. Do not add new text.
```

换色请求示例（换预设，锁住其余）：

```text
Keep the exact wording, composition, type scale, engraved-paper style
and 4:3 ratio unchanged. Replace only the palette with the preset
"warm beige / orange": near-paper-white #FCFAF6 paper, deep #4A3B2F text,
a small low-saturation #DDB98C accent. All copy stays contemporary
sans-serif and the four corners stay clean. Do not redraw the scene or
change any character.
```

只改两字请求示例（保留颜色与其余一切）：

```text
Edit only the supporting line: change “收集 · 整理 · 调用” to
“收集 · 整理 · 复用”. Keep all other wording, font appearance, scale,
placement, collage, palette, texture and aspect ratio unchanged.
Use this image as the edit target, not a vague style reference.
```

只提浅背景请求示例（只改色，仍走定点编辑）：

```text
Edit the supplied cover. Make ONLY the canvas background lighter: replace
the pale tinted paper with an airy almost-paper-white version, keeping a
faint low-saturation tint and fine paper grain. Do NOT apply a global
brightness filter. Preserve the deep ink of ALL text and engraved lines,
the label accent, ivory paper pieces, line contrast, tiny soft shadows,
typography, text sizes, margins and precise positions. Do not redraw,
simplify, add or move any subject. All four corners stay clean. This is a
background-only lightness adjustment, not a new composition.
```

「蓝一点」「暖一点」「再浅一点」按方向在预设内微调即可，不需要用户给色号；「只改字」时颜色一律保留。

## 重新生成还是定点编辑

两者按**用户意图**区分，不一刀切禁止编辑，也不在旧图上不断补丁：

| 用户意图 | 做法 |
| --- | --- |
| 只改字、只换色 / 只提浅背景 | 定点编辑：以指定现有图为编辑目标，锁住其余文案、字形、配色、构图与比例 |
| 整体重设计，或明确说「重新生成」「别在旧图上改」 | 从新画布生成：不传旧图作编辑目标，把文案、层级、主隐喻、留白、字体、背景、配色、比例一次性写进同一条提示词重新构图 |

多次局部修改叠加到画面失衡时，提示用户可选从新画布重生成，由用户决定；不私自把已认可的图当草稿反复覆盖。每个版本另存，保留旧版。

## 输出尺寸要说实话

区分「要求的比例」「实际尺寸」和「严格像素规格」。原生生成可能给出
1672×941 这样的近似 16:9 文件，不能把它登记成 1920×1080。用户只要常见
比例时可报告实际像素及取整差异；用户要求精确尺寸时必须满足后再声称完成。

每张成品都应查看，比例正确不能证明文字没漏或审美已通过。多比例交付时明确
列出各自路径与实际尺寸；不要把第一张的通过套给其余图片。
