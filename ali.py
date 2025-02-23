from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Simple test to check if Ali is working
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are Ali, an AI built for aligned growth and marketing strategy."},
        {"role": "user", "content": "Hey Ali, how do we scale PTU globally with automation?"}
    ]
)

print(response.choices[0].message.content)