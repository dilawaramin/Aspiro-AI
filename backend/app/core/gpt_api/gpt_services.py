import os
import openai 
from dotenv import load_dotenv
from gpt_utils import store_message_json



# Load the API key from the environment
load_dotenv()
MY_TEST_API_KEY = os.getenv("MY_TEST_API_KEY")

# set API key for OpenAI library, and model
openai.api_key = MY_TEST_API_KEY
MODEL = "gpt-4o-mini-2024-07-18"



def create_gpt_message(userName, model=MODEL, max_tokens=100):
    """ 
    Placeholder prompt function for GPT API
    
    :param userName: str: name of the user, to differentiate
    :param model: str: model name to use
    :param max_tokens: int: maximum number of tokens to generate
    :return: str: response from the model
    """
    try:
        response = openai.chat.completions.create(
            model = model,
            max_completion_tokens = max_tokens,
            temperature = 0.6,
            messages=[
                {
                    "role": "system",
                    "content": "."
                },
                {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": "Give me a 50 word motivational text message"
                        },
                    ]
                }   
            ],
        )
        print(response)
        
        return response
    
    except Exception as e:
        print(e)
        return f"Error: {e}"
    

    
    
# testing
if __name__ == "__main__":
    response = create_gpt_message("Test User")
    
    store_message_json(response)