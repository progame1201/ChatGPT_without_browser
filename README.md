# ChatGPT_without_browser
makes it possible to use chatgpt in the console

# where can it be run?
wherever python is supported. Needs modules: openai, pywebio.

# how to use it?
you can download an exe file with which you can use ChatGPT through my API keys, you can also download a python file that will not have my API keys, but you can use your API keys

# how it works?

very easy, you need to download the module openai and import it. Next you need to put the API key in a variable 

```py
openai.api_key = API
```

also you need to make a list type variable

```py
messages = []
```

next, you need to add the user's message to the list

```py
messages.append({"role": "user", "content": msg1})
```

next, create a request to chatgpt

```py
completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )
```
saving the chatgpt response to a variable
```py
chat_response = completion.choices[0].message.content
messages.append({"role": "assistant", "content": chat_response})
```
good luck in coding!

using the gpt-3.5-turbo model from OpenAI https://openai.com/
