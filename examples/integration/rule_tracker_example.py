#!/usr/bin/env python3
"""
示例：规则-学习系统集成
展示如何将防套娃规则与自动学习系统结合
"""

from datetime import datetime
from typing import Dict, List, Optional
import json

class RuleTracker:
    """
    跟踪规则执行情况，自动记录到学习系统
    集成 Mem0 记忆系统和知识图谱
    """
    
    def __init__(self, mem0_client=None, kg_client=None):
        self.mem0 = mem0_client
        self.kg = kg_client
        
    def track_tdd_execution(self, context: Dict) -> Dict:
        """
        记录TDD执行情况
        
        Args:
            context: {
                "project": "project_name",
                "file": "path/to/file.py",
                "test_written_first": True/False,
                "test_failed_first": True/False,
                "implementation_minimal": True/False,
                "all_tests_pass": True/False,
                "regressions": 0
            }
        """
        memory = {
            "type": "pattern",
            "category": "tdd_compliance",
            "content": {
                "rule": "tdd-enforcement",
                "project": context.get("project"),
                "file": context.get("file"),
                "compliance": {
                    "test_written_first": context.get("test_written_first", False),
                    "test_failed_first": context.get("test_failed_first", False),
                    "implementation_minimal": context.get("implementation_minimal", False),
                    "all_tests_pass": context.get("all_tests_pass", False)
                },
                "regressions": context.get("regressions", 0),
                "timestamp": datetime.now().isoformat()
            },
            "tags": ["tdd", "testing", "regression"],
            "timestamp": datetime.now().isoformat()
        }
        
        # 保存到Mem0
        if self.mem0:
            self.mem0.save(memory)
            
        # 分析模式并更新知识图谱
        if self.kg:
            self._update_kg_with_tdd_pattern(memory)
            
        return memory
        
    def track_precommit_checks(self, results: Dict) -> Dict:
        """
        记录预提交检查结果
        
        Args:
            results: {
                "secrets_found": 0,
                "tests_passed": True,
                "lint_clean": True,
                "new_failures": 0
            }
        """
        memory = {
            "type": "pattern",
            "category": "precommit_compliance",
            "content": {
                "rule": "pre-commit-verification",
                "security": {
                    "secrets_found": results.get("secrets_found", 0),
                    "security_issues": results.get("security_issues", [])
                },
                "quality": {
                    "tests_passed": results.get("tests_passed", False),
                    "lint_clean": results.get("lint_clean", False),
                    "new_failures": results.get("new_failures", 0)
                },
                "timestamp": datetime.now().isoformat()
            },
            "tags": ["security", "quality", "regression"]
        }
        
        if self.mem0:
            self.mem0.save(memory)
            
        return memory
        
    def track_three_strikes(self, failure: Dict) -> Optional[Dict]:
        """
        记录3次失败法则触发
        
        Args:
            failure: {
                "attempt": 3,
                "fix_description": "...",
                "error_message": "...",
                "project": "..."
            }
        """
        if failure.get("attempt", 0) < 3:
            return None
            
        memory = {
            "type": "learning",
            "category": "architecture_insight",
            "content": {
                "rule": "three-strikes",
                "attempts": failure.get("attempt"),
                "pattern": "architectural_problem_detected",
                "project": failure.get("project"),
                "error": failure.get("error_message"),
                "fix_attempts": failure.get("fix_description"),
                "recommendation": "Consider refactoring architecture",
                "severity": "high"
            },
            "tags": ["architecture", "refactoring", "design"]
        }
        
        if self.mem0:
            self.mem0.save(memory)
            
        # 自动生成架构改进建议
        insight = self._generate_architecture_insight(failure)
        
        return insight
        
    def _update_kg_with_tdd_pattern(self, memory: Dict):
        """更新知识图谱"""
        compliance = memory["content"]["compliance"]
        
        # 如果完全遵守，创建成功模式节点
        if all(compliance.values()):
            self.kg.add_node({
                "type": "tdd_success",
                "project": memory["content"]["project"],
                "file": memory["content"]["file"],
                "timestamp": memory["timestamp"]
            })
        else:
            # 如果有违反，创建改进节点
            violations = [k for k, v in compliance.items() if not v]
            self.kg.add_node({
                "type": "tdd_violation",
                "violations": violations,
                "project": memory["content"]["project"]
            })
            
    def _generate_architecture_insight(self, failure: Dict) -> Dict:
        """生成架构洞察"""
        insight = {
            "title": "架构问题检测",
            "problem": failure.get("error_message"),
            "attempts": failure.get("attempt"),
            "indicators": [
                "多次修复失败",
                "修复引入新问题",
                "症状在不同模块间移动"
            ],
            "recommendations": [
                "1. 审查模块依赖关系",
                "2. 检查是否有循环依赖",
                "3. 考虑引入接口层",
                "4. 评估是否需要重构"
            ],
            "next_steps": [
                "绘制模块依赖图",
                "识别循环依赖",
                "制定重构计划"
            ]
        }
        
        return insight


# 使用示例
if __name__ == "__main__":
    # 初始化（实际使用需要传入真实的Mem0和KG客户端）
    tracker = RuleTracker()
    
    # 示例1: 记录成功的TDD执行
    tdd_result = tracker.track_tdd_execution({
        "project": "ai-coding-rules",
        "file": "src/rule_tracker.py",
        "test_written_first": True,
        "test_failed_first": True,
        "implementation_minimal": True,
        "all_tests_pass": True,
        "regressions": 0
    })
    
    print("TDD跟踪结果:")
    print(json.dumps(tdd_result, indent=2))
    
    # 示例2: 记录预提交检查
    precommit_result = tracker.track_precommit_checks({
        "secrets_found": 0,
        "tests_passed": True,
        "lint_clean": True,
        "new_failures": 0
    })
    
    print("\n预提交检查结果:")
    print(json.dumps(precommit_result, indent=2))
    
    # 示例3: 记录3次失败
    three_strikes_result = tracker.track_three_strikes({
        "attempt": 3,
        "fix_description": "Fixed A, broke B; Fixed B, broke C; Fixed C, broke A",
        "error_message": "Circular dependency detected",
        "project": "example-project"
    })
    
    if three_strikes_result:
        print("\n3次失败分析:")
        print(json.dumps(three_strikes_result, indent=2))
