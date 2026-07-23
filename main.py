from Crypto.Cipher import DES, AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import base64

# DES
def des_encrypt_decrypt():

    print("\n" + "=" * 50)
    print("DES Encryption / Decryption")
    print("=" * 50)

    # DES key ต้องมีขนาด 8 bytes
    key = b"12345678"

    plaintext = "beyourlanaboy"

    # Encrypt
    cipher = DES.new(key, DES.MODE_ECB)

    encrypted = cipher.encrypt(
        pad(plaintext.encode(), DES.block_size)
    )

    encrypted_text = base64.b64encode(encrypted).decode()

    # Decrypt
    decrypted = unpad(
        cipher.decrypt(
            base64.b64decode(encrypted_text)
        ),
        DES.block_size
    )

    print("Before Encryption :")
    print(plaintext)

    print("\nAfter Encryption :")
    print(encrypted_text)

    print("\nAfter Decryption :")
    print(decrypted.decode())


# AES
def aes_encrypt_decrypt():

    print("\n" + "=" * 50)
    print("AES Encryption / Decryption")
    print("=" * 50)

    # AES key 16 bytes
    key = b"1234567890123456"

    plaintext = "beyourlanaboy"

    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt
    encrypted = cipher.encrypt(
        pad(plaintext.encode(), AES.block_size)
    )

    encrypted_text = base64.b64encode(encrypted).decode()

    # Decrypt
    decrypted = unpad(
        cipher.decrypt(
            base64.b64decode(encrypted_text)
        ),
        AES.block_size
    )

    print("Before Encryption :")
    print(plaintext)

    print("\nAfter Encryption :")
    print(encrypted_text)

    print("\nAfter Decryption :")
    print(decrypted.decode())


# RSA
def rsa_encrypt_decrypt():

    print("\n" + "=" * 50)
    print("RSA Encryption / Decryption")
    print("=" * 50)

    plaintext = "beyourlanaboy"

    # Generate RSA Key
    key = RSA.generate(2048)

    public_key = key.publickey()

    # Encrypt using Public Key
    encryptor = PKCS1_OAEP.new(public_key)

    encrypted = encryptor.encrypt(
        plaintext.encode()
    )

    encrypted_text = base64.b64encode(encrypted).decode()

    # Decrypt using Private Key
    decryptor = PKCS1_OAEP.new(key)

    decrypted = decryptor.decrypt(
        base64.b64decode(encrypted_text)
    )

    print("Before Encryption :")
    print(plaintext)

    print("\nAfter Encryption :")
    print(encrypted_text)

    print("\nAfter Decryption :")
    print(decrypted.decode())

# Results :DDD
print("beyourlanaboy")
print("Encryption and Decryption using DES, AES, RSA")
des_encrypt_decrypt()
aes_encrypt_decrypt()
rsa_encrypt_decrypt()