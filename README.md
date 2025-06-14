MCP Related Projects

# ArXiv research papers
## 环境
python >= 3.10.12
node = v22.16.0 (建议较高版本，否则会有问题)

# Python 包管理器 uv
## 安装
pip install uv
## 添加依赖
uv pip add <package>
## 移除依赖
uv pip remove <package>
## 安装依赖
uv pip install .
## 生成 requirements.txt
uv pip compile pyproject.toml -o requirements.txt

# MCP 调试
## 设置 node 版本
nvm use v22.16.0
## 安装 MCP inspector
npx @modelcontextprotocol/inspector uv run research_server_stdio.py