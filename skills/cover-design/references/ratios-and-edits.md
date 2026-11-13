# 比例适配与定点修改

## 自然说法怎么落到比例

没指定时**默认只生成一张 4:3**，不默认生成一堆图消耗额度。用户明确的比例或平台规格优先。

| 用户的自然说法 | 生成 |
| --- | --- |
| 没提比例 | 一张 4:3 |
| 「竖版」 | 一张 3:4 |
| 「宽屏」「视频横封面」 | 一张 16:9 |
| 「三个版本」「全部常用比例」 | 4:3、3:4、16:9 各一张，分别重新构图 |

一个多比例批次是同一套文案、同一套配色、三套构图；不要只把第一张拉宽或裁切当成三个版本。

## 同一内容，三种构图

| 比例 | 起始布局 | 关注点 |
| --- | --- | --- |
| 4:3 | 左侧文字，右侧中等大小拼贴 | 长标题先保证可读，必要时缩小插画 |
| 16:9 | 保持左文右图，扩展有意义的场景与间隔 | 不拉伸字形、不额外填满装饰 |
| 3:4 | 标题在上、完整场景在下 | 手、纸签、主物别被裁掉，底部说明留安全区 |

这只是起始布局。用户指定的参考和文字效果优先；不能为了套表而破坏标题。

横版转竖版的编辑请求示例：

```text
Recompose this exact cover into 3:4 portrait, not a crop or stretch.
Keep its exact approved wording, palette and engraved-paper style.
Place label and headline in the upper portion; put the complete meaningful
scene underneath with a quiet gap. Keep the headline the strongest element.
Preserve all illustration subjects and safe margins. Do not add new text.
```

换色请求示例（换预设，锁住其余）：

```text
Keep the exact wording, composition, type scale, engraved-paper style
and 4:3 ratio unchanged. Replace only the palette with the preset
"warm beige / orange": pale #F3E9DC paper, deep #4A3B2F text,
a small #E8A45C accent. Do not redraw the scene or change any character.
```

只改两字请求示例（保留颜色与其余一切）：

```text
Edit only the supporting line: change “收集 · 整理 · 调用” to
“收集 · 整理 · 复用”. Keep all other wording, font appearance, scale,
placement, collage, palette, texture and aspect ratio unchanged.
Use this image as the edit target, not a vague style reference.
```

「蓝一点」「暖一点」按方向在预设内微调即可，不需要用户给色号；「只改字」时颜色一律保留。

## 输出尺寸要说实话

区分「要求的比例」「实际尺寸」和「严格像素规格」。原生生成可能给出
1672×941 这样的近似 16:9 文件，不能把它登记成 1920×1080。用户只要常见
比例时可报告实际像素及取整差异；用户要求精确尺寸时必须满足后再声称完成。

每张成品都应查看，比例正确不能证明文字没漏或审美已通过。多比例交付时明确
列出各自路径与实际尺寸；不要把第一张的通过套给其余图片。
