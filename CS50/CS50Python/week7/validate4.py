# Validates email address by checking for @ with regex

import re
'''
email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email): #Add \.edu. Need to use "r" at beginig when using \
    #[^@] mean evrething exept "@"
    print("Valid")
else:
    print("Invalid")
    #________________________________________________________

    email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
'''


email = input("What's your email? ").strip()
# (\w+\.)?   - this mean characters followed with coma can be there or not
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
