##

To query the OpenAI API, we call the `Completion.create` function and store its return value in the variable `response`.

```python-hide-clipboard
response = openai.Completion.create(model="text-davinci-002", prompt=prompts)
```

We can see the `Completion.create` function takes a `model` keyword argument and a prompt keyword argument. The `prompt` keyword argument is the variable which we use to store the prompt we are going to pass to the GPT-3 model. 

Now let's tackle, the `model` keyword argument. When OpenAI defines GPT-3, it defines it as a set of models that can understand and generate natural language. GPT-3 offers four main models suitable for different tasks. For example, the `ada` model is the fastest, whereas the `davinci` model we used earlier is the most capable.


| Model            | Description                                                                                                                                         | Max Request | Training Data   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------------|
| **text-davinci-002** | Most capable GPT-3 model. Can do the task of the other models, often with less context. Contains the most recent training data. Additionally, this model is capable of inserting completions within a text. | 4000 tokens | up to June 2021 |
| **text-curie-001**   | Faster and lower cost than the `davinci` model, but it is less capable.                                                                                                 | 2048 tokens | Up to Oct 2019  |
| **text-babbage-001**| Works best with straightforward tasks only. It is fast and low cost when compared to the previous two models.                                                                                                        | 2048 tokens | Up to Oct 2019  |
| **text-ada-001**     | Lowest cost and fastest model. You get the best results with `ada` when the tasks are straightforward.                                                                                           | 2048 tokens | Up to Oct 2019  |

OpenAI plans to continuously improve their models over time. `davinci` is generally the most capable model. `curie` can perform many of the same tasks as `davinci` but faster with a reduced cost. As we continue to experiment with GPT-3, we will use the `davinci` model since it yields the best results. Once things are working, we can try different models to see how the results differ. 

Add the following code to the IDE. Make sure to delete the previous `prompt`,`response` and `print` statements. We should only have our libraries and our key left.  We are going to have different variables representing the responses from each of the models in the table above. The code then prints each response so we can compare and contrast how each model responds to the same prompt.

```python
prompts = 'tagline for ice cream shop'
response1 = openai.Completion.create(model="text-davinci-002", prompt=prompts)
response2 = openai.Completion.create(model="text-curie-001", prompt=prompts)
response3 = openai.Completion.create(model="text-babbage-001", prompt=prompts)
response4 = openai.Completion.create(model="text-ada-001", prompt=prompts)

print('davinci-002')
print('-----------')
print(response1['choices'][0]['text'].strip(), '\n')

print('curie-001')
print('---------')
print(response2['choices'][0]['text'].strip(), '\n')

print('babbage-001')
print('-----------')
print(response3['choices'][0]['text'].strip(), '\n')

print('ada-001')
print('-------')
print(response4['choices'][0]['text'].strip(), '\n')
```

{Try it!}(python3 temp.py 1)

Whereas responses between `curie` and `davinci` are pretty close, we can see a clear difference between the `ada` model and the `davinci` model. Use this [tool](https://gpttools.com/comparisontool) to generate more comparisons if you want to experiment further.

{Check It!|assessment}(fill-in-the-blanks-1669896248)
