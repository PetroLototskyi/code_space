# Your code goes here
def replace_string(orig, old, new):

    return orig.replace(old, new)


orig_string = "Greetings, everybody!"
old_string = "everybody"
new_string = "friends"
result = replace_string(orig_string, old_string, new_string)

print(result)