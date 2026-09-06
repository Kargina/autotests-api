import httpx

# Login data
login_payload = {
    "email": "1@example.com",
    "password": "string",
}

# Authentication
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']

# Get my data
headers = {
    "Authorization": f"Bearer {access_token}"
}
me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)
me_response_data = me_response.json()
print("Me response:", me_response_data)
print("Status code:", me_response.status_code)
