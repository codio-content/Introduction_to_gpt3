##

**GPT-3** is a transformer-based NLP model that performs a range of tasks such as translation, question-answering, and tasks that require reasoning.

Now let us try using GPT-3 in order to try out different prompts with our Python code. We are going to put our different prompts inside the string `prompts`. 

```python-hide-clipboard
prompts =""
## FREEZE CODE BEGIN
# This code queries the OpenAI API using the
# provided prompt and prints the result
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts)

print(response['choices'][0]['text'].strip())
## FREEZE CODE END
```

Let's first look at how GPT-3 handles prompts in which the model has to translate a word or words. Copy and paste the new value of `prompts` into the IDE and click the `TRY IT` button to see the result.

|||challenge
## Try these variations:

* Change the value of `prompts` to:

```python
prompts = 'Translate "my name is Jeff" in french'
```
{Try it!}(python3 test.py 1)

* Change the value of `prompts` to:
```python
prompts = 'how do you say car in lebanese?'
```

{Try it!}(python3 test.py 2)

* Change the value of `prompts` to:

```python
prompts = 'jueves in spanish means'
```

{Try it!}(python3 test.py 3)

|||

Now, we are going to look at how GPT-3 answers questions. Notice how the sentences do not have to be grammatically correct in order for the model to understand them. Copy and paste the new value of `prompts` into the IDE and click the `TRY IT` button to see the result.

|||challenge
## Try these variations:

* Change the value of `prompts` to:

```python
prompts = 'what is the capital of canada ?'
```

{Try it!}(python3 test.py 4)

* Change the value of `prompts` to:

```python
prompts = 'closest planet to the sun?'
```

{Try it!}(python3 test.py 5)

* Change the value of `prompts` to:

```python
prompts = 'who is the president of the us'
```

{Try it!}(python3 test.py 6)

|||

On the one hand, the above questions are not that difficult. You could argue that all the model has to do is "look up" the correct answer. Let's see how GPT-3 handles questions that require a bit of reasoning. Copy and paste the new value of `prompts` into the IDE and click the `TRY IT` button to see the result.

|||challenge
## Try these variations:

* Change the value of `prompts` to:

```python
prompts = 'Correct this to standard English: She no went to the movies'
```

{Try it!}(python3 test.py 7)

* Change the value of `prompts` to:

```python
prompts = 'Create an analogy for this phrase: life is like a highway'
```

{Try it!}(python3 test.py 8)

* Change the value of `prompts` to:

```python
prompts = 'Write a tagline for an ice cream shop'
```

{Try it!}(python3 test.py 9)

|||

{Check It!|assessment}(multiple-choice-3185264561)
