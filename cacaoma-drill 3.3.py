import math

N = int(input("Enter N: "))

def first_prime_numbers(N):
    X = 0
    i = 2
    flag = False
    while(X < N):
        flag = True
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if (i%j == 0):
                flag = False
                break
        if(flag):
            print(i, end=" ")
            X+=1
        i+=1
    print()

first_prime_numbers(N)

#This code is a slightly modified version of the code from https://www.geeksforgeeks.org/generate-and-print-first-n-prime-numbers/


