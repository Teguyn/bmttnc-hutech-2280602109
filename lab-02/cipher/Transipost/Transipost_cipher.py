class TranspositionCipher:
     def __init__(self):
         pass

     def encrypt(self, text, key):
         encrypted_text = ''
         for col in range(key):
             pointer = col
             while pointer < len(text):
                 encrypted_text += text[pointer]
                 pointer += key
         return encrypted_text


def decrypt(self, encrypted_text, key):
     decrypted_text = [''] * key
     row, col = 0, 0
     for symbol in encrypted_text:
         decrypted_text[col] += symbol
         col += 1
         if col == key or (col == 1 and row < len(encrypted_text) % key):
             col = 0
             row += 1
     return ''.join(decrypted_text)
