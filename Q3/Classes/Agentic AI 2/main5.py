import google.generativeai as genai
from config import API_KEY

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-002")

# Normal answer (no reasoning)
resp1 = model.generate_content("If Ali has 3 apples and buys 2 more, how many apples does he have?")
print("Normal Answer:\n", resp1.text, "\n")

# Chain of Thought answer (step-by-step reasoning)
resp2 = model.generate_content(
    "Think step by step before answering: "
    "If Ali has 3 apples and buys 2 more, how many apples does he have?"
)
print("Chain of Thought Answer:\n", resp2.text)
