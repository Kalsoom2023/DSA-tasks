import re
import math
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def preprocess_text(text):
    """
    Preprocess the text by lowercasing, removing special characters, 
    and tokenizing words.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    # Tokenize and remove stop words (basic implementation)
    stop_words = {"the", "and", "is", "in", "to", "a", "of", "for", "on", "it", "this"}
    words = [word for word in text.split() if word not in stop_words]
    return " ".join(words)
def calculate_similarity(doc1, doc2):
    """
    Calculate cosine similarity between two documents.
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([doc1, doc2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]
def highlight_plagiarism(original, compared, threshold=0.7):
    """
    Highlight plagiarized sections in the original text.
    """
    original_words = original.split()
    plagiarized_words = set()
    
    # Compare n-grams
    n = 3  # Use trigrams
    for i in range(len(original_words) - n + 1):
        ngram = " ".join(original_words[i:i + n])
        if calculate_similarity(ngram, compared) >= threshold:
            plagiarized_words.update(original_words[i:i + n])

    # Highlight plagiarized sections
    highlighted = []
    for word in original_words:
        if word in plagiarized_words:
            highlighted.append(f"[{word.upper()}]")
        else:
            highlighted.append(word)
    
    return " ".join(highlighted)
if __name__ == "__main__":
    # Example documents
    doc1 = """
    The quick brown fox jumps over the lazy dog. This is a simple example 
    to demonstrate plagiarism detection in text.
    """
    doc2 = """
    A quick brown fox jumped over a lazy dog. This example helps to show 
    how plagiarism detection systems can identify similarities.
    """
    
    # Preprocess the documents
    processed_doc1 = preprocess_text(doc1)
    processed_doc2 = preprocess_text(doc2)

    # Calculate similarity
    similarity = calculate_similarity(processed_doc1, processed_doc2)
    print(f"Similarity Score: {similarity * 100:.2f}%")

    # Highlight plagiarized sections
    highlighted_text = highlight_plagiarism(processed_doc1, processed_doc2)
    print("\nHighlighted Text:")
    print(highlighted_text)
