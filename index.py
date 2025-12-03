import os
import string

def load_documents(doc_folder):
    """
    Reads all .txt files from the documents folder.
    Returns a dictionary: { "doc_name": "file content..." }
    """
    documents = {}
    if not os.path.exists(doc_folder):
        print(f"Error: Folder '{doc_folder}' not found.")
        return documents

    for filename in os.listdir(doc_folder):
        if filename.endswith(".txt"):
            path = os.path.join(doc_folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                documents[filename] = f.read()
    return documents

def tokenize(text):
    """
    Splits text into words, removes punctuation, and converts to lowercase.
    """
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return tokens

def build_inverted_index(documents):
    """
    Builds an inverted index from the documents dictionary.
    Returns: { "token": ["doc1.txt", "doc3.txt", ...] }
    """
    inverted_index = {}
    
    for doc_name, content in documents.items():
        tokens = tokenize(content)
        for token in tokens:
            if token not in inverted_index:
                inverted_index[token] = []
            # Avoid duplicate document entries for the same token
            if doc_name not in inverted_index[token]:
                inverted_index[token].append(doc_name)
                
    return inverted_index

if __name__ == "__main__":
    # Test the indexing
    docs = load_documents("documents")
    index = build_inverted_index(docs)
    import pprint
    pprint.pprint(index)
