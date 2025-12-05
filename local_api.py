import requests

site = "http://127.0.0.1:8000"

# See if the FastAPI server is up and ready
r = requests.get(site)

print("Status Code:", r.status_code)
print("Welcome Message:", r.json()["message"])



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send data to API to get an inference
r = requests.post(url=f"{site}/model", json=data)

print("Status Code:", r.status_code)
print("Inference:", r.json()["result"])