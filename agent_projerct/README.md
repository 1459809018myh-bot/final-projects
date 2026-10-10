# AI知识问答系统

## 项目简介

基于FastAPI和OpenAI的智能知识问答系统，支持对话管理、知识库构建和检索增强生成（RAG）。系统提供Web界面和API接口，可以上传文档构建知识库，并通过AI进行智能问答。

## 主要功能

- **智能对话**：基于大语言模型的自然语言对话
- **知识库管理**：支持文档上传、存储和检索
- **RAG检索增强**：结合文档内容提供更准确的回答
- **Web界面**：友好的用户交互界面
- **API服务**：RESTful API接口，支持集成开发

## 技术栈

- **后端框架**：FastAPI
- **Web服务器**：Uvicorn
- **AI模型**：OpenAI API
- **前端**：HTML/CSS/JavaScript
- **数据处理**：Pandas
- **其他**：CORS中间件、静态文件服务

## 项目结构

```
agent_projerct/
├── app_server.py          # FastAPI应用主入口
├── generate.py            # 内容生成模块
├── webui.py              # Web界面服务
├── requirements.txt      # Python依赖
├── test.csv             # 测试数据
├── chat/                # 对话路由模块
├── knowledgebase_server/ # 知识库服务模块
└── configs/             # 配置文件
```

## 安装说明

### 环境要求

- Python 3.8+
- pip包管理器

### 安装步骤

1. 克隆项目到本地
```bash
git clone <repository-url>
cd agent_projerct
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置API密钥
   - 在配置文件中设置OpenAI API密钥
   - 配置其他必要的环境变量

## 使用方法

### 启动服务器

运行主服务器：
```bash
python app_server.py
```

服务器将在 `http://127.0.0.1:6605` 启动

### 启动Web界面

```bash
python webui.py
```

### API接口

#### 对话接口
```
POST /chat/
```

#### 知识库接口
```
POST /kb/upload    # 上传文档
GET  /kb/list      # 获取知识库列表
POST /kb/query     # 查询知识库
```

### 使用示例

1. **上传文档到知识库**
   - 通过Web界面或API上传文档
   - 系统自动处理并索引文档内容

2. **进行智能问答**
   - 在Web界面输入问题
   - 系统结合知识库内容生成回答

## 配置说明

### 媒体文件目录
在 `configs/setting.py` 中配置 `MEDIA_DIR` 路径

### CORS设置
默认允许所有来源的跨域请求，生产环境建议限制

### 服务器配置
- 主机：127.0.0.1
- 端口：6605
- 日志级别：info

## 开发说明

### 添加新的路由
在相应的路由模块中添加路由函数，并在 `app_server.py` 中注册

### 扩展知识库功能
在 `knowledgebase_server/` 目录下添加新的处理模块

## 注意事项

- 确保OpenAI API密钥配置正确
- 大文件上传可能需要调整服务器超时设置
- 生产环境部署时注意安全配置

## 许可证

[添加许可证信息]

## 贡献

欢迎提交Issue和Pull Request

## 联系方式

[添加联系方式]
