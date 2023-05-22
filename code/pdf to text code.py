import PyPDF2

def convert_pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Usage
pdf_file_path = 'C:/Users/adity/Downloads/Data/Data/Task1/table.pdf'
extracted_text = convert_pdf_to_text(pdf_file_path)
print(extracted_text)