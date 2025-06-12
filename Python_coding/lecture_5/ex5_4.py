# An acronym is a word formed by taking the first letters of the words in a 
# phrase and making a word from them. For example, RAM is an acronym 
# for "random access memory." Write a program that allows the user to 
# type in a phrase and then outputs the acronym for that phrase. Note: The 
# acronym should be all uppercase, even if the words in the phrase are not 
# capitalized.

def main():
    string = input("Write phrase that need to be converted to acronim: ")

    # words = string.split()
    # print(words)
    result=""
    for word in string.split():
        result=result+word[0]
    print (result.upper())
main()