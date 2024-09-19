import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_incidents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    incidents = []
    for incident in soup.select('div.incident'):  # Adjust selectors as needed
        title = incident.select_one('a').get_text(strip=True)
        date = incident.select_one('span.date').get_text(strip=True)
        description = incident.select_one('p').get_text(strip=True)
        incidents.append({
            'title': title,
            'date': date,
            'description': description,
            'source_url': url
        })

    return incidents

# Example URL (replace with actual URLs)
url = 'https://example.com'
incident_data = fetch_incidents(url)

# Convert to DataFrame
df = pd.DataFrame(incident_data)
df.head()
