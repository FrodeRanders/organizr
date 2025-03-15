from os import walk, path
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    name = path.basename(pdf_path)
    print(f"Extracting text from {name}")

    text = ""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def find_pdfs_recursive(start_dir):
    pdf_files = []
    for root, dirs, files in walk(start_dir):
        for filename in files:
            if filename.lower().endswith(".pdf"):
                # Construct the full (absolute) path:
                full_path = path.join(root, filename)
                pdf_files.append(full_path)
    return pdf_files
