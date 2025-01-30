def main():
    str=input("camelCase: ")
    print(convert(str))

def convert(str):
    new_str=""
    for i in str:
        if i.isupper():
            new_str += "_"+i.lower()
        else:
            new_str += i
    return new_str

main()

