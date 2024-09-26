import os 
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
        print(f"{doc_id}: {filename}")  # Debugging: Display mapping

    return documents
