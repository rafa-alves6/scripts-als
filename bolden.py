import os
from docx import Document

# Directory containing your Word documents
directory = 'Z:/CARTORIO DE SIMAO DIAS/LIVRO 2-AD - REGISTRO DE IMÓVEIS/Words'

# Loop through all Word documents in the specified directory
for filename in os.listdir(directory):
    if filename.endswith('.docx'):
        # Full path of the document
        doc_path = os.path.join(directory, filename)
        
        # Open the current document
        doc = Document(doc_path)
        
        # Make all the text bold
        for para in doc.paragraphs:
            for run in para.runs:
                run.bold = True
        
        # Save the modified document
        doc.save(doc_path)

print("All text in all documents has been made bold.")
