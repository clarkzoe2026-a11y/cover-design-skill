# 接手说明

这是 `editorial-cover` skill 的独立源项目。先读 `STATUS.md` 和 `skills/editorial-cover/SKILL.md`。

本轮目标：把文章/视频封面方法提炼为可复用skill，完成本机安装，并发布独立GitHub仓库。已存在的三张封面作为风格参考，不复制视频工程、个人网站或历史试稿。

修改后运行 `python3 scripts/check_package.py` 与 `python3 -m unittest discover -s tests -v`。流程变化需要重新演练真实任务；风格变化需要生成实际图片并交用户审核。

当前发布进度以 STATUS.md 为准，测试与提示词演练不代表人审通过。

## WorkBuddy 收尾交接（2026-11-13，供 Codex 审核）

- 本轮只改三份文档：`docs/validation.md`、`STATUS.md`、`HANDOFF.md`；未改 skill 包、示例图片、脚本与测试，未重复创建工程。
- 按事实补记：正向提示词演练由 Codex 完成 —— 蓝色知识库题材不照搬绿色房屋；严格 1920×1080 时如实报告 1672×941 缺口；只改两字锁住其余设计。**演练未调用图像生成、无新图、不是视觉验收**。独立只读审查未发现实质阻断。
- 校验摘要：`check_package.py` PASS（元数据 / 本地链接 / 可公开文本 / 示例像素与哈希）；`unittest discover -s tests -v` 5 项 OK；18 个必需文件齐备、frontmatter 合规、markdown 本地链接无错；Codex 安装软链与源包逐文件一致；15 个公开文本文件的隐私宽扫描无命中。
- 实际 Git：`main` 无提交、无 remote、全部文件未跟踪。提交身份已按用户给定值核对：`AI Hub <331626497+clarkzoe2026-a11y@users.noreply.github.com>`。按既定入口 `article-to-video/tools/identity_guard.py check` 复检：state PASS、exit 0，`manual_guard_installed` / `hooks_path_ok` / `use_config_only` 全为 true，repo-local `core.hooksPath` 指向既定 githooks，pre-commit / pre-push 可执行 —— **guard 已安装并通过，无需补装**。上一轮误用父级 `ai_hub/identity_guard.py` 得到 hooks false，属入口用错，已更正；未改父级 AI Hub 文件、未读认证文件。
- 发布计划：目标 `clarkzoe2026-a11y/editorial-cover-skill`，用户已授权；**本轮未 commit / push / create repo**，等 Codex 审核后明确指令，再以白名单身份执行首次提交与发布。
- 安装状态（Codex 审核确认）：`$HOME/.agents/skills/editorial-cover` 为源包软链且逐文件一致；`$HOME/.workbuddy/skills/editorial-cover` 为复制目录，SKILL.md 仅多一行 `agent_created: true`（工具元数据），去掉该行后正文逐行一致。**保留现装目录，不换软链、不改本机目录**。身份 guard 结论以 `article-to-video/tools/identity_guard.py check` 为准，父级其他 guard 的结果不用于判断本仓库 hooks 状态。
- 边界：未触碰原视频工程及无关脏改动，未调用额外付费服务。
