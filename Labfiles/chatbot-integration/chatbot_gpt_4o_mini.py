import os
from dotenv import load_dotenv
from openai import AzureOpenAI


def chat_gpt4o_mini(input_text) :

    load_dotenv()
    azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
    azure_oai_key = os.getenv("AZURE_OAI_KEY")
    azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
    
    client = AzureOpenAI(
        azure_endpoint=azure_oai_endpoint,
        api_key=azure_oai_key,
        api_version="2025-01-01-preview",
    )

    messages = [
        {
            "role" : "system",
            "content" : [
            {
                "type" : "text",
                "text" : "너는 사용자가 입력한 값에 대해서 설명해주고, 답변은 너무 길지않게 해"
            }
            ]
        }
    ]

    messages.append(
        {
            "role" : "user",
            "content" : [
            {
                "type" : "text",
                "text" : input_text

            }
            ]
        }
    )

    if len(messages) > 50 :
        messages = [messages[0]] + messages[-49:]
    
    completion = client.chat.completions.create(
        model=azure_oai_deployment,
        messages=messages,
        max_tokens=150,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )

    answer = completion.choices[0].message.content
    
    print("답변 : " + answer + "\n")

    messages.append(
        {
            "role" : "assistant",
            "content" : [
            {
                "type" : "text",
                "text" : answer

            }
            ]
        }
    )

    if len(messages) > 50 :
        messages = [messages[0]] + messages[-49:]
