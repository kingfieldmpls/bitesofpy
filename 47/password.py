# You know these Create a new password forms? They do a lot of checks to make
# sure you make a password that is hard to guess and you will surely forget.

# In this Bite you will write a validator for such a form field.

# Complete the validate_password function below. It takes a password str and
# validates that it:

# is between 6 and 12 chars long (both inclusive)
# has at least 1 digit [0-9]
# has at least two lowercase chars [a-z]
# has at least one uppercase char [A-Z]
# has at least one punctuation char (use: PUNCTUATION_CHARS)
# Has not been used before (use: used_passwords)
# If the password matches all criteria the function should store the password
# in used_passwords and return True.

# Have fun, keep calm and code in Python!

import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def pw_length(password):
    if 6 <= len(password) <= 12:
        return password


def pw_digit(password):
    if any(char.isdigit() for char in password):
        return password


def pw_lower(password):
    if len([char.islower() for char in password if char.islower() is True]) >= 2:
        return password


def pw_upper(password):
    if len([char.isupper() for char in password if char.isupper() is True]) >= 1:
        return password


def pw_punc(password):
    if any(char for char in PUNCTUATION_CHARS if char in password):
        return password


def pw_unique(password):
    if password not in used_passwords:
        return password


def validate_password(password):
    if (
        pw_length(password)
        and pw_digit(password)
        and pw_lower(password)
        and pw_upper(password)
        and pw_punc(password)
        and pw_unique(password)
    ):
        used_passwords.add(password)
        return True
