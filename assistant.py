from phi.assistant import Assistant
from phi.llm.openrouter import OpenRouter

assistant = Assistant(
    llm=OpenRouter(model="mistralai/mistral-7b-instruct:free"),
    description="You help people with their health and fitness goals.",
)
assistant.print_response(
    "Share a 2 sentence quick and healthy breakfast recipe.", markdown=True
)

#set OPENROUTER_API_KEY=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
#set OPENROUTER_API_KEY=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