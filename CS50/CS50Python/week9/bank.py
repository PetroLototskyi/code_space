balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    wirthraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance # Uses global
    balance += n # UnboundLocalError

def wirthraw(n):
    global balance # Uses global
    balance -= n # UnboundLocalError

if __name__=="__main__":
    main()
