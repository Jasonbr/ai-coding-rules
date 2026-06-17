# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-17

### Added

- Initial release of AI Coding Rules
- Three-layer anti-regression protection system

#### Rules

- **TDD Enforcement** (`tdd-enforcement.md`)
  - RED-GREEN-REFACTOR cycle enforcement
  - Test-first development requirement
  - Regression test requirements
  - Support for Python, TypeScript, and JavaScript

- **Pre-Commit Verification** (`pre-commit-verification.md`)
  - Self-review checklist
  - Static security scanning (secrets, injection, eval)
  - Regression test comparison
  - Lint and type checking
  - `[verified]` commit prefix requirement

- **Three Strikes Rule** (`three-strikes-rule.md`)
  - Failed fix counting
  - Architecture problem detection
  - Stop-and-escalate mechanism
  - Anti-whack-a-mole protection

#### Platform Support

- **OpenCode** rules (pure Markdown, global)
  - Location: `~/.config/opencode/rules/`
  - Trigger: `rules-injector` hook
  - Format: Standard Markdown

- **oh-my-openagent** rules (YAML frontmatter + globs)
  - Location: `.omo/rules/`
  - Trigger: File pattern matching
  - Format: YAML frontmatter + Markdown

#### Documentation

- Comprehensive README with usage instructions
- Analysis document comparing 5 anti-regression schemes
- Platform comparison guide
- Installation script with backup support
- MIT License

#### Installation

- Bash installation script (`install.sh`)
- Backup existing rules before installation
- Verification after installation
- Support for custom paths

### Expected Impact

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Bug regression rate | ~30% | <5% | -83% |
| Test coverage | ~40% | >80% | +100% |
| Fix success rate | ~60% | >90% | +50% |
| Whack-a-mole frequency | High | Very Low | -90% |

### Based On

- Hermes Agent `systematic-debugging` skill
- Hermes Agent `test-driven-development` skill
- Hermes Agent `requesting-code-review` skill
- obra/superpowers code review practices

## [Unreleased]

### Planned

- [ ] Claude Code support
- [ ] Codex CLI support
- [ ] CI/CD integration examples
- [ ] Pre-commit hook integration
- [ ] Custom rule creation guide
- [ ] Rule effectiveness metrics
- [ ] Multi-language support (Go, Rust, etc.)

---

**Legend:**
- `[verified]` = Passed pre-commit verification
- `feat:` = New feature
- `fix:` = Bug fix
- `docs:` = Documentation only changes
- `refactor:` = Code refactoring
