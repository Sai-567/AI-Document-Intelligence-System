import re


def clean_text(text):
    """
    Clean extracted document text.
    """

    if not text:
        return ""

    # Remove multiple spaces
    text = re.sub(r"[ ]+", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n+", "\n", text)

    # Remove tabs
    text = text.replace("\t", " ")

    # Remove unwanted special characters
    text = re.sub(r"[^\w\s.,:/@()-]", "", text)

    return text.strip()