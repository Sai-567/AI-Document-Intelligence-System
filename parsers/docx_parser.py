from docx import Document


def extract_text_from_docx(uploaded_file):
    doc = Document(uploaded_file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text