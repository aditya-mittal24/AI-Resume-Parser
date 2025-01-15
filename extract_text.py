import PyPDF2

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file object.
    Args:
        pdf_file: File object of the uploaded PDF.
    Returns:
        Extracted text as a string.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""
