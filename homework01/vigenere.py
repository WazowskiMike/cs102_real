def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    keyword *= len(plaintext) // len(keyword) + 1
    for i, j in enumerate(plaintext):
        m = ord(j) + ord(keyword[i])
        if 65 <=ord(j) <= 90:
            ciphertext += chr(m % 26 + 65)
    if 97 <= ord(j) <= 122:
        ord_new = ord('a')
        keyword *= len(plaintext) // len(keyword) + 1
        for indx, chplain in enumerate(plaintext):
            ciphertext += chr(((ord(chplain) - ord_new) + (ord(keyword[indx]) - ord_new)) % 26 + ord_new)
    return ciphertext




def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    keyword *= len(ciphertext) // len(keyword) + 1
    for i, j in enumerate(ciphertext):
        m = (ord(j) - ord(keyword[i]))
        if 65 <=ord(j) <= 90:
            plaintext += chr(m % 26 + 65)
        if 97 <= ord(j) <= 122:
            plaintext += chr(m % 26 + 97)
    return plaintext
