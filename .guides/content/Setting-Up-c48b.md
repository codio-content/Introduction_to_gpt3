
```python 
print(response['choices'][0]['text'].strip()) 
```

{Try it!}(python3 temp.py 1)

Because we did not send a prompt to OpenAI, the response is random. Run your code a few more times to see different output.

|||challenge
## Try this variation:
----
Change the print statement so that it prints the entire response from the OpenAI API.

```python
print(response)
```

{Try it!}(python3 temp.py 2)

|||

{Check It!|assessment}(multiple-choice-3200171246)
