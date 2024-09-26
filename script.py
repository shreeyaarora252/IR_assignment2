import os

#To read files
def read_documents_from_folder(folder_path):
    documents = {}
    doc_id = 1
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                documents[doc_id] = text
                doc_id += 1
                
    print("Documents loaded successfully")
    return documents

folder_path = './documents'
documents = read_documents_from_folder(folder_path)
print(documents)  
