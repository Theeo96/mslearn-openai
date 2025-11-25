import os
from dotenv import load_dotenv

# Add Azure OpenAI package
from openai import AzureOpenAI

def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        
        # Initialize the Azure OpenAI client...
        client = AzureOpenAI(
        azure_endpoint=azure_oai_endpoint,
        api_key=azure_oai_key,
        api_version="2025-01-01-preview",
        )

        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")

            messages = [
                {
                    "role": "system",
                    "content": [
                    {
                        "type": "text",
                        "text": "너는 컴공과 선배이고, 현업에서 transformer 모델을 다루는 개발직군에 속해있어. 그래서 AI 관련 질문이 왔을 때, 현업에서 어떻게 사용되는지 등의 내용을 사례와 함께 설명해."
                    }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                    {
                        "type": "text",
                        "text": input_text
                    }
                    ]
                }
            ]
            
            # Add code to send request...
            completion = client.chat.completions.create(
            model=azure_oai_deployment,
            messages=messages,
            max_tokens=6553,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False
            )
            
            print(completion.choices[0].message.content)
            

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()