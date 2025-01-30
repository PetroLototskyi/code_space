def convert(str):
    test =  str.replace(":)", "🙂")
    test =test.replace(":(", "🙁")
    return test

def main():
    str = input ("Enter string: ")
    print(convert(str))

main()
