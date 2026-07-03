from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

response = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it"
        },
        {
            "role": "user",
            "content": "The earliest successful AI program was written in 1951 by Christopher Strachey, later director of the Programming Research Group at the University of Oxford. Strachey's checkers (draughts) program ran on the Ferranti Mark I computer at the University of Manchester, England. The program was able to play a complete game of checkers at a reasonable speed. The Mark I computer was one of the first computers to be built in the world, and its development marked the beginning of the modern computing era."
        }
    ],
    temperature=0.5,
)

print(response.choices[0].message.content)
