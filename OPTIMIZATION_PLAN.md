# 🚀 OpenCode 防套娃 + 自动学习系统综合优化方案

## 📊 现状分析

### 已有系统

| 系统 | 功能 | 状态 | 仓库 |
|------|------|------|------|
| **防套娃规则** | TDD/Pre-commit/3-Strikes | ✅ 已部署 | ai-coding-rules |
| **自动学习** | 记忆提取/技能生成/知识图谱 | ✅ 已部署 | opencode-auto-learning |
| **Hermes** | 记忆存储/双向同步 | ✅ 运行中 | - |
| **oh-my-openagent** | 多代理协调 | ✅ 运行中 | - |

### 核心问题

```
┌─────────────────────────────────────────────────────────────┐
│ 当前状态：两套系统独立运行，缺乏深度集成                       │
│                                                              │
│ 问题 1: 防套娃规则不知道历史学习结果                          │
│ 问题 2: 学习系统不利用规则执行数据                            │
│ 问题 3: 没有从规则违反中自动学习                             │
│ 问题 4: 技能生成不考虑防套娃最佳实践                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 优化目标

### 一体化智能系统

```
用户操作
    ↓
防套娃规则检查 (TDD/Pre-commit/3-Strikes)
    ↓
自动学习系统 (记录执行/提取模式/生成技能)
    ↓
知识反馈 (主动推荐/技能建议/知识推送)
    ↓
用户获得智能辅助
```

---

## 💡 优化方案（分3个阶段）

## Phase 1: 规则-学习集成（高优先级）

### 1.1 规则执行自动记录

**目标**: 每次规则触发都自动记录到学习系统

**实现**:
```python
# src/learning/tracker/rule_tracker.py

class RuleTracker:
    """跟踪规则执行情况，自动记录到记忆系统"""
    
    def track_tdd(self, context: dict) -> None:
        """记录TDD执行情况"""
        memory = {
            "type": "pattern",
            "category": "tdd_compliance",
            "content": {
                "rule": "tdd-enforcement",
                "triggered": True,
                "test_written_first": context.get("test_first", False),
                "test_failed_first": context.get("test_failed", False),
                "regressions": context.get("regressions", 0),
                "project": context.get("project"),
                "timestamp": datetime.now().isoformat()
            },
            "tags": ["tdd", "testing", "regression"]
        }
        self.mem0.save(memory)
        
    def track_precommit(self, results: dict) -> None:
        """记录预提交检查结果"""
        memory = {
            "type": "pattern",
            "category": "precommit_compliance",
            "content": {
                "secrets_found": results.get("secrets", 0),
                "tests_passed": results.get("tests_passed", False),
                "lint_clean": results.get("lint_clean", False),
                "regressions": results.get("new_failures", 0)
            },
            "tags": ["security", "quality", "regression"]
        }
        self.mem0.save(memory)
        
    def track_three_strikes(self, attempt: int, failed: bool) -> None:
        """记录3次失败法则触发"""
        if attempt >= 3 and failed:
            memory = {
                "type": "learning",
                "category": "architecture_insight",
                "content": {
                    "rule": "three-strikes",
                    "attempts": attempt,
                    "pattern": "architectural_problem_detected",
                    "recommendation": "Consider refactoring architecture"
                },
                "tags": ["architecture", "refactoring", "design"]
            }
            self.mem0.save(memory)
            
            # 自动生成架构设计技能
            self.skill_generator.generate_architecture_skill(context)
```

**集成到规则系统**:
```markdown
# 在规则文件中添加跟踪指令

## Rule Execution Tracking

When this rule triggers:
1. Log to RuleTracker
2. Extract patterns
3. Generate skills if pattern repeats
```

### 1.2 规则违反自动学习

**目标**: 从违反规则的事件中学习，防止重复错误

**实现**:
```python
# src/learning/analyzer/violation_analyzer.py

class ViolationAnalyzer:
    """分析规则违反模式，自动学习"""
    
    def analyze_tdd_violation(self, violation: dict) -> dict:
        """分析TDD违反"""
        analysis = {
            "type": "tdd_violation",
            "pattern": self._identify_pattern(violation),
            "root_cause": self._analyze_root_cause(violation),
            "recommendation": self._generate_recommendation(violation)
        }
        
        # 保存到知识图谱
        self.kg.add_violation_node(analysis)
        
        return analysis
        
    def _identify_pattern(self, violation: dict) -> str:
        """识别违反模式"""
        patterns = {
            "implementation_before_test": "写代码前未写测试",
            "skipped_red_phase": "跳过看测试失败阶段",
            "bundle_changes": "一次修改多个功能",
            "no_regression_check": "未运行完整测试套件"
        }
        return patterns.get(violation.get("type"), "unknown")
        
    def _generate_recommendation(self, violation: dict) -> str:
        """生成改进建议"""
        return f"""
        ## TDD 最佳实践
        
        检测到违反: {violation.get('pattern')}
        
        ### 正确做法:
        1. 先写测试 - 确保测试失败
        2. 写最小代码 - 让测试通过
        3. 运行完整测试 - 确保无回归
        4. 重构代码 - 保持测试绿色
        
        ### 参考案例:
        {self._find_similar_cases(violation)}
        """
```

### 1.3 从3次失败自动生成架构洞察

**目标**: 自动识别架构问题并生成改进建议

**实现**:
```python
# src/learning/generator/architecture_insight_generator.py

class ArchitectureInsightGenerator:
    """从3次失败模式生成架构洞察"""
    
    def generate_insight(self, failure_series: list) -> dict:
        """生成架构洞察"""
        
        # 分析失败模式
        patterns = self._analyze_failure_patterns(failure_series)
        
        insight = {
            "type": "architecture_insight",
            "severity": self._calculate_severity(patterns),
            "patterns_detected": patterns,
            "recommendations": self._generate_recommendations(patterns),
            "refactoring_plan": self._create_refactoring_plan(patterns),
            "skills_to_learn": self._identify_skill_gaps(patterns)
        }
        
        return insight
        
    def _analyze_failure_patterns(self, failures: list) -> list:
        """分析失败模式"""
        patterns = []
        
        # 检测循环依赖
        if self._detect_circular_dependency(failures):
            patterns.append({
                "type": "circular_dependency",
                "description": "模块间循环依赖",
                "impact": "high",
                "solution": "引入接口层，打破循环"
            })
            
        # 检测状态共享
        if self._detect_shared_state(failures):
            patterns.append({
                "type": "shared_state",
                "description": "全局状态导致副作用",
                "impact": "high", 
                "solution": "使用纯函数，状态隔离"
            })
            
        # 检测紧耦合
        if self._detect_tight_coupling(failures):
            patterns.append({
                "type": "tight_coupling",
                "description": "模块间高度耦合",
                "impact": "medium",
                "solution": "依赖注入，接口抽象"
            })
            
        return patterns
```

---

## Phase 2: 主动智能推荐（高优先级）

### 2.1 基于规则的主动推荐

**目标**: 在用户操作前主动推送相关知识和规则

**实现**:
```python
# src/learning/recommender/rule_recommender.py

class RuleRecommender:
    """基于规则和上下文主动推荐"""
    
    def recommend_before_action(self, context: dict) -> list:
        """在操作前推荐"""
        recommendations = []
        
        # 基于文件类型推荐
        if context.get("file_type") == ".py":
            recommendations.extend(self._recommend_python_rules(context))
            
        # 基于操作类型推荐  
        if context.get("action") == "commit":
            recommendations.extend(self._recommend_precommit_checks(context))
            
        # 基于历史模式推荐
        similar = self.semantic_search.find_similar(context)
        recommendations.extend(self._recommend_from_history(similar))
        
        return recommendations
        
    def _recommend_python_rules(self, context: dict) -> list:
        """推荐Python相关规则"""
        return [
            {
                "type": "rule",
                "title": "Python TDD 检查",
                "content": "确保先写测试再写实现",
                "severity": "high",
                "auto_apply": False
            },
            {
                "type": "skill", 
                "title": "Python 测试最佳实践",
                "content": self._get_python_testing_skill(),
                "severity": "medium",
                "auto_apply": False
            }
        ]
        
    def _recommend_precommit_checks(self, context: dict) -> list:
        """推荐预提交检查"""
        return [
            {
                "type": "checklist",
                "title": "提交前检查清单",
                "items": [
                    "运行 pytest - 确保无回归",
                    "检查 hardcoded secrets",
                    "移除 debug print 语句",
                    "使用 [verified] 前缀"
                ],
                "auto_apply": True
            }
        ]
```

**UI集成**:
```markdown
┌─────────────────────────────────────────────────────────┐
│ 💡 智能推荐                                               │
├─────────────────────────────────────────────────────────┤
│ 检测到您正在编写 Python 代码...                           │
│                                                          │
│ 📋 建议操作:                                              │
│ 1. [高优先级] 先写测试 → 看失败 → 写代码 → 看通过         │
│ 2. [推荐] 查看技能: Python测试最佳实践                     │
│ 3. [参考] 类似项目使用 pytest + coverage                   │
│                                                          │
│ [应用建议] [查看详情] [忽略]                              │
└─────────────────────────────────────────────────────────┘
```

### 2.2 规则执行效果反馈

**目标**: 根据规则执行效果自动调整推荐

**实现**:
```python
# src/learning/feedback/rule_effectiveness_tracker.py

class RuleEffectivenessTracker:
    """跟踪规则执行效果，优化推荐"""
    
    def track_outcome(self, rule: str, outcome: dict) -> None:
        """跟踪规则执行结果"""
        
        effectiveness = {
            "rule": rule,
            "timestamp": datetime.now().isoformat(),
            "compliance_rate": self._calculate_compliance(rule),
            "bug_prevention": outcome.get("bugs_prevented", 0),
            "regression_rate": outcome.get("regressions", 0),
            "user_satisfaction": outcome.get("satisfaction", 0),
            "auto_apply_score": self._calculate_auto_apply_score(rule)
        }
        
        # 保存到知识图谱
        self.kg.add_effectiveness_node(effectiveness)
        
        # 如果规则效果好，提升推荐优先级
        if effectiveness["auto_apply_score"] > 0.8:
            self.recommender.boost_priority(rule)
            
    def _calculate_auto_apply_score(self, rule: str) -> float:
        """计算是否适合自动应用"""
        history = self.kg.get_rule_history(rule)
        
        if len(history) < 10:
            return 0.0  # 数据不足
            
        compliance_rate = sum(1 for h in history if h["complied"]) / len(history)
        bug_prevention = sum(h.get("bugs_prevented", 0) for h in history)
        false_positive = sum(h.get("false_positive", 0) for h in history)
        
        # 高合规率 + 防bug + 低误报 = 高分
        score = (compliance_rate * 0.4 + 
                min(bug_prevention / 10, 1) * 0.4 +
                (1 - min(false_positive / 10, 1)) * 0.2)
                
        return score
```

---

## Phase 3: 智能技能生成（中优先级）

### 3.1 从防套娃模式生成技能

**目标**: 自动从遵守规则的成功案例中生成技能

**实现**:
```python
# src/learning/generator/rule_based_skill_generator.py

class RuleBasedSkillGenerator:
    """基于规则遵守情况生成技能"""
    
    def generate_from_success(self, success_cases: list) -> dict:
        """从成功案例生成技能"""
        
        # 提取共同模式
        patterns = self._extract_patterns(success_cases)
        
        skill = {
            "name": f"tdd-success-pattern-{uuid4()[:8]}",
            "title": "TDD 成功模式",
            "category": "testing",
            "content": self._generate_skill_content(patterns),
            "triggers": self._identify_triggers(patterns),
            "applicability": self._calculate_applicability(patterns),
            "source": "auto-generated-from-success",
            "created_at": datetime.now().isoformat()
        }
        
        return skill
        
    def _generate_skill_content(self, patterns: list) -> str:
        """生成技能内容"""
        return f"""
        # TDD 成功模式
        
        ## 适用场景
        {self._describe_scenarios(patterns)}
        
        ## 执行步骤
        1. {patterns[0].get('step1', 'Write failing test')}
        2. {patterns[0].get('step2', 'Watch it fail')}
        3. {patterns[0].get('step3', 'Write minimal code')}
        4. {patterns[0].get('step4', 'Watch it pass')}
        
        ## 常见陷阱
        {self._extract_pitfalls(patterns)}
        
        ## 参考案例
        {self._list_reference_cases(patterns)}
        
        ## 验证检查清单
        - [ ] Test written first
        - [ ] Test failed first
        - [ ] Minimal implementation
        - [ ] All tests pass
        """
```

### 3.2 架构问题自动解决方案生成

**目标**: 从3次失败中自动生成架构解决方案

**实现**:
```python
# src/learning/generator/architecture_solution_generator.py

class ArchitectureSolutionGenerator:
    """从架构问题生成解决方案"""
    
    def generate_solution(self, problem: dict) -> dict:
        """生成架构解决方案"""
        
        problem_type = problem.get("type")
        
        if problem_type == "circular_dependency":
            return self._solve_circular_dependency(problem)
        elif problem_type == "shared_state":
            return self._solve_shared_state(problem)
        elif problem_type == "tight_coupling":
            return self._solve_tight_coupling(problem)
            
    def _solve_circular_dependency(self, problem: dict) -> dict:
        """解决循环依赖"""
        return {
            "problem": "Circular Dependency Detected",
            "analysis": problem.get("details"),
            "solution": {
                "approach": "Dependency Injection + Interface Segregation",
                "steps": [
                    "1. Identify the circular dependency chain",
                    "2. Extract interface for each module",
                    "3. Use dependency injection container",
                    "4. Break the cycle at the weakest link"
                ],
                "code_example": self._generate_di_example(),
                "refactoring_plan": self._create_refactoring_steps(problem),
                "tests": self._generate_test_plan(problem)
            },
            "skill_generated": self._create_di_skill(),
            "estimated_effort": "2-3 days"
        }
```

---

## 🔧 实施计划

### Week 1: Phase 1 - 基础集成

| 任务 | 时间 | 负责人 |
|------|------|--------|
| 实现 RuleTracker | 2天 | AI |
| 实现 ViolationAnalyzer | 2天 | AI |
| 集成到规则系统 | 2天 | AI |
| 测试和验证 | 1天 | AI |

### Week 2: Phase 2 - 主动推荐

| 任务 | 时间 | 负责人 |
|------|------|--------|
| 实现 RuleRecommender | 3天 | AI |
| 实现 EffectivenessTracker | 2天 | AI |
| UI集成 | 2天 | AI |

### Week 3: Phase 3 - 智能技能

| 任务 | 时间 | 负责人 |
|------|------|--------|
| 实现 RuleBasedSkillGenerator | 2天 | AI |
| 实现 ArchitectureSolutionGenerator | 2天 | AI |
| 集成和测试 | 2天 | AI |

---

## 📊 预期效果

### 量化指标

| 指标 | 当前 | 优化后 | 提升 |
|------|------|--------|------|
| 规则遵守率 | 60% | 90% | +50% |
| 技能生成质量 | 手动 | 自动 | 100% |
| 架构问题发现 | 被动 | 主动 | 主动 |
| 知识复用率 | 30% | 70% | +133% |
| 用户满意度 | - | - | 预期高 |

### 定性效果

- ✅ **预防为主**: 从被动修复到主动预防
- ✅ **自动进化**: 系统越用越智能
- ✅ **知识积累**: 每个错误都转化为学习
- ✅ **上下文感知**: 根据场景智能推荐
- ✅ **架构健康**: 自动识别和改进架构问题

---

## 🎁 额外优化建议

### 1. 可视化仪表板

创建 Web UI 展示：
- 规则遵守趋势
- 技能生成历史
- 架构健康度评分
- 知识图谱可视化

### 2. 团队协作功能

- 团队规则配置
- 共享技能库
- 集体记忆
- 代码审查集成

### 3. CI/CD 集成

- GitHub Actions 插件
- 预提交钩子
- 自动 PR 审查
- 代码质量报告

---

## 🏆 总结

这套优化方案将防套娃规则与自动学习系统深度集成，实现：

1. **智能规则**: 规则不再是死板的检查，而是学习的数据源
2. **主动防御**: 在问题发生前就给出建议
3. **自动进化**: 系统从每次交互中学习并改进
4. **知识沉淀**: 将个人经验转化为可复用的技能

**最终目标**: OpenCode 成为真正的智能编程伙伴，不仅执行命令，更主动帮助用户写出更好的代码。
