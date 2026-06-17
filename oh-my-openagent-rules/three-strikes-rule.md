---
description: Three strikes rule - stop after 3 failed fix attempts
globs:
  - "**/*"
---

# Three Strikes Rule (Anti-Whack-a-Mole)

**3 FAILURES = ARCHITECTURE PROBLEM, NOT A BUG**

## Core Principle

```
SYMPTOM FIXING = ENDLESS REGRESSION
ARCHITECTURE FIXING = PERMANENT SOLUTION
```

## The Rule

| Attempt | Result | Action |
|---------|--------|--------|
| 1st | Fix fails | Return to Phase 1, re-investigate with new info |
| 2nd | Fix fails | Deep analysis, question assumptions |
| 3rd | Fix fails | **STOP** - Question the architecture |

## Pattern Recognition

### Signs of Architectural Problem

✅ **Each fix reveals new shared state/coupling elsewhere**
- Fix A in module X → breaks module Y
- Fix B in module Y → breaks module Z  
- Fix C in module Z → breaks module X (cycle!)

✅ **Fixes require "massive refactoring"**
- "I need to refactor the whole module"
- "This touches 10 files"
- "Need to change the data model"

✅ **Each fix creates new symptoms in different places**
- Original: Bug in feature A
- Fix 1: Fixed A, broke B
- Fix 2: Fixed B, broke C
- Fix 3: Fixed C, broke A again (full circle)

✅ **"Just one more fix" feeling**
- "This should be the last one"
- "Almost there..."
- Feeling of chasing shadows

**These indicate wrong architecture, not wrong fixes.**

## Phase 1: First Failure

**After first fix attempt fails:**

### STOP - Do NOT attempt Fix #2 immediately

### Actions:
1. **Document the failure**
   - What was attempted
   - Why it failed
   - New information learned

2. **Return to systematic debugging**
   - Re-read error messages carefully
   - Re-reproduce the issue
   - Check recent changes
   - Trace data flow more deeply
   - Look for hidden dependencies

3. **Form new hypothesis**
   - Don't assume first diagnosis was correct
   - Consider alternative root causes
   - Check if symptom ≠ root cause

4. **Try different approach**
   - Don't retry same fix with tweaks
   - Try fundamentally different solution

## Phase 2: Second Failure

**After second fix attempt fails:**

### STOP - Deep analysis required

### Actions:
1. **Question all assumptions**
   - Is the diagnosis actually correct?
   - Is the fix addressing root cause or symptom?
   - Are there hidden dependencies?
   - Is the pattern fundamentally sound?

2. **Read reference implementation**
   - Find similar working code
   - Compare patterns
   - List all differences

3. **Check for systemic issues**
   - State management problems
   - Race conditions
   - Memory leaks
   - Circular dependencies

4. **Try fundamentally different approach**
   - Don't iterate on failed strategies
   - Consider rewriting from scratch
   - Look for higher-level solution

## Phase 3: Third Failure - THE STOP POINT

**After third fix attempt fails:**

```markdown
🛑 ARCHITECTURAL PROBLEM DETECTED

Pattern indicates fundamental architecture issue:
- Each fix reveals new coupling elsewhere
- Fixes require massive refactoring
- Symptoms keep moving to new places
- "Whack-a-mole" pattern detected

OPTIONS:
1. REFACTOR ARCHITECTURE
2. CHANGE APPROACH
3. ESCALATE TO HUMAN
4. ABANDON CURRENT DIRECTION

This is NOT a failed hypothesis — this is wrong architecture.
Stop fixing symptoms. Address the root pattern.
```

## Hard Rules

1. **Count failures explicitly** (don't guess)
2. **Never attempt Fix #4** without questioning architecture
3. **3 failures = STOP**, not "try harder"
4. **Document failures** and patterns
5. **Escalate architectural problems** to human

## Red Flags - STOP and Question Architecture

- ⛔ "Just one more fix"
- ⛔ "This should work..."
- ⛔ "Why is this breaking NOW?"
- ⛔ Each fix creates 2 new problems
- ⛔ Symptoms keep moving around
- ⛔ Feeling of chasing shadows
- ⛔ Code becoming more complex
- ⛔ Technical debt increasing
- ⛔ Tests becoming harder to write

**All of these mean: STOP. Question the architecture.**
