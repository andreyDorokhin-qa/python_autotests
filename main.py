import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json = {
  "id": 111,
  "category": {
    "id": 111,
    "name": "parrot"
  },
  "name": "parrot",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 111,
      "name": "parrot"
    }
  ],
  "status": "available"
})
print(response.text)
print(response.status_code)

response = requests.put("https://petstore.swagger.io/v2/pet", json = {
  "id": 111,
  "category": {
    "id": 111,
    "name": "parrot"
  },
  "name": "parrot",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 111,
      "name": "parrot"
    }
  ],
  "status": "available"
})
print(response.text)
print(response.status_code)

response = requests.get("https://petstore.swagger.io/v2/pet/111")
print(response.text)
print(response.status_code)