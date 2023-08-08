##

|||
**Large language models** (LLMs) are machine learning algorithms that can recognize, summarize, translate, predict, and generate human languages on the basis of very large text-based datasets. 
|||

## Pre-Trained Models

The building and training of models are both complex and resource intensive. Luckily, there are **pre-trained language models**.

A couple of factors to consider when choosing a pre-trained language model:
1. What task are you using it for?
1. What are the technical requirements to use the model?

###  What task are you using it for?
The best place to start is to find a purpose-specific model. Pre-trained models often have descriptions which include what the pre-trained models are best for. If you cannot find a model that is specific to your task or your task is ill-defined you can use a more general purpose model.

### What are the technical requirements to use the model?
While some technical requirements are easier to meet such as libraries like PyTorch or TensorFlow, using even a pre-trained model can be resource intensive. In some cases, a minimum RAM is specified or even the use of a GPU, however even meeting the minimum hardware requirements could result in very slow results.

## Popular Pre-Trained Models
There are hundreds of pre-trained language models that can be used. This course will focus on a well-known and very powerful model **GPT-3**.


### OpenAI’s GPT-3

GPT-3 is a transformer-based NLP model that performs a range of tasks such as translation, question-answering, and tasks that require reasoning such as unscrambling words.

It is trained on over 175 billion parameters on 45 TB of text from all over the internet, making it one of the biggest pre-trained NLP models available. What differentiates GPT-3 from other language models is it does not require fine-tuning to perform downstream tasks, developers are allowed to reprogram the model using instructions.

{Check It!|assessment}(multiple-choice-513414473)
