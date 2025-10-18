import google.generativeai as genai
from config import API_KEY

genai.configure(api_key = API_KEY)

#Tools
def multiply(a,b):
    return a * b

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

model = genai.GenerativeModel(
    "gemini-1.5-flash-002",
    tools=[multiply,add,sub],
)

chat = model.start_chat(enable_automatic_function_calling=True)

response1 = chat.send_message("What is 10 + 5?")

response2 = chat.send_message("What is 7 * 8?")

response3 = chat.send_message("What is 68 - 18?")

print("Answer:",response1)# to check if agent used
print("Answer:",response1.text)

print("Answer:",response2.text)

print("Answer:",response3)
