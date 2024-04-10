import requests
response = requests.get("https://www.reddit.com/r/programming/about.json")
print(response.content)
print(response)
