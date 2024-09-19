from transformers import RagTokenizer, RagSequenceForGeneration

# Load the tokenizer and model
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-base")

