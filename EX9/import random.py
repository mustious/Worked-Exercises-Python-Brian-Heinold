import requests
url1 = "https://us-central1-gifted-dreamer-311213.cloudfunctions.net/compeng-bot-web"
url2 = "https://us-central1-gifted-dreamer-311213.cloudfunctions.net/function-test"

params = {"text": "hello",
"project_id": "gifted-dreamer-311213",
"lang": "en-US"
}
r = requests.post(url=url1, data=params)
print("Compeng-bot-web response:\n{}".format(r.text))

r = requests.post(url=url2, data=params)
print("function-test response:\n{}".format(r.text))