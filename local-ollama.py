# -*- coding: utf-8 -*-

from ollama import chat
from ollama import ChatResponse


response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'What is the capital city of Thailand?',
  },
])


# print #1
print(response['message']['content'])

# print #2
print(response.message.content)
