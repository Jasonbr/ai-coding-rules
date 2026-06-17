---
description: Pre-commit verification - security scan and regression testing
globs:
  - "**/*"
  - "!.git/**"
  - "!node_modules/**"
  - "!dist/**"
  - "!build/**"
  - "!.omo/evidence/**"
---

# Pre-Commit Verification Rule (NON-NEGOTIABLE)

**NO COMMIT WITHOUT VERIFICATION.**

## Iron Law

```
SELF_REVIEW + SECURITY_SCAN + REGRESSION_TEST + LINT_CHECK = [verified] COMMIT
```

## Verification Steps (MUST PASS ALL)

### Step 1: Self-Review Checklist

Before staging changes:

- [ ] **No hardcoded secrets** (API keys, passwords, tokens)
- [ ] **No debug print/console.log** left behind
- [ ] **No commented-out code** (delete or keep, don't comment)
- [ ] **Input validation** on user-provided data
- [ ] **Error handling** for external calls (try/catch)
- [ ] **Test exists** for the changed code
- [ ] **Test passes** locally

### Step 2: Static Security Scan

Run on staged changes:

```bash
# Hardcoded secrets (critical)
git diff --cached | grep "^+" | grep -iE "(api_key|secret|password|token|passwd)\s*=\s*['\"][^'\"]{6,}['\"]" && echo "❌ ERROR: Found potential secret"

# Shell injection
if git diff --cached | grep "^+" | grep -E "os\.system\(|subprocess.*shell=True"; then
  echo "⚠️  WARNING: Potential shell injection"
fi

# Dangerous eval/exec
if git diff --cached | grep "^+" | grep -E "\beval\(|\bexec\("; then
  echo "⚠️  WARNING: eval/exec found"
fi

# Unsafe deserialization
if git diff --cached | grep "^+" | grep -E "pickle\.loads?\("; then
  echo "⚠️  WARNING: pickle.loads found"
fi
```

**Any match in secrets = MUST FIX before commit**
**Warnings should be reviewed and addressed**

### Step 3: Regression Test

Run tests and compare with baseline:

```bash
# TypeScript/Bun
bun test 2>&1 | tail -20

# Python
python -m pytest --tb=no -q 2>&1 | tail -10

# With coverage
pytest --cov=src --cov-report=term-missing --tb=no 2>&1 | tail -10
```

**Rule: 0 new failures vs baseline**

**If tests were passing before, they must pass after**

### Step 4: Lint and Type Check

```bash
# TypeScript
if command -v tsc &> /dev/null; then
  tsc --noEmit 2>&1 | grep -E "^src.*error" | head -5
fi

if command -v eslint &> /dev/null; then
  eslint . --ext .ts,.tsx 2>&1 | grep -E "^\s*[0-9]+:\s*error" | head -5
fi

# Python
if command -v ruff &> /dev/null; then
  ruff check . 2>&1 | grep "^+" | head -5
fi

if command -v mypy &> /dev/null; then
  mypy . --ignore-missing-imports 2>&1 | grep "error:" | head -5
fi
```

**Fix lint errors before commit**

### Step 5: Commit with Verification

If all checks pass:

```bash
git add -A && git commit -m "[verified] <type>: <description>"
```

The `[verified]` prefix indicates code passed self-review and tests.

## Failure Handling

**If any check fails:**

1. **STOP commit immediately**
2. Fix the issue
3. Re-run ALL checks
4. Only then commit

**Never commit with:**
- "fix later"
- "TODO"
- "will add tests"
- "temp commit"

## Quick Reference

| Check | Command | Pass Criteria |
|-------|---------|---------------|
| Secrets | `git diff --cached \| grep -i secret` | No matches |
| Tests | `bun test` or `pytest` | 0 new failures |
| Lint | `eslint` or `ruff` | Clean |
| Type | `tsc --noEmit` or `mypy` | No errors |

## Common Patterns to Reject

### TypeScript
```typescript
// ❌ REJECT: Hardcoded secret
const API_KEY = "sk-abc123xyz";

// ✅ ACCEPT: Environment variable
const API_KEY = process.env.API_KEY;
if (!API_KEY) throw new Error("API_KEY not set");

// ❌ REJECT: Shell injection
import { exec } from "child_process";
exec(`ls ${userInput}`); // DANGEROUS

// ✅ ACCEPT: Safe array
import { spawn } from "child_process";
spawn("ls", [userInput], { check: true });

// ❌ REJECT: Debug code left
console.log("DEBUG: got here", result);

// ✅ ACCEPT: Remove or use proper logging
import { logger } from "./logger";
logger.debug("Processing result", { result });

// ❌ REJECT: Commented code
// const oldImplementation = () => { ... };

// ✅ ACCEPT: Delete or git history
```

### Python
```python
# ❌ REJECT: SQL injection
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# ✅ ACCEPT: Parameterized query
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# ❌ REJECT: Shell injection
os.system(f"ls {user_input}")

# ✅ ACCEPT: Safe subprocess
subprocess.run(["ls", user_input], check=True)

# ❌ REJECT: Pickle with user data
data = pickle.loads(user_input)

// ✅ ACCEPT: JSON or safe serialization
import json
data = json.loads(user_input)
```

## Hard Rules

1. **NEVER commit without running tests**
2. **NEVER commit with hardcoded secrets**
3. **NEVER commit with debug code**
4. **NEVER commit if any check fails**
5. **ALWAYS use `[verified]` prefix**

## Red Flags - STOP Commit

- ⛔ Tests failing
- ⛔ Secrets detected
- ⛔ Lint errors
- ⛔ Type errors
- ⛔ "Quick fix" without test
- ⛔ "Will add tests later"
- ⛔ Commented-out code
- ⛔ Debug print statements
- ⛔ Merge conflicts markers

## Integration with Workflows

**With TDD Enforcement:**
- TDD ensures tests exist
- Pre-commit ensures tests pass

**With Three Strikes Rule:**
- If commits consistently fail checks
- Question the development process

## CI/CD Alignment

Local verification should match CI:
- CI runs same tests → you run same tests
- CI runs lint → you run lint
- CI checks secrets → you check secrets

**Goal: No surprises in CI**

## Metrics

| Metric | Target |
|--------|--------|
| Commits with `[verified]` | 100% |
| CI failures due to local skip | 0 |
| Secrets committed | 0 |
| Debug code in production | 0 |
