def main():
    text = input("Input: ")
    print("Output:", shorten(text))

def shorten(word):
    new_text=""
    for c in word:
        if c in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"] :
             continue
        else:
            new_text += c

    return new_text

if __name__=="__main__":
    main ()

