N = int(input("Enter N: "))

for i in range(1, N + 1):
    for j in range(i, N):
        print(" ", end='')
    for k in range(i):
        print("*", end='')
    for l in range(1, i):
        print("*", end='')
    print()

for i in range(N - 1, 0, -1):
    for x in range(N - i):
        print(" ", end='')
    for y in range(i):
        print("*", end='')
    for z in range(1, i):
        print("*", end='')
    print()



