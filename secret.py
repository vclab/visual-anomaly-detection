import secrets

# Generate a random 24-character secret key
secret_key = secrets.token_hex(24)
print(secret_key)