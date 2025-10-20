import os
from docx import Document

# Function to check if 'respectively' is in the document
def check_respectively_in_docx(file_path):
    try:
        # Open the .docx file
        doc = Document(file_path)
        # Iterate through each paragraph in the document
        for para in doc.paragraphs:
            if 'respectively' in para.text.lower():  # Case insensitive check
                return True
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return False

# Function to scan the directory and check each .docx file
def check_directory_for_respectively(directory_path):
    # List all files in the directory
    for filename in os.listdir(directory_path):
        # Skip temporary files that start with ~$ (Word temporary files)
        if filename.startswith("~$"):
            continue
        
        # Check if the file is a .docx
        if filename.endswith(".docx"):
            file_path = os.path.join(directory_path, filename)
            if check_respectively_in_docx(file_path):
                print(f"The word 'respectively' is found in: {filename}")

# Set the directory you want to scan
directory_path = r"Z:\CARTORIO DE SIMAO DIAS\LIVRO 2-AD - REGISTRO DE IMÓVEIS\Words"  # Change this to your directory path

# Start checking the directory
check_directory_for_respectively(directory_path)
