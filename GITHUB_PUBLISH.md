# GitHub 发布指南

## 项目信息

| 项目 | 内容 |
|------|------|
| **项目名称** | kimi-web-search |
| **描述** | OpenClaw Skill for web search using Kimi API |
| **许可证** | MIT |
| **本地路径** | `~/.openclaw/workspace/projects/kimi-web-search/` |

## 发布步骤

### 1. 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写信息：
   - Repository name: `kimi-web-search`
   - Description: `OpenClaw Skill - Web search using Kimi API's $web_search builtin_function`
   - Visibility: Public
   - 不勾选 "Initialize this repository with a README"
3. 点击 "Create repository"

### 2. 推送本地代码

```bash
cd ~/.openclaw/workspace/projects/kimi-web-search/

# 添加远程仓库（替换 yourusername 为你的 GitHub 用户名）
git remote add origin https://github.com/yourusername/kimi-web-search.git

# 推送到 GitHub
git push -u origin main
```

### 3. 配置仓库设置

在 GitHub 仓库页面：

1. **Settings > General**
   - 勾选 "Issues"
   - 勾选 "Discussions"（可选）
   - 勾选 "Projects"（可选）

2. **Settings > Branches**
   - 添加分支保护规则：
     - Branch name pattern: `main`
     - 勾选 "Require pull request reviews before merging"
     - 勾选 "Require status checks to pass"

3. **Settings > Secrets and variables > Actions**
   - 不需要添加 secrets（技能本身不需要）

### 4. 创建 Release

1. 访问仓库页面的 "Releases" 标签
2. 点击 "Create a new release"
3. 点击 "Choose a tag" 并输入 `v1.0.0`
4. 填写发布信息：

**Title**: Release v1.0.0 - Initial Release

**Description**:
```markdown
## What's New

### Features
- Web search using Kimi API's `$web_search` builtin_function
- Support for Chinese and English queries
- Command-line interface
- Python API for integration
- Token usage reporting

### Installation

#### Via ClawHub
```bash
clawhub install kimi-web-search
```

#### Manual Installation
1. Download `kimi-web-search.skill` from Assets
2. Copy to your OpenClaw skills directory

### Requirements
- Python 3.8+
- openai package
- Moonshot API Key

### Usage
```bash
export MOONSHOT_API_KEY="your-key"
python3 scripts/search.py "your search query"
```

### Cost
- ¥0.03 per search call
- Tokens consumed as prompt tokens
```

5. 上传 `kimi-web-search.skill` 文件作为附件
6. 点击 "Publish release"

### 5. 添加到 ClawHub

1. 访问 https://clawhub.com
2. 点击 "Publish Skill"
3. 上传 `kimi-web-search.skill`
4. 填写信息：
   - Name: `kimi-web-search`
   - Display Name: `Kimi Web Search`
   - Description: `Web search using Kimi API's builtin_function`
   - Tags: `search, web, kimi, moonshot`
   - Category: `Tools`
   - License: `MIT`
   - GitHub URL: `https://github.com/yourusername/kimi-web-search`
5. 提交审核

## 后续维护

### 更新版本

```bash
# 修改代码后
git add .
git commit -m "Fix: description of changes"
git push

# 创建新标签
git tag v1.0.1
git push origin v1.0.1
```

GitHub Actions 会自动创建 Release 并上传 skill 文件。

### 更新 ClawHub

1. 重新打包技能
2. 在 ClawHub 更新版本

## 相关链接

- [OpenClaw](https://openclaw.ai)
- [OpenClaw Docs](https://docs.openclaw.ai)
- [Kimi Platform](https://platform.moonshot.cn/)
- [ClawHub](https://clawhub.com)
