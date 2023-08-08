#CODIO SOLUTION BEGIN
import os 
import openai

import secret
openai.api_key=secret.api_key
prompts = ''
response = openai.Completion.create(model="text-davinci-002", prompt=prompts)
print(response['choices'][0]['text'].strip()) 
#CODIO SOLUTION END
