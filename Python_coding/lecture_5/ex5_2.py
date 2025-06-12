# A certain CS professor gives 5-point quizzes that are graded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as
# an input and prints out the corresponding grade.


def main():
    # get the quizzes number
    exit = 0
    while exit != 1:
        try:
            quiz_score = int(input("Enter a quiz point (from 0 to 5) : "))
        except ValueError:
            print("The score should be positive onteger in range  from 0 to 5 include")
            continue
        if quiz_score == 5:
            print("A")
            exit = 1
        elif quiz_score == 4:
            print("B")
            exit = 1
        elif quiz_score == 3:
            print("C")
            exit = 1
        elif quiz_score == 2:
            print("D")
            exit = 1
        elif quiz_score == 1 or quiz_score == 0:
            print("F")
            exit = 1
        else:
            print("The point is out of rscore range")


main()
