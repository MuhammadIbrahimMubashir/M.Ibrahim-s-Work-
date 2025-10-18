import google.generativeai as genai
from config import API_KEY

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-002")

# top_k = 1 (very strict, same outputs)
resp1 = model.generate_content(
    "Write a poem about the ocean.",
    generation_config={"temperature": 1, "top_k": 1}
)

# top_k = 40 (more variety)
resp2 = model.generate_content(
    "Write a poem about the ocean.",
    generation_config={"temperature": 1, "top_k": 40}
)

# top_p = 0.3 (less creative, more safe)
resp3 = model.generate_content(
    "Write a poem about the ocean.",
    generation_config={"temperature": 1, "top_p": 0.3}
)

# top_p = 0.9 (more creative, open-ended)
resp4 = model.generate_content(
    "Write a poem about the ocean.",
    generation_config={"temperature": 1, "top_p": 0.9}
)

print("top_k=1:\n", resp1.text, "\n")
print("top_k=40:\n", resp2.text, "\n")
print("top_p=0.3:\n", resp3.text, "\n")
print("top_p=0.9:\n", resp4.text, "\n")