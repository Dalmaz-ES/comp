
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars) #changing the type to str
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

#encrypt
plain_text = input("Enter plain text to encrypt: ")
cipher_text = ""

for x in plain_text:
    index = chars.index(x)
    cipher_text += key[index]

print(f"original plain text: {plain_text}")
print(f"cipher text: {cipher_text}")


#decrypt
cipher_text = input("Enter cipher text to decrypt: ")
plain_text = ""

for x in cipher_text:
    index = key.index(x)
    plain_text += chars[index]

print(f"cipher text: {cipher_text}")
print(f"original plain text: {plain_text}")
