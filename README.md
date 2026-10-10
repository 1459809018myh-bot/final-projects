# AI应用项目集合

这是一个包含多个AI应用项目的代码仓库，涵盖了知识问答、人脸识别、智能教育、电商客服、旅游推荐等多个应用场景。所有项目均采用Python开发，集成了深度学习、自然语言处理、计算机视觉等前沿技术。

## 项目列表

### 1. AI知识问答系统 (agent_projerct)

基于FastAPI和OpenAI的智能知识问答系统，支持RAG检索增强生成。

**主要功能**
- 智能对话与知识库管理
- 文档上传与检索
- RESTful API接口
- Web交互界面

**技术栈**: FastAPI, OpenAI API, Pandas

**快速开始**
```bash
cd agent_projerct
pip install -r requirements.txt
python app_server.py
```

[详细文档](./agent_projerct/README.md)

---

### 2. 人脸识别签到系统 (人脸识别签到)

基于OpenCV的人脸识别考勤系统，提供Gradio Web界面。

**主要功能**
- 人脸注册与实时识别
- 签到记录管理
- 多人脸检测
- 置信度评分

**技术栈**: OpenCV, Gradio, NumPy

**快速开始**
```bash
cd 人脸识别签到
pip install -r requirements.txt
python app.py
```

[详细文档](./人脸识别签到/README.md)

---

### 3. 知契·智能教育助手 (学习助手)

功能完善的AI教育助手系统，集成RAG、学习监控、家长报告等功能。

**主要功能**
- AI智能对话与教材检索
- 专注度监控
- 家长报告生成
- 多渠道接入（Web/飞书/QQ）
- 工具调用系统

**技术栈**: FastAPI, FAISS, SQLite, 飞书SDK

**快速开始**
```bash
cd 学习助手
pip install -r requirements.txt
python main.py  # 命令行模式
# 或
python gateway.py  # Web API模式
```

[详细文档](./学习助手/README.md)

---

### 4. 智能电商客服系统 (智能电商客服)

基于AI Agent的电商客服自动化系统，支持离线和在线两种模式。

**主要功能**
- 订单查询与退换货处理
- 工单管理与人工转接
- 商家管理后台
- 智能意图识别
- 上下文对话记忆

**技术栈**: Agent架构, Flask/FastAPI, WebSocket

**快速开始**
```bash
cd 智能电商客服
pip install -r requirements.txt
# 启动客服端
cd 客服页面 && python app.py
# 启动商家端
cd 模拟商家页面 && python app.py
```

[详细文档](./智能电商客服/README.md)

---

### 5. 四季个性化旅游推荐系统 (智能旅行助手)

基于多维度相似度匹配的智能旅游推荐系统。

**主要功能**
- 个性化景点推荐
- 季节与风格匹配
- 预算与行程规划
- 用户偏好管理
- 收藏与历史记录

**技术栈**: Flask, SQLite, 推荐算法

**快速开始**
```bash
cd 智能旅行助手/travel-recommend-system-main
pip install flask werkzeug
python init_db.py  # 初始化数据库
python app.py
```

[详细文档](./智能旅行助手/README.md)

---

### 6. 碳素块数据集 (2.0碳素块数据集)

用于机器学习的碳素块相关数据集。

**说明**: 包含碳素块相关的数据集，可用于材料分析、质量检测等机器学习任务。

---

## 技术栈总览

### AI与机器学习
- **大语言模型**: OpenAI API, 通义千问, 智谱GLM
- **计算机视觉**: OpenCV, 深度学习人脸识别
- **向量检索**: FAISS
- **推荐算法**: 多维度相似度匹配

### Web框架
- FastAPI (异步高性能)
- Flask (轻量级Web框架)
- Gradio (快速Web界面)

### 数据存储
- SQLite (轻量级关系数据库)
- FAISS (向量数据库)
- 文件系统存储

### 第三方集成
- 飞书开放平台
- QQ频道Bot
- B站API
- MCP协议

## 项目特点

### 完整性
每个项目都包含完整的功能实现、配置说明和使用文档。

### 实用性
涵盖企业常见的AI应用场景：
- 知识管理与问答
- 人脸识别与考勤
- 智能教育辅导
- 电商客服自动化
- 个性化推荐

### 可扩展性
- 模块化设计，易于扩展
- 支持多种LLM接入
- 工具系统可插拔
- 数据存储可替换

### 易部署
- Python生态，依赖管理清晰
- 支持Docker容器化
- 提供多种部署方案

## 环境要求

### 基础环境
- Python 3.8+
- pip包管理器

### 可选组件
- Docker（容器化部署）
- Nginx（反向代理）
- SQLite 3（部分项目需要）
- 摄像头（人脸识别项目）

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/1459809018myh-bot/final-projects.git
cd final-projects
```

### 2. 选择项目

进入感兴趣的项目目录，查看该项目的README.md文档。

### 3. 安装依赖

每个项目都有独立的requirements.txt：

```bash
cd <项目目录>
pip install -r requirements.txt
```

### 4. 配置与运行

根据各项目的README说明进行配置和启动。

## 项目结构

```
final-projects/
├── README.md                    # 本文件：总仓库说明
├── agent_projerct/             # AI知识问答系统
│   ├── README.md
│   └── ...
├── 人脸识别签到/                # 人脸识别签到系统
│   ├── README.md
│   └── ...
├── 学习助手/                    # 智能教育助手
│   ├── README.md
│   └── ...
├── 智能电商客服/                # 电商客服系统
│   ├── README.md
│   └── ...
├── 智能旅行助手/                # 旅游推荐系统
│   ├── README.md
│   └── ...
└── 2.0碳素块数据集/            # 数据集
    └── ...
```

## 使用场景

### 企业应用
- **客服中心**: 智能电商客服系统
- **人力资源**: 人脸识别签到系统
- **知识管理**: AI知识问答系统

### 教育行业
- **在线教育**: 智能教育助手
- **学习辅导**: 个性化AI辅导

### 生活服务
- **旅游规划**: 旅游推荐系统
- **个性化推荐**: 多维度匹配算法

## 开发指南

### 代码规范
- 遵循PEP 8 Python代码规范
- 函数和类添加文档字符串
- 关键逻辑添加注释

### 目录结构
建议各项目保持清晰的目录结构：
```
project/
├── README.md          # 项目说明
├── requirements.txt   # 依赖清单
├── app.py            # 主程序入口
├── config.py         # 配置管理
├── modules/          # 功能模块
├── static/           # 静态资源
├── templates/        # 模板文件
└── tests/            # 测试用例
```

### 测试
鼓励为关键功能编写测试用例：
```bash
python -m pytest tests/
```

### 贡献流程
1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交Pull Request

## 常见问题

### Q: 如何选择合适的项目？
A: 根据应用场景选择：
- 需要知识管理 → AI知识问答系统
- 需要考勤打卡 → 人脸识别签到
- 开发教育应用 → 智能教育助手
- 电商客服自动化 → 智能电商客服
- 旅游相关应用 → 旅游推荐系统

### Q: 项目可以商用吗？
A: 请查看各项目的LICENSE文件，遵循相应的开源协议。

### Q: 如何获得技术支持？
A: 
- 查看项目README文档
- 提交GitHub Issue
- 联系项目维护者

### Q: 可以同时运行多个项目吗？
A: 可以，但注意端口冲突。各项目使用不同端口，或修改配置文件中的端口设置。

## 性能与优化

### 数据库优化
- 添加合适的索引
- 定期清理过期数据
- 使用连接池

### API性能
- 实现请求缓存
- 使用异步处理
- 添加限流机制

### 部署优化
- 使用Gunicorn/Uvicorn多进程
- Nginx负载均衡
- Docker容器化

## 安全建议

- 不要将API密钥提交到代码仓库
- 使用环境变量管理敏感配置
- 定期更新依赖包
- 对用户输入进行验证和清洗
- 生产环境使用HTTPS

## 许可证

各项目可能使用不同的开源许可证，详见各项目目录下的LICENSE文件。

## 更新日志

### 2026-10-10
- 初始版本发布
- 包含5个完整项目
- 添加详细文档

## 致谢

感谢以下开源项目和社区：
- FastAPI & Flask
- OpenAI
- OpenCV
- Gradio
- 飞书开放平台
- 所有贡献者

## 联系方式

- GitHub: [@1459809018myh-bot](https://github.com/1459809018myh-bot)
- 项目主页: https://github.com/1459809018myh-bot/final-projects

## Star History

如果这个项目对你有帮助，欢迎Star支持！⭐

---

**最后更新**: 2026-10-10
