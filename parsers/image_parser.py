import easyocr
from PIL import Image
import numpy as np


reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def extract_text_from_image(uploaded_file):

    image = Image.open(uploaded_file)

    image_np = np.array(image)

    result = reader.readtext(
        image_np,
        detail=0
    )

    text = "\n".join(result)

    return text
