# Mini Inverted Index Search Engine

A simplified search engine that demonstrates the core concepts behind Google Search and modern Information Retrieval (IR) systems. It allows users to perform keyword-based queries over a collection of text documents and returns ranked results using **TF-IDF scoring**.

## Features

* **Document Ingestion**: Reads text files from a directory.
* **Tokenization**: Cleans and splits text into tokens.
* **Inverted Index**: Builds a map of tokens to documents for fast lookup.
* **TF-IDF Scoring**: Ranks documents based on Term Frequency and Inverse Document Frequency.

## Project Structure

```
mini-search-engine/
│
├── index.py          # Builds the inverted index
├── tfidf.py          # Computes TF-IDF scores
├── search.py         # User query + ranking output
├── documents/        # Folder containing sample text files
│   ├── doc1.txt
│   ├── doc2.txt
│   └── doc3.txt
└── README.md
```

## How to Run

1.  Ensure you have Python installed.
2.  Navigate to the project directory.
3.  Run the search engine:

    ```bash
    python search.py
    ```

4.  Enter a search query when prompted (e.g., "distributed systems").
5.  Type `exit` to quit.

## Concepts

### Inverted Index
Maps each unique token to the list of documents that contain it. This allows the search engine to quickly find relevant documents without scanning every single file for every query.

### TF-IDF
*   **TF (Term Frequency)**: Measures how frequently a term appears in a document.
*   **IDF (Inverse Document Frequency)**: Measures how important a term is. Rare terms have high IDF, while common terms (like "the") have low IDF.
*   **Score**: TF * IDF. High scores indicate that the document is very relevant to the query.
"# mini-inverted-index-search-engine" 
