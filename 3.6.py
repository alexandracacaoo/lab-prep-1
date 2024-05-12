N = int(input("Enter N: "))
print (N)

if N > 0:
    for i in range(N):
        for j in range(N):
            print("*", end=" ")
        print()
else:
    print(" ")


if N%2==1 and N>0:
    for i in range (N):
        for j in range (N):
            if i ==N-1:
                print ("*", end="")
            elif j == N-1:
                print("*", end="")
            elif i == 0:
                print("*", end="")
            elif j == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print ("")
