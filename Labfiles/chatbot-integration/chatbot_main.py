import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from chatbot_gpt_4o_mini import chat_gpt4o_mini

def chatbot_integration(): 
        
    try: 
        while True:

            print('반갑습니다! chatbot_integration에 오신 걸 환영합니다! 원하시는 기능을 선택해주세요!')
            print('-------------------------------------------')


            input_text = input("질문을 입력하세요 ('quit' 이라고 입력하면 종료): ")
            
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("질문을 다시 작성해주세요.")
                continue

            # print("질문 : " + input_text)

            gpt4o = chat_gpt4o_mini(input_text)
            

    except Exception as ex:
        print(ex)


if __name__ == '__main__': 
    chatbot_integration()