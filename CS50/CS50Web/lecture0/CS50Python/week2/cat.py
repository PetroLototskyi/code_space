'''
i = 1
while i <=3:
    print ("meow")
    i += 1
'''
# for _ in range(4):
#     print("meow")
#     print (_)

# print("meow\n" *3, end="")

'''
while True:
    n = int (input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range (n):
        print("meow")

main ()
