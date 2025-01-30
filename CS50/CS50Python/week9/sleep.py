def main():
    n=int(input("What's n? "))
    for i in range(n):
        print("🐑" * i)

# Returns n sheep from helper function
    print("____________________________Returns n sheep from helper function________________")

    for i in range(n):
        print(sheep(i))


# Returns a list of sheep
    print("____________________________Returns n sheep from helper function________________")

    for s in sheep_(n):
        print(s)


# Uses yield
    print("____________________________Uses yield________________")

    for s in sheep_y(n):
        print(s)


def sheep_y(n):
    for i in range(n):
        yield "🐑" * i #will return line by line . One value at the time

def sheep_(n):
    flock= []
    for i in range(n):
        flock.append("🐑"*i)
    return flock

def sheep(n):
    return "🐑" * n



if __name__ == "__main__":
    main()
