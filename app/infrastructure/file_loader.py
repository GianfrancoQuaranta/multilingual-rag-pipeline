import docx

def load_text_file(path: str) -> str:
    """
    Loads the content of a text or DOCX file from the given path.

    Args:
        path (str): Path to the file (.txt or .docx).

    Returns:
        str: The full content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file extension is unsupported.
    """
    try:
        if path.endswith(".docx"):
            # Read DOCX file and extract non-empty paragraphs
            doc = docx.Document(path)
            return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

        elif path.endswith(".txt"):
            # Read plain text file
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        else:
            raise ValueError("Unsupported file format. Only .txt and .docx are allowed.")

    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File not found: {path}")
    except Exception as e:
        raise RuntimeError(f"❌ Failed to load file '{path}': {e}")
