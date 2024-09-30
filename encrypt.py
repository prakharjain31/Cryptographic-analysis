from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Data to encrypt
message = b"Hello, world!"

# Hash the message
digest = hashes.Hash(hashes.SHA256())
digest.update(message)
hash_digest = digest.finalize()

# Encrypt the hash with the public key
encrypted = public_key.encrypt(
    hash_digest,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)