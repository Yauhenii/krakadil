import openai
from typing import List

from config import settings


class GPTAssistant:
    initial_messages: List = [
        {"role": "system", "content": "You are a helpful assistant for senior people."},
        {"role": "assistant", "content": "Hi! How can I help you"}
    ]
    messages: List

    def __init__(self):
        openai.api_key = settings.gpt.api_key
        self.messages = self.initial_messages

    def ask(self, content) -> str:
        self.messages.append({"role": "user", "content": content})
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        answer = chat_completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})
        return answer
