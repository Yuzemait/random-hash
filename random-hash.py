import hashlib
import random
import string

def generate_random_string(length=32):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_hash(input_string):
    """Generate a SHA-256 hash of the input string and return the first 32 characters."""
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha256_hash[:32]

def main():
    while True:
        # Generate a random string
        random_string = generate_random_string()
        
        # Generate a hash from the random string
        hash_value = generate_hash(random_string)
        
        # Check if the hash starts with two consecutive zeros
        if hash_value.startswith("00"):
            print("Found a hash starting with '00':")
            print(f"Random String: {random_string}")
            print(f"Hash Value: {hash_value}")
            break

if __name__ == "__main__":
    main()
