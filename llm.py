# import os module so that we can read environment variables
import os

# import load_dotenv so that variables from the .env file are loaded
from dotenv import load_dotenv

# import Groq client used to communicate with Groq API
from groq import Groq

# load .env variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# create Groq client using API key
client = Groq(api_key=api_key)

def generate_answer(question):

    # send requrest to Groq API
    response = client.chat.completions.create(

        # provide the conversation message to the model
        messages=[

            #tell the model that this message is from user
            {
                "role": "user",

                #Given the model the question we want to answer
                "content": "What is Zoho"
            }
        ],
        # specify LLM model
            model = "openai/gpt-oss-20b",
    )

    # extract generated text from the API response
    answer = response.choices[0].message.content

    return answer