# 接手说明

这是 `cover-design`（UI 名称「封面设计」）skill 的独立源项目。先读 `STATUS.md` 和 `skills/cover-design/SKILL.md`。本机项目根目录沿用 `editorial-cover-skill`，按约定不为外观重命名。

初始目标（已完成）：把文章/视频封面方法提炼为可复用skill，完成本机安装，并发布独立GitHub仓库。已存在的三张封面作为风格参考，不复制视频工程、个人网站或历史试稿。

修改后运行 `python3 scripts/check_package.py` 与 `python3 -m unittest discover -s tests -v`。流程变化需要重新演练真实任务；风格变化需要生成实际图片并交用户审核。

当前状态以 STATUS.md 及文末「命名定案与发布交接」为准，测试与提示词演练不代表人审通过。

## WorkBuddy 收尾交接（2026-11-13，命名定案前的历史快照）

> 本节全部为当时（仓库名 `editorial-cover-skill`、技能名 `editorial-cover`）的状态记录，保留原始 SHA 与 URL 作为历史语境；其中的安装结论已被后续命名迁移覆盖，不代表当前状态。

- 本轮只改三份文档：`docs/validation.md`、`STATUS.md`、`HANDOFF.md`；未改 skill 包、示例图片、脚本与测试，未重复创建工程。
- 按事实补记：正向提示词演练由 Codex 完成 —— 蓝色知识库题材不照搬绿色房屋；严格 1920×1080 时如实报告 1672×941 缺口；只改两字锁住其余设计。**演练未调用图像生成、无新图、不是视觉验收**。独立只读审查未发现实质阻断。
- 校验摘要：`check_package.py` PASS（元数据 / 本地链接 / 可公开文本 / 示例像素与哈希）；`unittest discover -s tests -v` 5 项 OK；18 个必需文件齐备、frontmatter 合规、markdown 本地链接无错；Codex 安装软链与源包逐文件一致；15 个公开文本文件的隐私宽扫描无命中。
- 实际 Git：`main` 无提交、无 remote、全部文件未跟踪。提交身份已按用户给定值核对：`AI Hub <331626497+clarkzoe2026-a11y@users.noreply.github.com>`。按既定入口 `article-to-video/tools/identity_guard.py check` 复检：state PASS、exit 0，`manual_guard_installed` / `hooks_path_ok` / `use_config_only` 全为 true，repo-local `core.hooksPath` 指向既定 githooks，pre-commit / pre-push 可执行 —— **guard 已安装并通过，无需补装**。上一轮误用父级 `ai_hub/identity_guard.py` 得到 hooks false，属入口用错，已更正；未改父级 AI Hub 文件、未读认证文件。
- **发布已完成（2026-11-13）**：Codex 审核通过后，WorkBuddy 核对待提交清单（18 个文件）与 `git diff --check` / `--cached --check`（均 0），以既定白名单身份首次提交 `c8b287c…` 并 push 到当时的公开仓库 `https://github.com/clarkzoe2026-a11y/editorial-cover-skill`（PUBLIC / main / 非空）。远程 SHA 与本地一致；Actions `Check skill package` ✓；README、SKILL.md、references、manifest 与示例图公开可读。身份 guard 以 `article-to-video/tools/identity_guard.py` 为准（PASS、hooks 已装），提交与 push 均未用 `--no-verify`。本文件所在提交为发布状态回写提交，最终 HEAD SHA 以 git 与远程 `main` 为准。
- 安装状态（当时 Codex 审核确认）：`$HOME/.agents/skills/editorial-cover` 为源包软链且逐文件一致；`$HOME/.workbuddy/skills/editorial-cover` 为复制目录，SKILL.md 仅多一行 `agent_created: true`（工具元数据），去掉该行后正文逐行一致。**保留现装目录，不换软链、不改本机目录**（本条为当时结论，已被后续命名迁移覆盖）。身份 guard 结论以 `article-to-video/tools/identity_guard.py check` 为准，父级其他 guard 的结果不用于判断本仓库 hooks 状态。
- 边界：未触碰原视频工程及无关脏改动，未调用额外付费服务。

## 命名定案与发布交接（2026-11-13，已完成）

- 用户定案：技能名 / 目录 `cover-design`，UI `display_name`「封面设计」，`default_prompt` 明确引用 `$cover-design`，仓库定案名 `cover-design-skill`；原技能能力与风格正文、参考文档、示例图均保持不变。
- 本次提交包含：技能目录与 SKILL.md frontmatter、`agents/openai.yaml`、README 安装链接与用法、AGENTS.md、STATUS.md、HANDOFF.md、docs/validation.md、examples/manifest.json、scripts/check_package.py、tests/test_package.py。本机项目根目录仍为 `editorial-cover-skill`，文档未公开本机绝对路径；历史 SHA 不变。
- 本机安装实际状态：`$HOME/.agents/skills/cover-design` 为软链，指向本仓库 `skills/cover-design/`，旧名软链已移除、无悬空；`$HOME/.workbuddy/skills/cover-design` 由旧目录原地迁移，迁移前逐行核对唯一差异为 `agent_created: true`，该元数据保留，其余正文与新源包逐行一致。迁移前两个目标新目录均不存在，未覆盖任何未知目录；两个技能目录现均无旧名入口。
- 校验：包检查 PASS、原 5 项单测 OK、`quick_validate.py` → `Skill is valid!`、结构校验 18 个文件齐备、旧活动引用 rg 扫描仅剩有意保留的历史记录、`git diff --check` 系列 exit 0。Codex 审核时独立复跑包检查 PASS、单测 5/5、官方 skill-creator `quick_validate` 输出 `Skill is valid`、`git diff HEAD --check` 无错，并核对新软链有效、两个旧安装入口不存在、WorkBuddy 安装除元数据外逐文件一致、About 中文回读一致。本轮未重新生成图片、未做图像演练。
- **发布阶段已完成**：确认目标仓库名无冲突 → `gh repo rename cover-design-skill` 原地改名（保留 PUBLIC、两个历史提交与旧 URL 重定向，未新建仓库、未覆盖历史）→ 更新本地 origin → README 中的新仓库地址生效 → 以既定 `AI Hub` noreply 白名单身份正常提交（hooks 生效、未 bypass `--no-verify`）并 push `main`。
- 发布后核对：新仓库 URL、中文 description、技能文件公开可读、本地/远程 HEAD 一致、clean、最终 HEAD 的 GitHub Actions success；结果见本对话最终报告，最终 HEAD SHA 以 git 与远程 `main` 为准。
