#!/usr/bin/env python3
"""
Kimi Web Search Tool
Use Kimi API's builtin_function $web_search to perform web search

Usage:
    python3 search.py "your search query"
    python3 search.py "Apple latest earnings 2025"

Environment:
    MOONSHOT_API_KEY: Kimi API Key (required)
"""

import os
import sys
import json
from typing import Dict, Any

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai package not installed. Run: pip install openai")
    sys.exit(1)


def get_api_key() -> str:
    """Get Moonshot/Kimi API Key from environment or config file"""
    # Try environment variable first
    api_key = os.environ.get("MOONSHOT_API_KEY") or os.environ.get("KIMI_API_KEY")
    
    if not api_key:
        # Try config files
        config_paths = [
            os.path.expanduser("~/.config/moonshot/api_key"),
            os.path.expanduser("~/.openclaw/credentials/moonshot-api-key"),
        ]
        for path in config_paths:
            if os.path.exists(path):
                with open(path, "r") as f:
                    api_key = f.read().strip()
                    if api_key:
                        break
    
    if not api_key:
        print("Error: MOONSHOT_API_KEY not found.")
        print("Please set it as environment variable or create ~/.config/moonshot/api_key")
        print("Get your API key from: https://platform.moonshot.cn/")
        sys.exit(1)
    
    return api_key


def search(query: str, model: str = "kimi-k2-turbo-preview") -> str:
    """
    Perform web search using Kimi's $web_search builtin_function
    
    Args:
        query: Search query string
        model: Model name (default: kimi-k2-turbo-preview for larger context)
    
    Returns:
        AI-synthesized search results
    """
    import httpx
    
    # Create HTTP client with timeout
    http_client = httpx.Client(
        base_url="https://api.moonshot.cn/v1",
        timeout=60.0,
        follow_redirects=True,
    )
    
    client = OpenAI(
        base_url="https://api.moonshot.cn/v1",
        api_key=get_api_key(),
        http_client=http_client,
    )
    
    # Declare $web_search as builtin_function
    tools = [
        {
            "type": "builtin_function",
            "function": {
                "name": "$web_search",
            },
        },
    ]
    
    # Initialize messages
    messages = [
        {"role": "system", "content": "You are Kimi, a helpful AI assistant. Use web search to get latest information and provide accurate, detailed answers."},
        {"role": "user", "content": query},
    ]
    
    max_iterations = 3
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        
        # Send request to Kimi API
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            temperature=0.6,
            max_tokens=8192,
        )
        
        choice = completion.choices[0]
        
        # If no tool_calls, return the result directly
        if choice.finish_reason != "tool_calls":
            return choice.message.content
        
        # Handle tool_calls
        messages.append(choice.message)  # Add assistant message
        
        for tool_call in choice.message.tool_calls:
            tool_call_name = tool_call.function.name
            tool_call_arguments = json.loads(tool_call.function.arguments)
            
            if tool_call_name == "$web_search":
                # Log search token usage (optional)
                usage = tool_call_arguments.get("usage", {})
                if usage:
                    print(f"[Search] Content tokens: {usage.get('total_tokens', 'N/A')}", file=sys.stderr)
                
                # Return arguments back to Kimi for internal execution
                tool_result = tool_call_arguments
            else:
                tool_result = {"error": f"Unknown tool: {tool_call_name}"}
            
            # Add tool result to messages
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call_name,
                "content": json.dumps(tool_result),
            })
    
    return "Error: Max iterations reached"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 search.py <query>")
        print('Example: python3 search.py "Apple latest earnings 2025"')
        print('         python3 search.py "快手 最新财报 2025"')
        sys.exit(1)
    
    query = sys.argv[1]
    print(f"Searching: {query}\n", file=sys.stderr)
    
    result = search(query)
    print(result)


if __name__ == "__main__":
    main()
