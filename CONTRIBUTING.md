# Contributing to AI Coding Rules

感谢您对 AI Coding Rules 项目的关注！我们欢迎各种形式的贡献。

## 🎯 贡献类型

### 1. 规则改进

- 完善现有规则的描述
- 添加更多示例
- 修复规则中的错误

### 2. 新平台支持

- Claude Code 规则
- Codex CLI 规则
- Cursor 规则
- 其他 AI 编程工具

### 3. 新规则开发

- 针对特定问题的规则
- 针对特定语言的规则
- 针对特定框架的规则

### 4. 文档改进

- 修正拼写和语法错误
- 添加更多使用示例
- 改进安装说明
- 翻译为其他语言

### 5. Bug 修复

- 修复安装脚本问题
- 修复规则逻辑错误

## 📋 贡献流程

### 1. Fork 和克隆

```bash
# Fork 仓库后克隆
git clone https://github.com/YOUR_USERNAME/ai-coding-rules.git
cd ai-coding-rules
```

### 2. 创建分支

```bash
# 创建特性分支
git checkout -b feature/your-feature-name

# 或者修复分支
git checkout -b fix/issue-description
```

### 3. 开发和测试

#### 规则开发检查清单

- [ ] 规则内容清晰、完整
- [ ] 包含具体示例（好/坏对比）
- [ ] 包含验证步骤
- [ ] 格式符合平台要求（OpenCode vs oh-my-openagent）
- [ ] 无拼写和语法错误

#### 安装脚本修改

- [ ] 测试安装脚本
- [ ] 确保备份机制工作
- [ ] 验证安装后状态

#### 文档更新

- [ ] 更新 README.md
- [ ] 更新 CHANGELOG.md
- [ ] 如有必要，更新 ANALYSIS.md

### 4. 提交更改

```bash
# 添加更改
git add .

# 提交（使用 [verified] 前缀）
git commit -m "[verified] type: description"

# 提交类型：
# - feat: 新规则或功能
# - fix: 规则修复
# - docs: 文档更新
# - refactor: 代码重构
# - test: 测试相关
# - chore: 其他
```

### 5. 推送和创建 PR

```bash
# 推送到你的 Fork
git push origin feature/your-feature-name

# 然后到 GitHub 创建 Pull Request
```

### 6. PR 审查

PR 会经过以下审查：

1. **内容审查** - 规则是否合理、有用
2. **格式审查** - 是否符合平台格式要求
3. **拼写审查** - 基本语法和拼写检查

## 📝 规则编写指南

### OpenCode 规则格式

```markdown
# Rule Title

> Injected on [when]

## Core Principle

```
Iron Law: NO XXX WITHOUT YYY
```

## Section 1: Title

**Before doing X:**

1. Step 1
2. Step 2
3. Step 3

### Subsection

Content...

## Hard Rules

1. **NEVER** do this
2. **ALWAYS** do that

## Red Flags

- ⛔ Danger sign
- ⚠️ Warning sign

## Verification

- [ ] Check item 1
- [ ] Check item 2
```

### oh-my-openagent 规则格式

```markdown
---
description: Short description of the rule
globs:
  - "**/*.ts"      # Match
  - "!**/test/**"  # Exclude
---

# Rule Title

Same content as OpenCode...
```

## 🎨 风格指南

### 写作风格

- 使用简洁、清晰的语言
- 使用命令式语气（"Write test first"）
- 使用 emoji 标记重要点
- 提供具体代码示例

### Markdown 格式

- 使用 ATX 标题（`#`）
- 使用 fenced code blocks（```）
- 使用表格展示对比
- 使用列表展示步骤

### 代码示例

- 提供完整、可运行的代码
- 包含好/坏对比
- 使用注释解释关键点

## 🧪 测试规则

### 本地测试

```bash
# 测试安装脚本
./install.sh verify

# 测试 OpenCode 规则
ls -la ~/.config/opencode/rules/

# 测试 oh-my-openagent 规则
ls -la .omo/rules/
```

### 实际测试

- 在 OpenCode 中触发规则
- 在 oh-my-openagent 中触发规则
- 验证规则是否按预期工作

## 📞 联系方式

- **GitHub Issues**: 报告 Bug 或请求功能
- **GitHub Discussions**: 一般讨论
- **Email**: songxibo@gmail.com

## 🏆 贡献者

感谢所有贡献者！

<!-- 贡献者列表将由 GitHub Actions 自动生成 -->

## 📄 许可证

通过贡献，您同意您的贡献将在 MIT 许可证下发布。

---

**Happy Contributing!** 🎉
