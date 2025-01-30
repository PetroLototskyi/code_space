# TODO
import math


def main():
    text = input("Text: ")
    index = round(0.0588 * count_letters(text) - 0.296 * count_sentences(text) - 15.8)
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    result = 0
    for char in text:
        if char.isalpha():
            result += 1
    return (result / count_words(text)) * 100


def count_words(text):
    words = text.split()
    return len(words)


def count_sentences(text):
    result = 0
    for char in text:
        if char in [".", "!", "?"]:
            result += 1
    return (result / count_words(text)) * 100


if __name__ == "__main__":
    main()
