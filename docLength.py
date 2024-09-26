import math

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
