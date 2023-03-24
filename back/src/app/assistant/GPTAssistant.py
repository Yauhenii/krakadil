import openai
from typing import List

from config import settings


class GPTAssistant:
    initial_messages: List = [
        {"role": "system", "content": "You are a helpful assistant for eldery people."},
        {"role": "assistant", "content": "Make your answers short. Simplify the message, easy to understand is key. Instead of using jargon or medical terms, use simple words that are easier to understand when talking to them. Make your messages short and informal and friendly."}
    ]
    messages: List

    def __init__(self):
        openai.api_key = settings.gpt.api_key
        self.messages = self.initial_messages

    async def ask(self, content) -> str:
        self.messages.append({"role": "user", "content": content})
        chat_completion = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        answer = chat_completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})
        return answer
