N = int(input("Enter N: "))

if N%2 == 1 and N>0:
    for i in range(N):
        for j in range(N):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print(" ")

#I made this code using exer 4.1 as guide. 