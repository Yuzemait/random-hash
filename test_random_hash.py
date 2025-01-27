import hashlib
from random_hash import generate_random_string, generate_hash

def test_generate_random_string():
    random_string = generate_random_string()
    assert len(random_string) == 32
    assert random_string.isalnum()

def test_generate_hash():
    input_string = "test_string"
    hash_value = generate_hash(input_string)
    assert len(hash_value) == 32
    assert hash_value == hashlib.sha256(input_string.encode()).hexdigest()[:32]

