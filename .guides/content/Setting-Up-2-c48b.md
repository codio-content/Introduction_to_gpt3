
## Python

Now that our OpenAI account is set up and we have copied our API key, we are ready to prepare our coding environment. The first thing we need to do is install the `openai` package. In the terminal (bottom-left panel), copy and paste the command below. Press `ENTER` or `RETURN` on your keyboard to install the package.

```markdown
python3 -m pip install openai
```

Next, go to the Python file (top-left panel) and import the `os` module and the newly downloaded `openai` package.

```python
import os 
import openai
```

|||important

Now we need to put in our environment variable which is stored in our `secret.py` file. 

```python 
import secret
openai.api_key=secret.api_key
```
|||

Create the variable `prompts` which we will use to store the prompt we are going to pass to the GPT-3 model. The variable can be an empty string for now.

```python
prompts = ''
```

To query the OpenAI API, we are going to call the `Completion.create` method and store its return value in the variable `response`. We need to specify the model we are using as well as the prompt. This is done with the `model` and `prompt` keyword arguments.

```python
response = openai.Completion.create(model="text-davinci-002", prompt=prompts)
```

Finally, we want to print the output from the model. OpenAI returns a complex dictionary. The response we want is buried inside the dictionary. Use the following code to print your results.

```python 
print(response['choices'][0]['text'].strip()) 
```

{Try it!}(python3 temp.py 1)

Because we did not send a prompt to OpenAI, the response is random. Run your code a few more times to see different outputs.

|||challenge
## Try this variation:
----
Delete the previous `print` statement. Copy and paste the code below in order to print the entire response from the OpenAI API.

```python
print(response)
```

{Try it!}(python3 temp.py 2)

|||

{Check It!|assessment}(multiple-choice-3200171246)
