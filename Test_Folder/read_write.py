# Reading a file
with open("Test_Folder/example.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
with open("Test_Folder/output.txt", "w") as file:
    file.write("Hello, World!")