from index import load_documents, build_inverted_index
from tfidf import compute_tfidf_scores

def verify():
    print("Verifying Mini Inverted Index Search Engine...")
    
    # 1. Load Documents
    documents = load_documents("documents")
    print(f"Loaded {len(documents)} documents.")
    assert len(documents) == 3
    
    # 2. Build Index
    index = build_inverted_index(documents)
    print(f"Index contains {len(index)} terms.")
    assert "distributed" in index
    
    # 3. Search
    query = "distributed systems"
    print(f"Searching for: '{query}'")
    scores = compute_tfidf_scores(documents, query)
    
    ranked_results = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    
    print("\nResults:")
    for doc_name, score in ranked_results:
        if score > 0:
            print(f"{doc_name}: {score:.4f}")
            
    # Check if doc1 and doc2 are in the top results (they contain "distributed" or "systems")
    top_docs = [doc for doc, score in ranked_results if score > 0]
    assert "doc1.txt" in top_docs
    assert "doc2.txt" in top_docs
    
    print("\nVerification Successful!")

if __name__ == "__main__":
    verify()
