# Kimi Web Search

使用 Kimi API 的 `$web_search` builtin_function 进行联网搜索的 OpenClaw Skill。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Kimi](https://img.shields.io/badge/Kimi-Moonshot-green)](https://moonshot.cn)

## 功能特性

- 🔍 **联网搜索** - 使用 Kimi 内置搜索功能获取最新信息
- 🌐 **双语支持** - 完美支持中文和英文搜索
- 📰 **实时资讯** - 获取新闻、股价、财报等时效性信息
- 🤖 **AI 合成** - 返回 AI 整理的搜索结果，带引用来源
- 💰 **成本透明** - 每次搜索 ¥0.03，无隐藏费用

## 快速开始

### 1. 安装依赖

```bash
pip install openai
```

### 2. 配置 API Key

```bash
export MOONSHOT_API_KEY="your-api-key-here"
```

或者创建配置文件：

```bash
mkdir -p ~/.config/moonshot
echo "your-api-key-here" > ~/.config/moonshot/api_key
```

获取 API Key：[Moonshot 开放平台](https://platform.moonshot.cn/)

### 3. 使用技能

```bash
python3 scripts/search.py "你的搜索关键词"
```

示例：

```bash
# 搜索公司财报
python3 scripts/search.py "紫金矿业 2025年 最新财报"

# 搜索股价信息
python3 scripts/search.py "特斯拉 股价 今天"

# 搜索新闻
python3 scripts/search.py "OpenAI 最新新闻"
```

## 在 OpenClaw 中使用

### 安装技能

```bash
clawhub install kimi-web-search
```

### 使用方式

当需要搜索最新信息时，OpenClaw 会自动调用此技能：

```
用户: 搜索一下快手最近的新闻
OpenClaw: [自动调用 kimi-web-search 技能进行搜索]
```

## 工作原理

本技能使用 Kimi 的 `$web_search` builtin_function：

1. **声明工具** - 将 `$web_search` 声明为 `builtin_function` 类型
2. **模型执行** - Kimi 模型自动执行搜索
3. **返回结果** - 获取 AI 合成的搜索结果

```python
tools = [
    {
        "type": "builtin_function",
        "function": {
            "name": "$web_search",
        },
    },
]
```

## 成本说明

| 项目 | 费用 |
|------|------|
| 搜索调用 | ¥0.03/次 |
| Token 消耗 | 搜索结果计入 prompt tokens |

建议使用 `kimi-k2-turbo-preview` 模型以获得更大上下文窗口。

## 项目结构

```
kimi-web-search/
├── SKILL.md              # 技能说明文档
├── scripts/
│   └── search.py         # 搜索脚本
├── README.md             # 本文件
├── LICENSE               # MIT 许可证
└── .github/
    └── workflows/        # CI/CD 工作流
```

## 开发

### 本地测试

```bash
# 克隆仓库
git clone https://github.com/yourusername/kimi-web-search.git
cd kimi-web-search

# 设置环境变量
export MOONSHOT_API_KEY="your-api-key"

# 运行测试
python3 scripts/search.py "测试搜索"
```

### 打包技能

```bash
python3 /path/to/skill-creator/scripts/package_skill.py .
```

## 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

[MIT](LICENSE) © 2025 [Your Name]

## 相关链接

- [OpenClaw 官网](https://openclaw.ai)
- [OpenClaw 文档](https://docs.openclaw.ai)
- [Kimi 开放平台](https://platform.moonshot.cn/)
- [Moonshot AI](https://moonshot.cn)
- [ClawHub](https://clawhub.com)

## 致谢

- [OpenClaw](https://openclaw.ai) - 强大的 AI 助手平台
- [Moonshot AI](https://moonshot.cn) - 提供 Kimi 大模型和搜索能力
