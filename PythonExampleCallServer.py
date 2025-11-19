import requests

url = "http://localhost:5000/metta"
headers = {"Content-Type": "text/plain"}
data = "!(+ 1 1)"

response = requests.post(url, headers=headers, data=data)

print("Status:", response.status_code)
print("Response:", response.text)
