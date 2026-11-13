# 接手说明

这是 `cover-design`（UI「封面设计」）skill 的独立源项目，公开仓库 `https://github.com/clarkzoe2026-a11y/cover-design-skill`。先读 `STATUS.md` 与 `skills/cover-design/SKILL.md`。本机项目根目录沿用 `editorial-cover-skill`，不为外观重命名，文档不公开本机绝对路径。

修改后运行 `python3 scripts/check_package.py`、`python3 -m unittest discover -s tests -v` 与官方 skill-creator `quick_validate.py`。流程变化做文本层演练；风格变化需要生成实际图片并交用户审核。文件检查与提示词演练都不等于视觉验收，没有用户确认不写「已验收」。

## 历史（简表，仅为语境，SHA 不改写）

| 提交 | 内容 |
| --- | --- |
| `c8b287c…` | 首次发布（当时技能名与仓库名为 `editorial-cover`） |
| `418fe11…` | 发布状态回写 |
| `9ff6ed3…` | 改名 `cover-design` / `cover-design-skill`，原地 rename 保留 PUBLIC、历史与旧 URL 重定向 |
| 本轮提交 | 小白向改进 + 三处小修（SHA 以 git / 远程 `main` 为准） |

提交身份 `AI Hub <331626497+clarkzoe2026-a11y@users.noreply.github.com>`；guard 以 `article-to-video/tools/identity_guard.py check` 为准（PASS、hooks 已装）；所有提交与 push 均未用 `--no-verify`。当前状态以 `STATUS.md` 为准。

## 本轮交接（2026-11-13，已完成并发布）

- 小白向改进：一句话或仅标题即可生成；标签/副标题可省略，配色/风格/比例按默认决策自动补齐；默认一张 4:3 与自然话比例映射；四套现成配色；换色 / 只改字的锁定规则；保留版画拼贴质量与真实尺寸 / 视觉检查。
- 三处小修：明确标签/副标题可省略、配色/风格/比例自动补齐；配色轮换限定为可见上下文中的独立新任务、同主题默认保留配色；`docs/validation.md` 的 B 补虚拟测试摘要与零参数请求的实际决策（提炼标题、预设、简短插画提示词）。
- 改动：`SKILL.md`、`design-and-prompts.md`、`ratios-and-edits.md`、`agents/openai.yaml`、`README.md`、`STATUS.md`、`HANDOFF.md`、`docs/validation.md`；WorkBuddy 安装已同步（保留 `agent_created: true`，同步前按小修前基线复核无未知改动），Codex 软链自动一致。
- 校验与三种请求（仅标题 / 已有文章零参数 / 同主题三比例 + 换色 + 仅改两字）的文本层演练实际结果见 `docs/validation.md`；未调用图像 API、未生成新图、未做视觉验收、未新增程序或界面。
- 已由既定身份正常 commit / push（hooks 生效）；最终 HEAD 的 CI、远程 SHA 一致与 clean 状态在发布后核对，结果见对话审核报告。仓库名与中文 About 保持不变。
