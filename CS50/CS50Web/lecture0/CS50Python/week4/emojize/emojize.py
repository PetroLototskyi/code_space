# import library
import emoji

# Promt for uer input
user_input = input("Input: ")

# enables both the full list of emoji code and aliases and assign to varible
output = emoji.emojize(user_input, language="alias")

# print rezult
print(f"Output: {output}")
