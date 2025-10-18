from config import API_KEY
import google.generativeai as genai

# Configure Gemini with API Key
genai.configure(api_key=API_KEY)

# Function to ask with dynamic instruction
def ask_agent(query, instruction):
    model = genai.GenerativeModel("gemini-1.5-flash")
    final_prompt = f"{instruction}\nUser: {query}"
    response = model.generate_content(final_prompt)
    return response.text

# Example 1: Short answers
print(ask_agent("What is AI?", "Always reply in 2 short lines."))

# Example 2: Teacher mode
print(ask_agent("What is gravity?", "Explain like I am 10 years old."))

# Example 3: Urdu mode
print(ask_agent("What is a black hole?", "Answer only in simple Urdu."))
