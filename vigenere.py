from collections import Counter

def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    for i in range(len(text)):
        result += chr(((ord(text[i]) - 65 + ord(key[i % len(key)]) - 65) % 26) + 65)
    return result

def vigenere_decrypt(cipher, key):
    cipher = cipher.upper()
    key = key.upper()
    result = ""
    for i in range(len(cipher)):
        result += chr(((ord(cipher[i]) - 65 - (ord(key[i % len(key)]) - 65)) % 26) + 65)
    return result

def frequency_analysis(text):
    count = Counter(text)
    for k, v in count.items():
        print(f"{k} : {v/len(text):.3f}")

plaintext = "ATTACKATDAWN"
key = "LEMON"

ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

print("\nDekripsi:", vigenere_decrypt(ciphertext, key))

print("\nFrekuensi huruf:")
frequency_analysis(ciphertext)


