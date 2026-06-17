---
description: TDD Enforcement - requires tests before implementation code
globs:
  - "**/*.ts"
  - "**/*.js"
  - "**/*.py"
  - "!**/*.test.ts"
  - "!**/*.spec.ts"
  - "!**/__tests__/**"
  - "!**/test/**"
  - "!**/tests/**"
---

# TDD Enforcement Rule (NON-NEGOTIABLE)

**NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.**

## Iron Law

```
RED → GREEN → REFACTOR (MANDATORY)
```

## Before Writing ANY Implementation Code

### Step 1: Check for Existing Test

```bash
# Find matching test file
find . -name "*.test.ts" -o -name "*.spec.ts" | grep -E "$(basename $FILE)"

# Or for Python
find . -name "test_*.py" | grep -E "$(basename $FILE)"
```

### Step 2: If No Test Exists → STOP and Write Test First

Create minimal test that captures the expected behavior:

```typescript
// For TypeScript/Bun
import { describe, it, expect } from "bun:test";

describe("FeatureName", () => {
  it("should do X when Y", () => {
    const result = functionUnderTest(input);
    expect(result).toBe(expectedOutput);
  });
});
```

```python
# For Python
import pytest

def test_feature_behavior():
    result = function_under_test(input)
    assert result == expected_output
```

### Step 3: Run Test - MUST FAIL

```bash
# TypeScript/Bun
bun test path/to/test.test.ts

# Python
pytest path/to/test.py::test_name -v
```

**Verify failure reason is expected** (e.g., "function not defined", "assertion failed")

**If test passes immediately → Test is wrong. Fix test.**

### Step 4: Write Minimal Implementation

Write simplest code to pass the test:
- No extra features
- No refactoring
- No "while I'm here" improvements

### Step 5: Run Test - MUST PASS

```bash
bun test path/to/test.test.ts
# or
pytest path/to/test.py::test_name -v
```

### Step 6: Run Full Test Suite - No Regressions

```bash
# TypeScript/Bun
bun test

# Python
pytest

# With coverage
pytest --cov=src --cov-report=term-missing
```

**If other tests fail → Fix regressions NOW**

### Step 7: Refactor (Optional)

Only after all tests pass:
- Remove duplication
- Improve names
- Keep tests green throughout

## Hard Rules

1. **NEVER write code before a failing test**
2. **NEVER skip watching the test fail**
3. **NEVER bundle multiple changes in one commit**
4. **NEVER commit without running full test suite**

## Red Flags - STOP and Delete Code

- Writing implementation before test
- Test passes on first run
- "I'll add tests later"
- "This is too simple to test"
- Multiple changes in one commit
- "Quick fix" without test

## Verification Checklist

Before marking task complete:

- [ ] Test exists and was written first
- [ ] Test failed with expected reason
- [ ] Minimal implementation written
- [ ] Test now passes
- [ ] Full test suite passes (no regressions)
- [ ] No debug code left
- [ ] Committed with `[tdd]` prefix

## Anti-Patterns to Reject

### Reject This:
```typescript
// Writing implementation first
export function calculate(x: number): number {
  return x * 2;
}

// Then adding test "later"
describe("calculate", () => {
  it("should double", () => {
    expect(calculate(5)).toBe(10);
  });
});
```

### Require This:
```typescript
// Test FIRST - watch it FAIL
describe("calculate", () => {
  it("should double", () => {
    expect(calculate(5)).toBe(10); // FAIL: "calculate is not defined"
  });
});

// Then minimal implementation
export function calculate(x: number): number {
  return x * 2; // Now test PASSES
}
```

## Integration with Workflows

**With Pre-Commit Verification:**
- TDD ensures code is tested
- Pre-commit ensures test passes

**With Three Strikes Rule:**
- If TDD is consistently violated → architectural problem
- Question why tests aren't being written first

## Metrics

| Metric | Target |
|--------|--------|
| Test coverage | >80% |
| Tests written first | 100% |
| Commits without tests | 0 |
| Regressions per change | <5% |
