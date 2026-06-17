#!/bin/bash
# AI Coding Rules 安装脚本
# Usage: ./install.sh [opencode|oh-my-openagent] [target-path]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VERSION="1.0.0"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 安装 OpenCode 规则
install_opencode() {
    log_info "安装 OpenCode 规则..."
    
    local target_dir="${1:-$HOME/.config/opencode/rules}"
    
    # 备份现有规则
    if [ -d "$target_dir" ]; then
        local backup_dir="${target_dir}.backup.$(date +%Y%m%d_%H%M%S)"
        log_warn "备份现有规则到 $backup_dir"
        cp -r "$target_dir" "$backup_dir"
    fi
    
    # 创建目录
    mkdir -p "$target_dir"
    
    # 复制规则
    log_info "复制规则文件到 $target_dir"
    cp "$SCRIPT_DIR/opencode-rules"/*.md "$target_dir/"
    
    # 验证安装
    if [ -f "$target_dir/tdd-enforcement.md" ]; then
        log_info "✅ OpenCode 规则安装成功！"
        log_info "   位置: $target_dir"
        log_info "   规则数: $(ls "$target_dir"/*.md 2>/dev/null | wc -l)"
    else
        log_error "安装失败"
        exit 1
    fi
    
    log_warn "请重启 OpenCode 以生效"
}

# 安装 oh-my-openagent 规则
install_oh_my_openagent() {
    log_info "安装 oh-my-openagent 规则..."
    
    local project_path="${1:-$(pwd)}"
    local target_dir="$project_path/.omo/rules"
    
    if [ ! -d "$project_path/.omo" ]; then
        log_warn "创建 .omo 目录"
        mkdir -p "$project_path/.omo"
    fi
    
    # 备份现有规则
    if [ -d "$target_dir" ]; then
        local backup_dir="${target_dir}.backup.$(date +%Y%m%d_%H%M%S)"
        log_warn "备份现有规则到 $backup_dir"
        cp -r "$target_dir" "$backup_dir"
    fi
    
    # 创建目录
    mkdir -p "$target_dir"
    
    # 复制规则
    log_info "复制规则文件到 $target_dir"
    cp "$SCRIPT_DIR/oh-my-openagent-rules"/*.md "$target_dir/"
    
    # 验证安装
    if [ -f "$target_dir/tdd-enforcement.md" ]; then
        log_info "✅ oh-my-openagent 规则安装成功！"
        log_info "   位置: $target_dir"
        log_info "   规则数: $(ls "$target_dir"/*.md 2>/dev/null | wc -l)"
    else
        log_error "安装失败"
        exit 1
    fi
    
    log_warn "请重启 oh-my-openagent 以生效"
}

# 验证安装
verify_installation() {
    log_info "验证安装..."
    
    local opencode_dir="$HOME/.config/opencode/rules"
    local errors=0
    
    if [ -d "$opencode_dir" ]; then
        log_info "✅ OpenCode 规则目录存在"
        log_info "   规则文件: $(ls "$opencode_dir"/*.md 2>/dev/null | wc -l)"
    else
        log_warn "OpenCode 规则目录不存在"
        ((errors++))
    fi
    
    return $errors
}

# 显示帮助
show_help() {
    cat << EOF
AI Coding Rules 安装脚本 v$VERSION

用法:
    ./install.sh [COMMAND] [OPTIONS]

命令:
    opencode              安装 OpenCode 规则
    oh-my-openagent       安装 oh-my-openagent 规则
    verify                验证安装
    help                  显示帮助

选项:
    -p, --path PATH       指定目标路径
    -h, --help            显示帮助

示例:
    # 安装 OpenCode 规则
    ./install.sh opencode
    
    # 安装到指定目录
    ./install.sh opencode --path /path/to/rules
    
    # 安装 oh-my-openagent 规则
    ./install.sh oh-my-openagent ~/workspace/my-project
    
    # 验证安装
    ./install.sh verify

EOF
}

# 主函数
main() {
    local command="${1:-}"
    local target_path=""
    
    # 解析参数
    while [[ $# -gt 0 ]]; do
        case $1 in
            -p|--path)
                target_path="$2"
                shift 2
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                command="$1"
                shift
                ;;
        esac
    done
    
    # 执行命令
    case "$command" in
        opencode)
            install_opencode "$target_path"
            ;;
        oh-my-openagent)
            install_oh_my_openagent "$target_path"
            ;;
        verify)
            verify_installation
            ;;
        help|*)
            show_help
            exit 0
            ;;
    esac
}

main "$@"
