import os
import openai
import secret
openai.api_key=secret.api_key


prompts =""
# FREEZE CODE BEGIN
# This code queries the OpenAI API using the provided prompt and prints the result
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts)

print(response['choices'][0]['text'].strip())
# FREEZE CODE END