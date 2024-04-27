import os
from openai import OpenAI

# Define the model to use
model = "gpt-3.5-turbo"

# Define the client
client = OpenAI(api_key=os.environ["OPENAI"])

# A helper function to return response for a prompt
def get_completion(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=100):
    response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

# Create a list of conversation to feed to GPT
conversation = [
    {"role": "system",
     "content": """Act as a Parisian travel expert. Give concise and friendly answer. You should only answer in English.\
   You should only answer to questions related to travelling in Paris, and nothing else.\
   Always ask a follow-up question at the end of your answer by asking what else the user wants to ask.\
   If the user says they want to quit using this service, say 'E_X_I_T', without the quotation marks, and nothing else.
   """}
]
num_loops = 0
flag = True
while flag == True:
    # First question with a welcome message
    if num_loops == 0:
        user_input = input(
            "Welcome to Peterman Reality Tours AI assistant. How can I help?\n")
        conversation.append({"role": "user", "content": user_input})
        answer = get_completion(conversation)
        conversation.append({"role": "assistant", "content": answer})
        num_loops += 1

        if answer == "E_X_I_T":
            flag = False
            print("Ok! Have a great trip. See ya!")

    # Non-first question without a welcome message

    user_input = input(f'{answer}\n')
    conversation.append({"role": "user", "content": user_input})
    answer = get_completion(conversation)
    conversation.append({"role": "assistant", "content": answer})
    
    if answer == "E_X_I_T":
        flag = False
        print("Ok! Have a great trip. See ya!")
