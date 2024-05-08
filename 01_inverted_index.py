import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
#nltk.download('stopwords')

# Define the documents
document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

# Tokenize the documents and convert to lowercase
tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

# Get unique terms from both documents
terms = set(tokens1 + tokens2)

# Initialize data structures
inverted_index = {}
occurrences_doc1 = {}
occurrences_doc2 = {}

# Count term occurrences in each document
for term in terms:
    # Initialize empty list for documents containing the term
    documents = []
    
    # Check if term is in document 1
    if term in tokens1:
        documents.append("Document 1")
        occ_num_doc1 = tokens1.count(term)
        occurrences_doc1[term] = occ_num_doc1
        

    # Check if term is in document 2
    if term in tokens2:
        documents.append("Document 2")
        occ_num_doc2 = tokens2.count(term)
        occurrences_doc2[term] = occ_num_doc2
    
    
    # Update the inverted index with the term and documents list
    inverted_index[term] = documents

# Print the inverted index
for term, documents in inverted_index.items():
    print(f"{term} ->", end=" ")
    for doc in documents:
        if doc == "Document 1":
            count = occurrences_doc1.get(term, 0)
        else:
            count = occurrences_doc2.get(term, 0)
        print(f"{doc} ({count}),", end=" ")
    print()  