from pywebio.input import *
from pywebio.output import *
import openai
import random
def main():
  out = output()
  put_info("ChatGPT with browser 2.0, progame1201\nusing the gpt-3.5-turbo-0613 model from OpenAI https://openai.com/")
  put_text(" ")
  put_link(name="https://github.com/progame1201/ChatGPT_without_browser", url="https://github.com/progame1201/ChatGPT_without_browser")
  put_text(" ")
  put_scrollable(out, height=450, keep_bottom=True)


  out.append("API")
  out.append("-------------------------------")
  out.append("1 - use your API key")
  out.append("2 - use the standard API key")
  out.append("3 - use a second spare key (another user)")
  chooseAPI = input("API type")
  if chooseAPI == "1":
    API = input("API key:")
    openai.api_key = API
  messages = []
  if chooseAPI == "2":
    API = ""
    openai.api_key = API
  if chooseAPI == "3":
    API = ""
    openai.api_key = API
  out.append("")

  out.append("Logs")
  out.append("-------------------------------")
  out.append("1 - turn on logs")
  out.append("2 - turn off logs")
  turnonlogs = input("Turn on logs?")
  out.append("")
  if turnonlogs == "1":
    randomnum = random.randint(0, 9999999999999)
    logname = "logWEB-{}.txt".format(randomnum)
    log = open(logname, "w")
    log.close()
  out.reset()
  while True:
    msg1 = input("message to chat gpt")
    out.append("you: " + msg1)
    if turnonlogs == "1":
        log = open(logname, "a")
        log.write("\nyou: " + msg1)
        log.close()
    out.append()

    out.append("ChatGPT generates a response...")

    out.append()

    messages.append({"role": "user", "content": msg1})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )
    chat_response = completion.choices[0].message.content

    out.append("ChatGPT: " + completion.choices[0].message.content)
    if turnonlogs == "1":
        log = open(logname, "a")
        log.write("\nChatGPT: " + completion.choices[0].message.content)
        log.close()
    out.append()

    messages.append({"role": "assistant", "content": chat_response})
main()
