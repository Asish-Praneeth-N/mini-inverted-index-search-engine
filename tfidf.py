import math
from index import tokenize

def compute_tf(document_content):
    """
    Computes Term Frequency (TF) for a single document.
    TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)
    """
    tokens = tokenize(document_content)
    total_terms = len(tokens)
    tf_dict = {}
    
    if total_terms == 0:
        return tf_dict

    for token in tokens:
        tf_dict[token] = tf_dict.get(token, 0) + 1
        
    for token in tf_dict:
        tf_dict[token] = tf_dict[token] / total_terms
        
    return tf_dict

def compute_idf(documents):
    """
    Computes Inverse Document Frequency (IDF) for all terms in the corpus.
    IDF(t) = log_10(Total number of documents / Number of documents with term t)
    """
    total_documents = len(documents)
    idf_dict = {}
    
    # Count in how many documents each term appears
    term_document_count = {}
    
    for content in documents.values():
        tokens = set(tokenize(content)) # Use set to count each term only once per document
        for token in tokens:
            term_document_count[token] = term_document_count.get(token, 0) + 1
            
    for term, count in term_document_count.items():
        idf_dict[term] = math.log10(total_documents / count)
        
    return idf_dict

def compute_tfidf_scores(documents, query):
    """
    Computes TF-IDF scores for a query against all documents.
    Returns a dictionary: { "doc_name": score }
    """
    query_tokens = tokenize(query)
    scores = {}
    
    # Precompute IDF for the whole corpus
    idf_dict = compute_idf(documents)
    
    for doc_name, content in documents.items():
        tf_dict = compute_tf(content)
        score = 0.0
        
        for token in query_tokens:
            if token in tf_dict and token in idf_dict:
                score += tf_dict[token] * idf_dict[token]
                
        scores[doc_name] = score
        
    return scores
