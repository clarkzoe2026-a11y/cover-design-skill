# 比例适配与定点修改

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

单字修改请求示例：

```text
Edit only the supporting line: change “收集 · 整理 · 调用” to
“收集 · 整理 · 复用”. Keep all other wording, font appearance, scale,
placement, collage, palette, texture and aspect ratio unchanged.
Use this image as the edit target, not a vague style reference.
```

## 输出尺寸要说实话

区分“要求的比例”“实际尺寸”和“严格像素规格”。原生生成可能给出
1672×941 这样的近似16:9文件，不能把它登记成1920×1080。用户只要常见
比例时可报告实际像素及取整差异；用户要求精确尺寸时必须满足后再声称完成。

每张成品都应查看，比例正确不能证明文字没漏或审美已通过。多比例交付时明确
列出各自路径与实际尺寸；不要把第一张的通过套给其余图片。
