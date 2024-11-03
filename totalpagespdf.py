import os
import PyPDF2

def count_total_pages_in_pdfs(folder):
    total_pages = 0
    for root,dir, files in os.walk(folder):
        for file in files:
            if file.endswith('.pdf'):
                pdf_file_path = os.path.join(root, file)
                with open(pdf_file_path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    total_pages += len(pdf_reader.pages)
    return total_pages

folder_path = f'D:\Vishal'  # Replace with your folder path
total_pages = count_total_pages_in_pdfs(folder_path)
print(f'Total number of pages in all PDFs: {total_pages}')
