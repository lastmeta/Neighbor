import requests

url = "http://localhost:5000"
payload = [
    {"length": 10, "quantity": 1},
    {"length": 20, "quantity": 2},
    {"length": 25, "quantity": 1}
]

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:")
print(response.json())
