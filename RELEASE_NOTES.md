## Release v1.0.0

🎉 **Kimi Web Search Skill 首个正式版本发布！**

使用 Kimi API 的 `$web_search` builtin_function 进行联网搜索的 OpenClaw Skill。

---

## ✨ 功能特性

- 🔍 **联网搜索** - 使用 Kimi 内置搜索获取最新信息
- 🌐 **双语支持** - 完美支持中文和英文搜索查询
- 📰 **实时资讯** - 获取新闻、股价、财报等时效性信息
- 🤖 **AI 合成** - 返回 AI 整理的搜索结果，带引用来源
- 💰 **成本透明** - 每次搜索 ¥0.03，无隐藏费用

---

## 📦 安装方式

### 方式一：下载 Skill 文件（推荐）

1. 下载本页面附件中的 `kimi-web-search.skill`
2. 复制到你的 OpenClaw skills 目录：
   ```bash
   cp kimi-web-search.skill ~/.openclaw/skills/
   ```

### 方式二：通过 ClawHub 安装

```bash
clawhub install kimi-web-search
```

### 方式三：从源码安装

```bash
git clone https://github.com/ppweek/kimi-web-search.git
cd kimi-web-search
# 复制 src 目录到 OpenClaw skills 目录
cp -r src ~/.openclaw/skills/kimi-web-search
```

---

## 🔧 配置要求

### 1. 安装依赖

```bash
pip install openai
```

### 2. 配置 API Key

```bash
export MOONSHOT_API_KEY="your-api-key-here"
```

或创建配置文件：

```bash
mkdir -p ~/.config/moonshot
echo "your-api-key-here" > ~/.config/moonshot/api_key
```

获取 API Key：[Moonshot 开放平台](https://platform.moonshot.cn/)

---

## 🚀 使用方法

### 命令行

```bash
python3 ~/.openclaw/skills/kimi-web-search/scripts/search.py "你的搜索关键词"
```

### 示例

```bash
# 搜索公司财报
python3 scripts/search.py "紫金矿业 2025年 最新财报"

# 搜索股价信息
python3 scripts/search.py "特斯拉 股价 今天"

# 搜索新闻
python3 scripts/search.py "OpenAI 最新新闻"
```

### 在 OpenClaw 中使用

当需要搜索最新信息时，OpenClaw 会自动调用此技能：

```
用户: 搜索一下快手最近的新闻
OpenClaw: [自动调用 kimi-web-search 技能进行搜索]
```

---

## 💰 成本说明

| 项目 | 费用 |
|------|------|
| 搜索调用 | ¥0.03/次 |
| Token 消耗 | 搜索结果计入 prompt tokens |

建议使用 `kimi-k2-turbo-preview` 模型以获得更大上下文窗口。

---

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `kimi-web-search.skill` | 打包好的 OpenClaw Skill 文件 |
| `src/SKILL.md` | 技能说明文档 |
| `src/scripts/search.py` | 搜索脚本 |

---

## 🔗 相关链接

- [项目主页](https://github.com/ppweek/kimi-web-search)
- [OpenClaw 官网](https://openclaw.ai)
- [OpenClaw 文档](https://docs.openclaw.ai)
- [Kimi 开放平台](https://platform.moonshot.cn/)
- [ClawHub](https://clawhub.com)

---

## 📜 许可证

[MIT License](LICENSE)

---

## 🙏 致谢

- [OpenClaw](https://openclaw.ai) - 强大的 AI 助手平台
- [Moonshot AI](https://moonshot.cn) - 提供 Kimi 大模型和搜索能力

---

**Enjoy searching with Kimi!** 🎉
