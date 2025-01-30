'''def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print (*uppercased) # Prints arbitrarily many args in uppercase

if __name__=="__main__":
    main()'''
# Uses map
def main():
    yell("This", "is", "CS50")

    '''
def yell(*words):
    uppercased = map(str.upper , words)
    print (*uppercased)'''

# Uses list comprehension
def yell(*words):
    uppercased = [arg.upper() for arg in words] #create list inside of each word upper case
    print (*uppercased)

if __name__=="__main__":
    main()

