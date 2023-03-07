import requests


data = requests.post(f"http://127.0.0.1:5000/adverts/", json={
    "title": "New large thick-walled cauldron",
    "description": "Excellent high-quality cast aluminum cauldron. For gas and electric stoves.",
    "owner": "Igor"
})
print(data.status_code)
print(data.json())

# data = requests.get(f"http://127.0.0.1:5000/adverts/1/")
# print(data.status_code)
# print(data.json())
#
# data = requests.delete(f"http://127.0.0.1:5000/adverts/1/")
# print(data.status_code)
# print(data.json())
