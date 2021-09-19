from django.contrib.auth.hashers import make_password
from datetime import datetime
from secrets import token_hex


def hash_pbkdf2(plaintext):
    if plaintext.startswith("pbkdf2_"):
        return plaintext
    return make_password(plaintext, token_hex(12))
