from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world')
    '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib
    if not text:
        return None
    hash_object = hashlib.md5(text.encode())
    return hash_objec.hexdigest()
