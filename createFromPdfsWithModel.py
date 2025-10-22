import os
import shutil
import win32com.client as win32

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

    # Initialize Word application (using COM automation)
    word = win32.Dispatch('Word.Application')
    word.Visible = False  # Don't show Word UI (run in the background)

    try:
        # Open the model Word document
        doc = word.Documents.Open(model_docx_path)

        # Process each PDF file and create the corresponding Word document
        for pdf_file in pdf_files:
            # Extract the numeric part of the filename (remove the .pdf)
            pdf_name_without_extension = pdf_file[:-4]
            new_docx_path = os.path.join(word_dir, f"{pdf_name_without_extension}.docx")
            
            # Make a copy of the model document
            doc.Copy()
            new_doc = word.Documents.Add()  # Create a new document
            new_doc.Range(0, 0).Paste()  # Paste content from the clipboard

            # Save the new document with the appropriate name
            try:
                new_doc.SaveAs(new_docx_path)
                print(f"Created: {new_docx_path}")
            except Exception as e:
                print(f"Failed to create Word document for {pdf_file}: {e}")
            finally:
                new_doc.Close()

    except Exception as e:
        print(f"Error opening model document: {e}")
    finally:
        # Close the original model document
        doc.Close()

    word.Quit()  # Close the Word application

    print("Process completed.")

# Example usage:
model_docx_path = r'Z:\CARTORIO DE SIMAO DIAS\modelo.docx'
create_word_from_pdf(model_docx_path)
