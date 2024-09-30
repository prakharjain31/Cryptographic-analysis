from cryptography.exceptions import InvalidSignature

# Decrypt the encrypted hash
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Verify the hash digest
try:
    digest.verify(decrypted)
    print("Message integrity confirmed.")
except InvalidSignature:
    print("Message integrity check failed.")