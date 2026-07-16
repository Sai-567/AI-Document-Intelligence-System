import streamlit as st
from parsers.pdf_parser import extract_text_from_pdf
from parsers.docx_parser import extract_text_from_docx
from parsers.image_parser import extract_text_from_image
from preprocessing.cleaner import clean_text
from utils.file_manager import save_text
from extractor.entity_extractor import extract_entities

st.set_page_config(
    page_title="AI Document Intelligence System",
    page_icon="📄",
    layout="wide"
)
import base64

def get_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_image = get_base64("assets/image.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Optional: Make the main content readable */
    .main > div {{
        background: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #fffff;
}

/* Main title */
h1 {
    color: #1E3A8A;
    text-align: center;
}

/* Subheadings */
h2, h3 {
    color: #2563EB;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1E293B;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: black;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #dbeafe;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

st.title("📄 AI Document Intelligence System")

st.markdown("""
### 🤖 AI-Powered Document Processing & Intelligence

Transform unstructured documents into structured insights using **OCR, NLP, Machine Learning, and AI**.

#### ✨ Features

- 📄 Extract text from **PDF, DOCX, and Images**
- 🔍 OCR for scanned documents
- 🧹 Intelligent text cleaning
- 📌 Entity extraction (Name, Email, Phone, Organization, etc.)
- 📚 Automatic document classification
- 🤖 AI-powered document summarization
---
""")


uploaded_file = st.file_uploader(
    "Upload a Document",
    type=["pdf", "docx", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    col1, col2 = st.columns(2)

    col1.info(f"📄 File Type: {uploaded_file.type}")

    col2.info(f"📦 File Size: {round(uploaded_file.size/1024,2)} KB")
    text = ""

    if uploaded_file.type == "application/pdf":

        text = extract_text_from_pdf(uploaded_file)

    elif uploaded_file.type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]:

        text = extract_text_from_docx(uploaded_file)

    elif uploaded_file.type.startswith("image"):

        text = extract_text_from_image(uploaded_file)

    cleaned_text = clean_text(text)
    entities = extract_entities(cleaned_text)
    st.subheader("📌 Extracted Information")

    for key, values in entities.items():

      with st.expander(f"📂 {key}", expanded=False):

        if values:
            for value in values:
                st.markdown(f"- **{value}**")
        else:
            st.info("No data found")
    st.subheader("📊 Document Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Characters", len(cleaned_text))
    col2.metric("Words", len(cleaned_text.split()))
    col3.metric("Lines", len(cleaned_text.splitlines()))

    st.subheader("Extracted Text")

    st.text_area(
        "Document Content",
        cleaned_text,
        height=450
    )

    saved_file = save_text(
        uploaded_file.name,
        cleaned_text
    )

    st.balloons()

    st.success("""
    ## 🎉 Thank You!

    Your document has been processed successfully.

    You can now:
    - Review the extracted text
    - View extracted entities
    - Check document statistics

    Thank you for using the **AI Document Intelligence System**!
    """)
    
