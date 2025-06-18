MCP Related Projects

# ArXiv research papers
## 环境
python >= 3.10.12
node = v22.16.0 (建议较高版本，否则会有问题)

# Python 包管理器 uv
## 安装
pip install uv
## 创建虚拟环境
### 与conda类似，但是conda是全局的，uv是基于项目的
uv venv --python <python_version>
如：
uv venv --python 3.10.12
## 激活虚拟环境
### linux/mac
source .venv/bin/activate
### windows
.\.venv\Scripts\activate.bat
## 添加依赖
### 直接添加
uv pip add <package>
### 从传统依赖列表迁移
uv add -r requirements.txt
## 移除依赖
uv pip remove <package>
## 生成 requirements.txt
uv pip compile pyproject.toml -o requirements.txt
## 安装依赖
并行安装
### 通过 pyproject.toml 安装依赖：
uv sync
### 通过 requirements.txt 安装依赖：
uv pip install -r requirements.txt

# MCP 调试
## 设置 node 版本
nvm use v22.16.0
## 安装 MCP inspector
npx @modelcontextprotocol/inspector uv run research_server_stdio.py

# Web 部署
JMM2015@163.com
https://dashboard.render.com/
## 创建新的 Web 服务