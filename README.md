# 封面设计（cover-design）

把文章意思画出来，让标题先被读到。

一套用于文章、视频封面的 Codex / Agent skill：浅色纸面、深色字、概念版画拼贴，支持品牌主色适配、文字定点编辑，以及 **4:3、3:4、16:9** 重新构图。

![浅绿版画拼贴封面示例](skills/cover-design/assets/reference-4x3.png)

## 这套方法做什么

先明确读者要记住的词，再为内容选择可理解的动作隐喻。字体、字距、换行与留白先确定，插画为标题服务。它不是个人网站截图模板，也不是用同一套科技道具给不同标题换字。

主色、标题、标签和内容都可以替换。示例的 `#DDFB78` 是其中一套品牌配色，不会强制应用到所有任务。

## 安装

克隆后将 skill 文件夹复制到 Codex 的技能目录；已有同名 skill 时先检查，不直接覆盖。

```bash
git clone https://github.com/clarkzoe2026-a11y/cover-design-skill.git
cd cover-design-skill
mkdir -p "$HOME/.agents/skills"
cp -R skills/cover-design "$HOME/.agents/skills/cover-design"
```

新开会话后调用 `$cover-design`。其他兼容 `SKILL.md` 的 Agent，可把该文件夹放入其技能目录。 skill 本身不调用付费 API；实际生成需要运行环境提供图像生成/编辑能力。没有工具时会报告限制，不把占位图当成品。

## 用法

```text
使用 $cover-design，给“把散落笔记变成可复用知识库”制作封面。
标签：AI知识管理
副标题：收集 · 整理 · 调用
主色：#DDFB78
比例：3:4
突出标题，使用浅纸版画拼贴，插画不要盖住文字。
```

也可以继续说“改为16:9”“只把调用改成复用”“换成我的蓝色品牌”，skill 会区分比例重排与局部编辑。

## 内容

- [SKILL.md](skills/cover-design/SKILL.md)：核心决策与工作方式。
- [配色、提示词与具体例子](skills/cover-design/references/design-and-prompts.md)。
- [比例与定点编辑](skills/cover-design/references/ratios-and-edits.md)。
- [三比例示例清单](examples/manifest.json)：图片的实际尺寸、哈希与来源说明。
- [行为验证记录](docs/validation.md)：结构校验与独立提示词演练的范围。

## 示例说明

示例为 AI 生成的同系列封面，包含建站教程的示例文字；没有个人网站截图、真实域名或备案号。它们用于理解画法与字图关系，不限制新主题的图像主体。16:9 示例原生尺寸存在像素取整差异，清单保留真实值。

不提供网页部署、API 代理或后台服务。下载项目不需要配置 Key；使用者的图像工具与额度由其所在环境管理。

## 本地检查

```bash
python3 scripts/check_package.py
```

检查文件链接、示例实际尺寸与哈希、可公开内容；不证明成品的文字准确或审美已通过。发布前仍应人工查看图片。见 [MIT License](LICENSE)。
