# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes
# import hashlib

# def aes_encrypt(key, data):
#     cipher = AES.new(key, AES.MODE_CBC, iv=get_random_bytes(AES.block_size))
#     ciphertext = cipher.iv + cipher.encrypt(pad(data, AES.block_size))
#     return ciphertext

# def aes_decrypt(key, ciphertext):
#     iv = ciphertext[:AES.block_size]
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     decrypted_data = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
#     return decrypted_data

# # Example usage
# key = hashlib.sha256(b"salam").digest()[:32]  # 32 bytes for AES-256

# print(key)

# data = b'Some secret message'

# encrypted_data = aes_encrypt(key, data)
# print("Encrypted data:", encrypted_data.hex())

# decrypted_data = aes_decrypt(key, encrypted_data)
# print("Decrypted data:", decrypted_data.decode('utf-8'))


# print(get_random_bytes(AES.block_size))



from Crypto.Cipher import AES

key = b'ZiyaGadimli12345'
nonce = b'ZiyaGadimli54321'

ciper = AES.new(key, AES.MODE_EAX, nonce)

ciperText = ciper.encrypt(b"Hello World!")

print(f"encrypted: {ciperText}")
ciper = AES.new(key, AES.MODE_EAX, nonce)
print(f"encrypted: {ciper.decrypt(ciperText).decode()}")