from collections import defaultdict
import os 
import math

def read_documents_from_folder(folder_path):
    documents = {}
    doc_id_map = {}  # Map to store document ID -> filename
    doc_id = 1

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                documents[doc_id] = text
                doc_id_map[doc_id] = filename  # Store mapping
                doc_id += 1

    print("Document ID -> Filename Map:")
    for doc_id, filename in doc_id_map.items():
        print(f"{doc_id}: {filename}")  # debugging: Display mapping

    return documents


def build_index(documents):
    inverted_index = defaultdict(list)

    for doc_id, text in documents.items():
        term_freqs = defaultdict(int)
        terms = text.lower().split()

        for term in terms:
            term_freqs[term] += 1

        for term, tf in term_freqs.items():
            inverted_index[term].append((doc_id, tf))
    
    print("Inverted index created")  # debugging
    return inverted_index

inverted_index = build_index(documents)
print(inverted_index)  

def build_index(documents):
    inverted_index = defaultdict(list)
    document_lengths = {}  # Store document vector lengths

    for doc_id, text in documents.items():
        term_freqs = defaultdict(int)
        terms = text.lower().split()

        for term in terms:
            term_freqs[term] += 1

        for term, tf in term_freqs.items():
            inverted_index[term].append((doc_id, tf))

        length = math.sqrt(sum((1 + math.log(tf))**2 for tf in term_freqs.values()))
        document_lengths[doc_id] = length
    
    print("Document lengths calculated")  # Debugging
    return inverted_index, document_lengths

inverted_index, document_lengths = build_index(documents)

def compute_tf_idf(inverted_index, document_lengths, N, query):
    query_terms = query.lower().split()
    query_term_freqs = defaultdict(int)

    for term in query_terms:
        query_term_freqs[term] += 1

    scores = defaultdict(float)
    query_length = 0.0

    for term, qtf in query_term_freqs.items():
        if term in inverted_index:
            df = len(inverted_index[term])
            idf = math.log(N / df)
            query_tf_idf = (1 + math.log(qtf)) * idf
            query_length += query_tf_idf ** 2

            for doc_id, tf in inverted_index[term]:
                doc_tf_idf = (1 + math.log(tf))
                scores[doc_id] += query_tf_idf * doc_tf_idf

    query_length = math.sqrt(query_length)
    for doc_id in scores:
        scores[doc_id] /= (document_lengths[doc_id] * query_length)

    return scores


