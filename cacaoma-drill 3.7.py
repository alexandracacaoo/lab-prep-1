N = int(input("Enter N: "))

if N > 0:
    for i in range(N):
        for j in range (N - i) :
            print(" ", end="")
        for k in range((i * 2) - 1):
            print("*", end="")
        print()
    for i in range(N, 0, -1):
        for j in range (N - i) :
            print(" ", end="")
        for k in range((i * 2) - 1):
            print("*", end="")
        print()

#This code is a slightly modified version of the code from https://stackoverflow.com/questions/32613579/creating-a-diamond-pattern-using-loops