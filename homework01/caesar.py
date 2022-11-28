def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alphabet_en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_en_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for i in plaintext:
        if i.isupper():
            place = alphabet_en_upper.find(i)
            new_place = place + shift
            if i in alphabet_en_upper:
                ciphertext += alphabet_en_upper[new_place]
            elif plaintext == '""':
                ciphertext += "''"
            else:
                ciphertext += i
        else:
            place = alphabet_en_lower.find(i)
            new_place = place + shift
            if i in alphabet_en_lower:
                ciphertext += alphabet_en_lower[new_place]
            elif plaintext == '""':
                ciphertext += "''"
            else:
                ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
        for i in plaintext:
        if i.isupper():
            place = alphabet_en_upper.find(i)
            new_place = place + shift
            if i in alphabet_en_upper:
                ciphertext += alphabet_en_upper[new_place]
            elif plaintext == '""':
                ciphertext += "''"
            else:
                ciphertext += i
        else:
            place = alphabet_en_lower.find(i)
            new_place = place + shift
            if i in alphabet_en_lower:
                ciphertext += alphabet_en_lower[new_place]
            elif plaintext == '""':
                ciphertext += "''"
            else:
                ciphertext += i
    return plaintext
