import easyocr
from PIL import Image
import numpy as np

# Initialize the OCR reader once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    image_np = np.array(image)

    results = reader.readtext(image_np)

    text = "\n".join([result[1] for result in results])

    return text