file = input("File name: ").strip().lower()
print (file)
extention = file.rfind(".")
copy=file[extention:len(file)]
print(extention)
print(copy)
