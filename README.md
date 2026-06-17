# AI Coding Rules

AI 编程防套娃规则集 - 防止"修复一个问题却引入新问题"的经典困境

## 🎯 项目目标

为 OpenCode、oh-my-openagent 等 AI 编程助手提供一套防回归规则，确保：
- ✅ 代码修改有测试保护
- ✅ 提交前经过质量检查
- ✅ 修复失败时及时止损

## 📁 目录结构

```
ai-coding-rules/
├── opencode-rules/           # OpenCode 规则
│   ├── tdd-enforcement.md
│   ├── pre-commit-verification.md
│   ├── three-strikes-rule.md
│   ├── README.md
│   ├── ANALYSIS.md
│   └── PLATFORM_COMPARISON.md
├── oh-my-openagent-rules/    # oh-my-openagent 规则
│   ├── tdd-enforcement.md
│   ├── pre-commit-verification.md
│   ├── three-strikes-rule.md
│   └── README.md
├── docs/                     # 文档
│   └── (预留)
├── install.sh                # 安装脚本
├── README.md                 # 本文件
└── LICENSE                   # MIT 许可证
```

## 🚀 快速开始

### 安装到 OpenCode

```bash
# 克隆仓库
git clone https://github.com/Jasonbr/ai-coding-rules.git

# 安装规则
cd ai-coding-rules
./install.sh opencode
```

### 安装到 oh-my-openagent

```bash
# 在项目目录下
./install.sh oh-my-openagent ~/workspace/oh-my-openagent
```

## 📋 规则说明

### 三层防护体系

| 层 | 规则 | 作用 | 防止问题 |
|----|------|------|----------|
| Layer 1 | TDD Enforcement | 测试驱动开发 | 无测试代码、症状修复 |
| Layer 2 | Pre-Commit Verification | 预提交审查 | 密钥泄露、回归、调试代码 |
| Layer 3 | Three Strikes Rule | 3次失败法则 | 无尽套娃、架构问题 |

## 📊 预期效果

| 指标 | 改善 |
|------|------|
| Bug 回归率 | -83% (30% → 5%) |
| 测试覆盖率 | +100% (40% → 80%) |
| 修复成功率 | +50% (60% → 90%) |
| 套娃困境频率 | -90% |

## 🔧 平台支持

| 平台 | 状态 | 位置 |
|------|------|------|
| OpenCode | ✅ 已配置 | `~/.config/opencode/rules/` |
| oh-my-openagent | ✅ 已配置 | `.omo/rules/` |
| Claude Code | 📝 计划中 | - |
| Codex | 📝 计划中 | - |

## 📖 文档

- [OpenCode 规则说明](./opencode-rules/README.md)
- [oh-my-openagent 规则说明](./oh-my-openagent-rules/README.md)
- [方案分析](./opencode-rules/ANALYSIS.md)
- [平台对比](./opencode-rules/PLATFORM_COMPARISON.md)

## 🤝 贡献

欢迎提交 PR 和 Issue！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m '[verified] Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- 基于 Hermes Agent 的 `systematic-debugging`、`test-driven-development`、`requesting-code-review` 技能
- 参考 obra/superpowers 的代码审查实践
- 感谢 OpenCode 和 oh-my-openagent 社区

## 📞 联系

- GitHub: [@Jasonbr](https://github.com/Jasonbr)
- 邮箱: songxibo@gmail.com

---

**防止套娃，从规则开始！** 🛡️
