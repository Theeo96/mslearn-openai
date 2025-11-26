import gradio as gr

# 각 기능별로 나중에 연결할 함수들 (일단 더미로 만들어놓음)
def voice_recognition(audio):
    return "음성 인식 결과: (여기에 Whisper 등 연결)"

def image_analysis(image):
    return "이미지 분석 결과: 고양이 한 마리가 앉아있네요 😺"

def image_generation(prompt):
    return "생성된 이미지"  # 여기엔 DALL-E나 Stable Diffusion 연결

def chat_with_bot(message, history):
    return f"당신: {message}\n봇: 아직 기능 선택 안 하셨네요! 위 버튼을 눌러보세요~"

# Gradio 인터페이스 만들기
with gr.Blocks(title="멀티모달 챗봇") as demo:
    gr.Markdown("# 반갑습니다! chatbot_integration에 오신 걸 환영합니다!")
    gr.Markdown("### 원하시는 기능을 선택해주세요!")
    
    with gr.Row():
        voice_btn = gr.Button("음성 인식 기능", variant="primary")
        analyze_btn = gr.Button("이미지 분석 기능", variant="secondary")
        generate_btn = gr.Button("이미지 생성 기능", variant="secondary")
    
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(label="메시지를 입력하세요", placeholder="여기에 입력 후 엔터!")
    
    # 버튼 클릭 → 기능 실행
    voice_btn.click(
        fn=voice_recognition,
        inputs=gr.Audio(sources="microphone", type="filepath", label="마이크로 말하세요!", ),
        outputs=chatbot
    )
    
    analyze_btn.click(
        fn=image_analysis,
        inputs=gr.Image(type="pil", label="분석할 이미지를 업로드하세요"),
        outputs=chatbot
    )
    
    generate_btn.click(
        fn=image_generation,
        inputs=gr.Textbox(label="생성할 이미지 설명을 입력하세요", placeholder="예: 우주를 나는 고양이"),
        outputs=gr.Image(label="생성된 이미지")
    )
    
    # 일반 채팅도 되게
    msg.submit(chat_with_bot, [msg, chatbot], chatbot)

# 실행!
demo.launch(share=True)  # share=True 하면 외부 링크도 줌 (카톡으로 바로 공유 가능!)