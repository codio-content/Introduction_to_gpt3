## OpenAI

Before we can get started using the GPT-3 model, we need to have an account with OpenAI. Use [this link](https://auth0.openai.com/u/signup/identifier?state=hKFo2SB4YXJldDFqR2NNbzFtRHJSbmtfZDRWRXhaeWNMRWR3c6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFNoeXBMcjJ6TGZQSzdRYnZjODF6YkhCSkFQMG41ZndFo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q) to create an account. OpenAI will ask you a few questions along the way.

Once your account has been created, you need to find your API key. This allows you to connect to the OpenAI API and make use of the GPT-3 model. Click on your profile picture in the top-right corner. Then click on "View API keys".

)


![The image depicts the list of options once you click on your profile picture in OpenAI. There is a red box around the choice "View API keys".](.guides/img/find-api-keys.png)

Next, click the link that reveals your API key if you want to see it. Otherwise, copy the API key for use later. **Important** you should not share your API key with anyone.

![The image depicts a portion of the webpage that has your API key. There is a red box around the link to reveal the API key.](.guides/img/reveal-api-key.png)

## CODIO

Now that our OpenAI account is set up and we have copied our API key, we are ready to prepare our coding environment. We are going to store our API key as an environment variable. This is going to allow us not to have to copy and paste our variable everywhere. Environment variables are useful when you want to avoid hard-coding access credentials or other variables into code.

The code on the left is going to be how we pull our environmental variables. In order to create our environmental variable we are going to click on the Codio tab on the top left. Inside the Preferences tab, click on the Environment Variables button. 

![The image depicts a portion of the webpage. It shows the content of the Codio tab. There is a red box around the link preferences at the bottom of the Codio tab.](.guides/img/prefer.png)

You should get to a page where similar to a dictionary you can create key-value pair. In the key area, name your key `OPENAI_KEY` and paste your OpenAI key in the value section. 



<img src=".guides/img/envVariable.png" alt="The picture shows the webpage associated with environmental variables. The image shows a location with a key box and value box." width="600" height="150">


From there we can press the **SAVE** button on the bottom left. Then we can restart our Codio box, to make sure the environmental is saved and stored. To restart, press the Project tab next to the Codio drop-down then click on the Restart box. 


![The image depicts a portion of the webpage. In the drop down "Restart Box" is highlighted.](.guides/img/reset.png)


||| 
Note that using `getenv()` or the `get()` method on a dictionary key will return None if the key does not exist. 
Try to `print` the key. 
```python
print(api_key)
```

|||
To execute commands at different checkpoints, a `Try It` button will be provided. In order to run the `print` statement from earlier click the `try it` button below, which will run the code for you and display the response.
{Try it!}(python3 secret.py)

If the following prints your key without quotation you are clear. If it is printed with quotations, please go back to the Environment Variable tabs and remove them. If you get `None`, try checking if you named the API key the right way. Delete the print statement when you are done. We don't want it to keep printing when we use other commands.
