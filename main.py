from litellm import completion
from dotenv import load_dotenv

# Load environment variables from .env (make sure your OpenAI API key is in there)
load_dotenv()

# Send a message to the model
response = completion(
    model="openai/gpt-4o",
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)

# Print the whole response to see its structure
print(response.choices[0].message.content)


