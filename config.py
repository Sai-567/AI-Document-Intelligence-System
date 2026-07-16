import os
import pytesseract

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
EXTRACTED_FOLDER = os.path.join(BASE_DIR, "extracted")
MODEL_FOLDER = os.path.join(BASE_DIR, "models")
DATA_FOLDER = os.path.join(BASE_DIR, "data")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"