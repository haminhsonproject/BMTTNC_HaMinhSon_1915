from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for plaintext in text:
            plaintext_index = self.alphabet.index(plaintext)
            output_index = (plaintext_index + key) % alphabet_len
            output_cipher = self.alphabet[output_index]
            encrypted_text.append(output_cipher)
        return "".join(encrypted_text)
    
    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for cipher in text:
            cipher_index = self.alphabet.index(cipher)
            output_index = (cipher_index - key) % alphabet_len
            output_cipher = self.alphabet[output_index]
            decrypted_text.append(output_cipher)
        return "".join(decrypted_text)
            
        