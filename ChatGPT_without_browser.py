import os

os.system("title ChatGPT without browser")
from time import sleep
import openai
import datetime
import random

def center(str, weight):
    print(" "*weight + str)

str = "ChatGPT without browser 2.0, progame1201"

weight = 40
center(str, weight)
str = "using the gpt-3.5-turbo-0613 model from OpenAI https://openai.com/"
weight = 29
center(str, weight)
print("------------------------------------------------------------------------------------------------------------------------")

sleep(1)

print("API")
print("-------------------------------")
print("1 - use your API key")

print("2 - use the standard API key")

print("3 - use a second spare key (another user)")

chooseAPI = input("")

if chooseAPI == "1":
 API = input("API key:")
 openai.api_key = API
messages = []

if chooseAPI == "2":
    API = "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"
    openai.api_key = API

if chooseAPI == "3":
    API = "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"
    openai.api_key = API
print()
print("Logs")
print("-------------------------------")
print("1 - turn on logs")
print("2 - turn off logs")
turnonlogs = input("")
if turnonlogs == "1":
 randomnum = random.randint(0, 9999999999999)
 logname = "log-{}.txt".format(randomnum)
 log = open(logname, "w")
 log.close()
while True:
    msg1 = input("you:")
    if turnonlogs == "1":
        log = open(logname, "a")
        log.write("\nyou: " + msg1)
        log.close()
    print()

    print("ChatGPT generates a response...")

    print()

    messages.append({"role": "user", "content": msg1})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )
    chat_response = completion.choices[0].message.content

    print("ChatGPT: " + completion.choices[0].message.content)
    if turnonlogs == "1":
        log = open(logname, "a")
        log.write("\nChatGPT: " + completion.choices[0].message.content)
        log.close()
    print()

    messages.append({"role": "assistant", "content": chat_response})
