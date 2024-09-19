import requests

url = 'https://www.cvedetails.com/vulnerability-list.php'
response = requests.get(url)
print(response.status_code)  # Should be 200 if the request is successful
print(response.text[:1000])  # Print the first 1000 characters of the HTML response

