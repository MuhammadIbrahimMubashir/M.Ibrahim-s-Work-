from config import API_KEY
import google.generativeai as genai

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-002")

prompt = """
You are solving a puzzle.
Think of at least 2 different possible approaches (like a tree of thoughts).
Then choose the best one and give the final answer.

Puzzle: A farmer has a boat. He must take a wolf, a goat, and a cabbage across the river.
The boat can only carry the farmer and one item at a time.
How can the farmer safely cross?
"""

resp = model.generate_content(prompt)

print(resp.text)
