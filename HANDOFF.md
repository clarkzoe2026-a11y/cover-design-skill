# 接手说明

先读 [当前状态](STATUS.md)，再读 [技能正文](skills/cover-design/SKILL.md)。比例与编辑读 `references/ratios-and-edits.md`，配色与完整提示词读 `references/design-and-prompts.md`。只维护本仓库的源包；安装副本从源同步，不独立演进。

修改后运行：

```bash
python3 scripts/check_package.py
python3 -m unittest discover -s tests -v
```

再用官方 skill-creator 的 `quick_validate.py` 检查 `skills/cover-design`；该工具需要 PyYAML，可使用已有具备该依赖的 Python 环境，不修改验证器绕过失败。提交前运行 `git diff --check`。流程变化要演练内容入口、默认比例与编辑决策；风格变化要查看实际图片并交用户审核。文件校验不等于视觉通过。

发布保留既定提交身份与身份防护 hooks，不使用 `--no-verify` 或强推。当前规则、验证范围与用户确认见 [验证记录](docs/validation.md)，提交与远端一致性在发布后核对，不预写成功。

内部执行器会话目录不入包；用户候选与私有正文不复制到公开仓库。三比例历史图片仅是画法参考，不能当作当前字体与配色标准。后续批量封面须逐篇读取内容、另存候选、逐版记录确认，不能把一张通过套到整批，更不能据此替换或发布网站。

[整理前交接记录](docs/archive/2026-11-14-before-consolidation/HANDOFF.md)保留历史过程，当前执行以本页和 STATUS 为准。
