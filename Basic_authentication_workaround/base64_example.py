import requests

# URL of the endpoint you want to send the request to
url = 'https://example.com/api/endpoint'

# Data to be sent in the request body (if any)
data = {'key': 'value'}

# Headers to be sent with the request, including the Authorization header
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Content-Type': 'application/json'  # Example content type
}

# Make a POST request with the specified URL, data, and headers
response = requests.post(url, json=data, headers=headers)

# Print the response from the server
print(response.text)
