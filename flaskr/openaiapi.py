import openai
import os
key = os.environ.get('openaikey')
openai.api_key = key
messages = [{"role": "system", "content": "You are a helpful assistant."}]
models = ["gpt-3.5-turbo","gpt-4"]
current_model = models[0]

def define_system(new_system):
    messages[0] = {"role": "system", "content": new_system}

def completion(text):
    print("Using model: " + current_model)
    messages.append({"role": "user", "content": text})
    r = openai.ChatCompletion.create(
        model=current_model,
        messages=messages,
    )
    messages.append({"role": "assistant", "content": r['choices'][0]['message']['content']})
    print(messages)
    return r

def clear():
    messages[1:] = []

def change_version(new_model):
    global current_model 
    current_model = new_model
