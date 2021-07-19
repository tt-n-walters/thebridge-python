# Hashing

import hashlib

print(hashlib.algorithms_available)

password = "abc123"
encoded = password.encode()
encrypted = hashlib.md5(encoded).hexdigest()

print()
print(encrypted)
