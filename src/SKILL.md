---
name: kimi-web-search
description: Use Kimi API's builtin_function $web_search to perform web search. Use when you need to search for latest news, real-time information, stock prices, company updates, or any time-sensitive data. Supports Chinese and English search queries. Returns AI-synthesized search results with citations.
---

# Kimi Web Search

Use Kimi API's built-in web search function `$web_search` to search the internet for latest information.

## Prerequisites

### 1. Install Dependencies

```bash
pip install openai
```

### 2. Configure API Key

Set your Moonshot API Key as an environment variable:

```bash
export MOONSHOT_API_KEY="your-api-key-here"
```

Or create a config file:

```bash
mkdir -p ~/.config/moonshot
echo "your-api-key-here" > ~/.config/moonshot/api_key
```

Get your API Key from: https://platform.moonshot.cn/

## Usage

### Command Line

```bash
python3 scripts/search.py "your search query"
```

Examples:

```bash
# Search for company news
python3 scripts/search.py "Apple latest earnings 2025"

# Search for stock information
python3 scripts/search.py "Tesla stock price today"

# Search in Chinese
python3 scripts/search.py "快手 最新财报 2025"
```

### Python API

```python
from scripts.search import search

result = search("your search query")
print(result)
```

## How It Works

This skill uses Kimi's `$web_search` builtin_function:

1. **Declaration**: Declare `$web_search` as a `builtin_function` type tool
2. **Execution**: Kimi model automatically performs the search
3. **Result**: Returns AI-synthesized search results with sources

Unlike regular web search APIs, Kimi's `$web_search`:
- Is executed internally by Kimi model
- Returns synthesized results, not raw search results
- Charges ¥0.03 per search call
- Consumes tokens (search results count as prompt tokens)

## Cost Considerations

- **Search fee**: ¥0.03 per search call
- **Token consumption**: Search results are included in prompt tokens
- **Recommended model**: `kimi-k2-turbo-preview` (larger context window)

## Troubleshooting

### Connection Error

If you encounter SSL/connection errors, check your network connection or try:

```bash
# Test connectivity
curl https://api.moonshot.cn/v1/models \
  -H "Authorization: Bearer $MOONSHOT_API_KEY"
```

### Authentication Error

Make sure your API Key is valid and has not expired. Check at:
https://platform.moonshot.cn/console

### Rate Limit

If you hit rate limits, wait a moment before retrying. Consider:
- Adding delays between requests
- Caching results for repeated queries

## Resources

### scripts/search.py

Main search script that handles:
- API client initialization
- Tool declaration (`$web_search`)
- Message handling and tool call execution
- Result formatting

## Examples

### Investment Research

```bash
python3 scripts/search.py "紫金矿业 2025年3月 最新财报 股价"
```

### News Monitoring

```bash
python3 scripts/search.py "OpenAI latest news today"
```

### Product Research

```bash
python3 scripts/search.py "iPhone 16 review 2025"
```

## Notes

- Search results are cached for 15 minutes by default
- Results may vary based on Kimi's search index
- For time-sensitive queries, include date in the query
- Chinese queries work well for Chinese content

## License

MIT License - Feel free to use and modify.
