import openai
from typing import List

from config import settings

import tiktoken

#encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def num_tokens_from_string(string: str, encoding) -> int:
    """Returns the number of tokens in a text string."""
    num_tokens = len(encoding.encode(string))
    return num_tokens

def crop_list_string(lst):
    # if total number of tokens exceeds 4097, crop the list from the beginning
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    last_element_id_to_keep = len(lst)
    sum_tokens = 0
    for elem in lst[::-1]:
        #print(last_element_id_to_keep, elem)
        sum_tokens += num_tokens_from_string(elem["content"], encoding)
        if sum_tokens > 4097:
            break
        last_element_id_to_keep -= 1
        
    return lst[last_element_id_to_keep:]

class GPTAssistant:
    initial_messages: List =  [
        {"role": "system", "content": "You are a helpful assistant for eldery people. Make your answers short. Simplify the message, easy to understand is key. Instead of using jargon or medical terms, use simple words that are easier to understand when talking to them. Make your messages short and informal and friendly."},
        {"role": "assistant", "content": "Hey, how I can help you?"}
    ]
    messages: List

    def __init__(self):
        openai.api_key = settings.gpt.api_key
        self.messages = self.initial_messages

    async def ask(self, content) -> str:
        content = f"It is input from the eldery user, it may contain some errors due to speech recognition: {content}.  If the conversation has come to a standstill, suggest a random topic for casual talk"
        self.messages.append({"role": "user", "content": content})
        # keep only the last 4097 tokens
        self.messages = crop_list_string(self.messages)
        chat_completion = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        answer = chat_completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})
        return answer
