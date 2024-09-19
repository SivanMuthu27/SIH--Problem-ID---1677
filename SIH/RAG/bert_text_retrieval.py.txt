from transformers import BertTokenizer, BertModel
import torch
import faiss
import numpy as np

# Load the BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
bert_model = BertModel.from_pretrained("bert-base-uncased")

def encode_texts(texts, tokenizer, model):
    encoded_inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**encoded_inputs)
    # Use the mean of token embeddings as the sentence embedding
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.numpy()

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def generate_response(query, tokenizer, model, index, contexts, k=3):
    # Encode the query
    query_embedding = encode_texts([query], tokenizer, model)

    # Retrieve top-k contexts
    distances, indices = index.search(query_embedding, k)
    retrieved_contexts = [contexts[i] for i in indices[0]]

    # Return retrieved contexts
    return retrieved_contexts

# Sample contexts and query
contexts = [
    "In recent months, the Indian financial sector has experienced several cyber incidents, including ransomware attacks targeting banks.",
    "Phishing schemes aimed at financial institutions have increased. CERT-IN frequently issues alerts regarding these issues.",
    "Other significant incidents include data breaches affecting customer information and various types of malware targeting financial systems."
]
query = "What are recent significant cyber incidents in the Indian financial sector?"

# Encode contexts and build the FAISS index
context_embeddings = encode_texts(contexts, tokenizer, bert_model)
index = create_faiss_index(context_embeddings)

# Generate and print retrieved contexts
retrieved_contexts = generate_response(query, tokenizer, bert_model, index, contexts)
print(retrieved_contexts)
