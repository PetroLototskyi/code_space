#  Validates email address by checking whether domain ends with .edu

email = input("What's your email? ").strip() #.strip() will remove white spases on both sides

uername, domain = email.split("@")

# if uername and "." in domain: # checking if username exist and if "." in domain
if username and domain.endswith(".edu"): #checking if username exist and whether domain ends with .edu
    print("Valid")
else:
    print("Invalid")
