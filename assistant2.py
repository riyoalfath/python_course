import os
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

# Fetch the API key from the environment variable
api_key = os.getenv('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')
if not api_key:
    raise ValueError("API key not found in environment variables")

# Initialize the Assistant with the API key
assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o", max_tokens=500, temperature=0.3, api_key=api_key),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
)

assistant.print_response("What's happening in France?", markdown=True)

#set OPENROUTER_API_KEY=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