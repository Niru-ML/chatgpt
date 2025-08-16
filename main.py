import openai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# It's best practice to use environment variables for API keys for security.
# The openai library automatically looks for the OPENAI_API_KEY environment variable.
# You can set it in your terminal before running the script:
# On Linux/macOS: export OPENAI_API_KEY='your_api_key_here'
# On Windows CMD:   set OPENAI_API_KEY=your_api_key_here
# On PowerShell:    $env:OPENAI_API_KEY="your_api_key_here"
# Or, by using python-dotenv, it will be loaded from the .env file.

# This initializes the client, which will automatically use the environment variable.
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: The OPENAI_API_KEY environment variable was not found.")
    print("Please check the following:")
    print("1. You have a .env file in the same directory as this script.")
    print("2. The .env file contains: OPENAI_API_KEY='your_actual_api_key'")
    print("3. The python-dotenv library is installed (`pip install python-dotenv`).")
    exit()

client = openai.OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    try:
        # The syntax for the openai library (v1.0.0+) has changed.
        # Also, corrected a typo from 'resopnse' to 'response'.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except openai.APIError as e:
        # Handles API-specific errors
        return f"OpenAI API returned an error: {e}"
    except Exception as e:
        # Handles other potential errors (e.g., network issues)
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
