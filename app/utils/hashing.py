import hashlib

def stable_hash(text: str) -> str:
    """
    Generate a stable SHA-256 hash from a normalized input string.

    This function ensures consistent hashing by:
    - Stripping leading/trailing whitespace.
    - Replacing multiple spaces and newlines with a single space.
    - Encoding the result in UTF-8 before hashing.

    Args:
        text (str): The input text to hash.

    Returns:
        str: A hexadecimal representation of the SHA-256 hash.
    """
    # Normalize whitespace (remove extra spaces, newlines, tabs)
    normalized = " ".join(text.strip().split())

    # Compute and return SHA-256 hash
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()
