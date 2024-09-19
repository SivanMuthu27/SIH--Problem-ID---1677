# Module 1: Setup
!apt-get update
!apt-get install -y wget unzip
!wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
!unzip chromedriver_linux64.zip
!mv chromedriver /usr/bin/chromedriver
!pip install selenium transformers plotly

# Module 2: Web Scraping
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to ChromeDriver
webdriver_service = Service('/usr/bin/chromedriver')

# Initialize WebDriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    # Fetch the page
    url = 'https://www.cvedetails.com/vulnerability-list.php'
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchresults')))

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the table element
    table = soup.find('table', {'class': 'searchresults'})
    if not table:
        raise Exception("Table not found. Check the structure or class name.")

    # Extract table data
    def extract_table_data(table):
        rows = table.find_all('tr')
        headers = [header.text.strip() for header in rows[0].find_all('th')]
        data = []
        for row in rows[1:]:
            cols = row.find_all('td')
            data_row = [col.text.strip() for col in cols]
            data.append(data_row)
        return headers, data

    headers, data = extract_table_data(table)
    df = pd.DataFrame(data, columns=headers)
    print(df.head())  # Display the first few rows of the DataFrame

finally:
    driver.quit()

# Module 3: Summarization
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Load RAG model and tokenizer
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")
retriever = RagRetriever.from_pretrained("facebook/rag-token-base")
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-base")

# Function to use RAG model
def generate_summary(text):
    inputs = tokenizer(text, return_tensors="pt")
    # Retrieve relevant documents
    doc_ids = retriever.retrieve(inputs["input_ids"], inputs["attention_mask"])
    # Generate summary
    outputs = model.generate(input_ids=inputs["input_ids"], context_input_ids=doc_ids)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

# Apply summarization to the 'Description' column
if 'Description' in df.columns:
    df['Summary'] = df['Description'].apply(generate_summary)
    print(df[['Description', 'Summary']].head())  # Display original and summarized descriptions
else:
    print("Column 'Description' not found in DataFrame.")

# Module 4: Visualization
import plotly.express as px

# Example: Number of incidents by severity (update based on actual columns)
if 'Severity' in df.columns:
    fig = px.bar(df, x='Severity', title='Number of Incidents by Severity')
    fig.show()
else:
    print("Column 'Severity' not found in DataFrame.")