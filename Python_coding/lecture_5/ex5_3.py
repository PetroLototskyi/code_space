#  A certain CS professor gives 100-point exams that are graded on the scale 
# 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that ac
#  cepts an exam score as input and prints out the corresponding grade.

def main():
    # get the quizzes number
    exit = 0
    while exit != 1:
        try:
            quiz_score = int(input("Enter a quiz point (from 0 to 100) : "))
        except ValueError:
            print("The score should be positive onteger in range  from 0 to 100 include")
            continue
        if 90 <= quiz_score < 101:
            print("A")
            exit = 1
        elif 80 <= quiz_score <= 89:
            print("B")
            exit = 1
        elif 70 <= quiz_score <= 79:
            print("C")
            exit = 1
        elif 60 <= quiz_score <= 69:
            print("D")
            exit = 1
        elif quiz_score <60:
            print("F")
            exit = 1
        else:
            print("The point is out of rscore range")


main()
