import google.generativeai as genai
from config import API_KEY

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-002")

# Low temperature (deterministic)
response1 = model.generate_content(
    "Write a short story about a cat in space.",
    generation_config={"temperature": 0}
)

# High temperature (creative)
response2 = model.generate_content(
    "Write a short story about a cat in space.",
    generation_config={"temperature": 1}
)

print("Tempureture 0:",response1.text, "\n")
print("Tempurature 1:",response2.text)