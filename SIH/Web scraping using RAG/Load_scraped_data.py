import pandas as pd

# Load scraped data
data = pd.read_json('cyber_incidents.json')
data.head()
