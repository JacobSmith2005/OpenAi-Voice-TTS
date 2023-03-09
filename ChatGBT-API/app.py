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

url = "https://api.uberduck.ai/speak"

payload = {
    "pace": 1,
    "speech": message
}
headers = {
    "accept": "application/json",
    "uberduck-id": "anonymous",
    "content-type": "application/json",
    "authorization": "Basic cHViX2xhc2doa2NncnRjb256Z2tybjpwa185OTkyZDY4YS1mNWI0LTQ1MjktYjMyNi04YTM2MjA2OGY3Mzg="
}

response = requests.post(url, json=payload, headers=headers)


url = "https://api.uberduck.ai/speak-status?uuid=5cfd8f2d-97a4-4e5b-8c1e-72f611896183"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
