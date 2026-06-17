# oh-my-openagent 防套娃规则集

Anti-Regression Rules for oh-my-openagent

## 📋 规则清单

| 规则文件 | 适用场景 | 核心机制 |
|----------|----------|----------|
| `test-discipline.md` (已有) | 测试文件 | 测试纪律 |
| `tdd-enforcement.md` (新增) | 源代码文件 | TDD强制 |
| `pre-commit-verification.md` (新增) | 所有文件 | 预提交审查 |
| `three-strikes-rule.md` (新增) | 所有文件 | 3次失败法则 |

## 🎯 防套娃原理

### 三层防护体系

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 1: TDD Enforcement - 确保代码正确                    │
│  • 写测试 → 看失败 → 写代码 → 看通过                       │
│  • 防止: 无测试代码、症状修复                               │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Layer 2: Pre-Commit Verification - 确保不引入回归           │
│  • 自检清单 → 安全扫描 → 回归测试                          │
│  • 防止: 密钥泄露、调试代码、回归                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: Three Strikes Rule - 确保止损                     │
│  • 计数失败 → 3次STOP → 质疑架构                           │
│  • 防止: 无尽套娃、症状修复、架构问题                       │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 规则触发机制

规则使用 YAML frontmatter 定义触发条件：

```yaml
---
description: 规则描述
globs:
  - "**/*.ts"      # 匹配
  - "!**/test/**"  # 排除
---
```

### 触发条件

| 规则 | globs | 触发时机 |
|------|-------|----------|
| test-discipline | `**/*.test.ts`, `**/__tests__/**` | 编辑测试文件时 |
| tdd-enforcement | `**/*.ts`, `!**/*.test.ts` | 编辑非测试代码时 |
| pre-commit-verification | `**/*` | 所有文件操作时 |
| three-strikes-rule | `**/*` | 所有操作时 |

## 🚀 使用方式

### 1. 规则自动注入

oh-my-openagent 通过 `rules-injector` hook 自动读取 `.omo/rules/*.md`。

### 2. 验证规则加载

```bash
# 查看规则目录
ls -la .omo/rules/

# 应该看到:
# test-discipline.md (已有)
# tdd-enforcement.md (新增)
# pre-commit-verification.md (新增)
# three-strikes-rule.md (新增)
```

### 3. 重启 oh-my-openagent

规则更改后需要重启服务生效。

## 📊 效果对比

| 场景 | 无规则 | 有规则 |
|------|--------|--------|
| 修复Bug | 可能引入新Bug | 测试保护，回归检测 |
| 添加功能 | 范围可能失控 | TDD约束，最小化代码 |
| 多次修复失败 | 继续尝试第4、5次... | 第3次失败STOP，质疑架构 |
| 代码质量 | 依赖自觉 | 强制检查清单 |
| 回归风险 | 高 | 低（测试+审查） |

## ✅ 验证安装

```bash
# 1. 检查规则文件存在
ls -la .omo/rules/*.md

# 2. 检查文件内容
head -20 .omo/rules/tdd-enforcement.md

# 3. 重启 oh-my-openagent（如果需要）
# 规则应该自动生效
```

## 🎉 预期效果

启用这些规则后：
1. ✅ 每个代码修改都有测试保护
2. ✅ 每次提交都经过审查
3. ✅ 修复失败3次自动STOP
4. ✅ 大幅减少回归Bug
5. ✅ 代码质量显著提升
6. ✅ 告别"修复A破坏B"的套娃困境

## 🔄 与 OpenCode 规则同步

这些规则与 `~/.config/opencode/rules/` 中的规则保持一致，确保在 OpenCode 和 oh-my-openagent 中使用相同的防套娃策略。

## 📚 相关文档

- `AGENTS.md` - oh-my-openagent 架构文档
- `execution-discipline.md` - 执行纪律
- `.opencode/AGENTS.md` - OpenCode 集成文档

---

**规则版本**: 1.0.0
**创建时间**: 2026-06-17
**适用**: oh-my-openagent / OpenCode
