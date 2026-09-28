
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key= os.getenv("GROQ_API_KEY")

print("API key loaded:",api_key is not None)

client = Groq(api_key = api_key)

print("AI Chatbot started!")
print("Type 'exit' to stop.\n")

while True:
    user_message = input("you: ")
    if user_message.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "system", "content": "you are a helpful and friendly AI assistant."}, {"role": "user", "content": user_message}],
        max_tokens=150
    )
    print("Bot:", response.choices[0].message.content)
        
        