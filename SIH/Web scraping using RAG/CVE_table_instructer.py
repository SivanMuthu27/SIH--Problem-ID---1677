from bs4 import BeautifulSoup
import requests

# Make the request
url = 'https://www.cvedetails.com/vulnerability-list.php'
response = requests.get(url, headers=headers)

# Parse the content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first table element
table = soup.find('table')
print(table)  # Inspect this output to see if the table is found
