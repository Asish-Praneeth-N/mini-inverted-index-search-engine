import os
from index import load_documents, build_inverted_index
from tfidf import compute_tfidf_scores

def main():
    print("Mini Inverted Index Search Engine")
    print("=================================")
    
    doc_folder = "documents"
    print(f"Loading documents from '{doc_folder}'...")
    documents = load_documents(doc_folder)
    
    if not documents:
        print("No documents found. Exiting.")
        return

    print(f"Loaded {len(documents)} documents.")
    
    print("Building inverted index...")
    inverted_index = build_inverted_index(documents)
    print("Index built successfully.")
    
    while True:
        print("\n" + "-"*30)
        query = input("Enter search query (or 'exit' to quit): ").strip()
        
        if query.lower() == 'exit':
            break
            
        if not query:
            continue
            
        print(f"Searching for: '{query}'")
        
        # 1. Retrieve relevant documents using Inverted Index (Optional optimization)
        # In a real system, we would only score documents that contain at least one query term.
        # For this mini project, we can score all documents, but let's show how we *could* use the index.
        # relevant_docs = set()
        # for token in tokenize(query):
        #     if token in inverted_index:
        #         relevant_docs.update(inverted_index[token])
        
        # 2. Rank documents using TF-IDF
        scores = compute_tfidf_scores(documents, query)
        
        # Sort by score descending
        ranked_results = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        
        print("\nResults:")
        found = False
        for doc_name, score in ranked_results:
            if score > 0:
                print(f"{doc_name}: {score:.4f}")
                found = True
        
        if not found:
            print("No matching documents found.")

if __name__ == "__main__":
    main()
