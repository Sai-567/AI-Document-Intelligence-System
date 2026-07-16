import re


def extract_entities(text):
    entities = {}

    # ------------------------
    # Email
    # ------------------------
    entities["Emails"] = list(set(re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )))

    # ------------------------
    # Phone Numbers
    # ------------------------
    entities["Phone Numbers"] = list(set(re.findall(
        r"(?:\+91[-\s]?)?[6-9]\d{9}",
        text
    )))

    # ------------------------
    # Websites
    # ------------------------
    entities["Websites"] = list(set(re.findall(
        r"(https?://[^\s]+|www\.[^\s]+)",
        text
    )))

    # ------------------------
    # LinkedIn
    # ------------------------
    entities["LinkedIn"] = list(set(re.findall(
        r"https?://(?:www\.)?linkedin\.com/[^\s]+",
        text
    )))

    # ------------------------
    # GitHub
    # ------------------------
    entities["GitHub"] = list(set(re.findall(
        r"https?://(?:www\.)?github\.com/[^\s]+",
        text
    )))

    # ------------------------
    # Years
    # ------------------------
    entities["Years"] = list(set(re.findall(
        r"\b(?:19|20)\d{2}\b",
        text
    )))
    return entities