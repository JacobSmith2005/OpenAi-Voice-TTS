import openai
import dotenv, os

dotenv.main.load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.environ['API_KEY']

question = input("wuz ur question?")

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "Your are a helpful assistant."},
        {"role": "user", "content": question},
    ])

message = response.choices[0]['message']
# print("{}: {}".format(message['role'], message['content']))
print(message['content'])
