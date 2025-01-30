def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print (evaluate(answer))

def evaluate(str):
    if str.strip()== "42":
        return "Yes"
    elif str.lower()=="forty-two" or str.lower()=="forty two":
        return "Yes"
    else: return "No"

main()

