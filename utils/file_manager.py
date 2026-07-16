import os
import config


def save_text(filename, text):

    # Create the folder if it doesn't exist
    os.makedirs(config.EXTRACTED_FOLDER, exist_ok=True)

    name = os.path.splitext(filename)[0]

    output_path = os.path.join(
        config.EXTRACTED_FOLDER,
        name + ".txt"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return output_path