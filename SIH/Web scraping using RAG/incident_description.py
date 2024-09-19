from transformers import pipeline

# Load pre-trained BERT model for summarization and entity extraction
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# Function to summarize the incident description
def summarize_description(description):
    summary = summarizer(description, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Apply summarization
data['summary'] = data['description'].apply(summarize_description)

# Entity recognition (APT groups, sector, etc.)
def extract_entities(description):
    entities = ner(description)
    return [(e['word'], e['entity']) for e in entities]

data['entities'] = data['description'].apply(extract_entities)

data.head()
