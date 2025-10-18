import google.generativeai as genai
from config import API_KEY

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-002")

chat = model.start_chat(history=[])

response1 = chat.send_message("Who is Elon Musk?")
print("Q1:",response1.text)

response2 = chat.send_message("What company does he own?")
print("Q2:",response2.text)

response3 = chat.send_message("What I am refering by he?")
print("Q3:",response3.text)