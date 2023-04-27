import openai

openai.api_key = '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'

messages = []
while True:
  content = input("User: ")
  messages.append({"role":"user", "content":content})
  # messages.append({"role":"system", "content":"너는 어린 아이들을 위한 학습용 챗봇이야. 아이들이 학습 이외의 말을 하면 학습용 프로그램임을 알려줘"})
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages
  )
  
  chat_response = completion.choices[0].message.content 
  print(f"ChatGPT: {chat_response}")
  messages.append({"role":"assistant", "content":chat_response})
  