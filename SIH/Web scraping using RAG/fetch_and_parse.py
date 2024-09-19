import requests
from bs4 import BeautifulSoup

# Adding a User-Agent header to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = 'https://www.cvedetails.com/vulnerability-list.php'
response = requests.get(url, headers=headers)
print(response.status_code)

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# Check for the table again
table = soup.find('table', {'class': 'searchresults'})
print(table)  # Ensure that this is not None
