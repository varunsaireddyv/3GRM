import requests

base="http://127.0.0.1:5000/"

userquery=input()

response=requests.get(base + userquery)
print(response.json())