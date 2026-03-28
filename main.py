import requests
import data

response = requests.post(
    data.BASE_URL + "/api/v1/users",
    json=data.user_body
)

print(response.status_code)
print(response.text)




