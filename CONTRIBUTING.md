## 如何贡献

感谢您对本项目的关注！我们欢迎各种形式的贡献。

### 报告问题

如果您发现了 bug 或有功能建议，请通过 [GitHub Issues](https://github.com/yourusername/kimi-web-search/issues) 提交。

提交问题时，请包含：
- 问题的清晰描述
- 复现步骤
- 期望行为 vs 实际行为
- 环境信息（Python 版本、操作系统等）

### 提交代码

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

### 代码规范

- 遵循 PEP 8 Python 代码风格
- 添加适当的注释和文档字符串
- 确保代码通过现有测试
- 更新相关文档

### 开发设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/kimi-web-search.git
cd kimi-web-search

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install openai

# 设置环境变量
export MOONSHOT_API_KEY="your-api-key"

# 运行测试
python3 scripts/search.py "测试搜索"
```

### 技能打包

```bash
# 使用 skill-creator 打包
python3 /path/to/openclaw/skills/skill-creator/scripts/package_skill.py .
```

### 行为准则

- 尊重他人，保持友善
- 接受建设性批评
- 关注对社区最有利的事情
- 展现同理心

## 贡献者

感谢所有为本项目做出贡献的人！

- [Your Name](https://github.com/yourusername) - 项目创建者
