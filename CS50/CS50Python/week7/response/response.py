from validator_collection import validators, checkers, errors
import sys

email = input("What's your email address? ")

try:
    email_address = validators.email(email)
    print ("Valid")
except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")


