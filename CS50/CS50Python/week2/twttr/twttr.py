def main():
    text = input("Input: ")
    print("Output:", remove_vowels(text))

def remove_vowels(text):
    new_text=""
    for c in text:
        if c in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"] :
             continue
        else:
            new_text += c

    return new_text

main ()

