import os
from docx import Document

def create_word_from_pdf(model_docx_path):
    # Get the current directory where the script is located
    current_dir = os.getcwd()
    
    # Set the pdf_folder as the current directory
    pdf_folder = current_dir

    # Ensure the 'WORDS' directory exists inside the current directory
    word_dir = os.path.join(current_dir, 'WORDS')
    if not os.path.exists(word_dir):
        os.makedirs(word_dir)

    # Get list of PDF files in the current directory that follow the numeric naming pattern
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf') and f[:-4].isdigit()]

    if not pdf_files:
        print("No valid PDF files found in the folder.")
        return

    # Load the model Word document to replicate its content
    try:
        model_doc = Document(model_docx_path)
    except Exception as e:
        print(f"Error loading model document: {e}")
        return

    # Process each PDF file and create the corresponding Word document
    for pdf_file in pdf_files:
        # Extract the numeric part of the filename (remove the .pdf)
        pdf_name_without_extension = pdf_file[:-4]
        new_docx_path = os.path.join(word_dir, f"{pdf_name_without_extension}.docx")
        
        # Create a new Word document based on the model
        new_doc = Document()

        # Copy content from the model document to the new document
        for element in model_doc.element.body:
            new_doc.element.body.append(element)

        # Save the new document with the appropriate name
        try:
            new_doc.save(new_docx_path)
            print(f"Created: {new_docx_path}")
        except Exception as e:
            print(f"Failed to create Word document for {pdf_file}: {e}")
        
    print("Process completed.")

# Example usage:
model_docx_path = 'path/to/your/model/file.docx'
create_word_from_pdf(model_docx_path)
