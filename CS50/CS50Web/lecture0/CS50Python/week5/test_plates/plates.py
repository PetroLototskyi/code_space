def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False
    elif not s.isalnum():
        return False

    for index in range(len(s)):
        if index<2 and s[index].isdigit():
            return False
        elif s[index].isdigit():
            if s[index]=="0":
                return False
            elif any(ch.isalpha() for ch in s[index:]):
                return False
            else:
                break


    return True

if __name__=="__main__":
    main()
