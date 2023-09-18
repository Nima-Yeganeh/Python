# https://platform.openai.com/account/api-keys
# https://platform.openai.com/apps
# https://openai.com/
# https://chat.openai.com/

import os
import openai
import time
import datetime
import random

# xcode = input("What is the code? ")
# openai.api_key = "sk-"+xcode+"joeRLSZjsL9bOXI2PT3BlbkFJEc4ys7pAJe7SL82uqxtE"
openai.api_key = ""

def generate_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": question},
            ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return(result)

ztext = "Hello"
prompt = "translate to french >> " + ztext
print(prompt)
story = generate_response(prompt)
print(story)
# time.sleep(60)
