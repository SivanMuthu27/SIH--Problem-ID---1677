from transformers import RagTokenizer, RagSequenceForGeneration
import torch
import faiss
import numpy as np
from transformers import BertTokenizer, BertModel

# Load the BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
bert_model = BertModel.from_pretrained("bert-base-uncased")

# Load RAG model and tokenizer
rag_tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-base")
rag_model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-base")

def encode_texts(texts, tokenizer, model):
    encoded_inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
    with torch.no_grad():
        outputs = model(**encoded_inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.numpy()

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def generate_response(query, tokenizer, model, index, contexts, k=3):
    query_embedding = encode_texts([query], tokenizer, model)
    distances, indices = index.search(query_embedding, k)
    retrieved_contexts = [contexts[i] for i in indices[0]]
    return retrieved_contexts

def encode_rag_inputs(query, contexts, rag_tokenizer):
    query_input = rag_tokenizer(query, return_tensors="pt", truncation=True, padding=True, max_length=512)
    context_inputs = rag_tokenizer(contexts, return_tensors="pt", padding=True, truncation=True, max_length=512)
    return query_input, context_inputs

def generate_rag_response(query, retrieved_contexts, rag_tokenizer, rag_model):
    query_inputs, context_inputs = encode_rag_inputs(query, retrieved_contexts, rag_tokenizer)
    with torch.no_grad():
        outputs = rag_model.generate(
            input_ids=query_inputs['input_ids'],
            attention_mask=query_inputs['attention_mask'],
            context_input_ids=context_inputs['input_ids'],
            context_attention_mask=context_inputs['attention_mask']
        )
    return rag_tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

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
print("Retrieved Contexts:")
print(retrieved_contexts)

# Generate and print RAG response
rag_response = generate_rag_response(query, retrieved_contexts, rag_tokenizer, rag_model)
print("\nRAG Response:")
print(rag_response)
