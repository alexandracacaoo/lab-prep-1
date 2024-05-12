N = int(input("Enter N: "))
print (N)

first = []
for j in range(N - 1):
    first.append("*" * N)
first.append("*" * N)

two = []
for j in range(N - 1):
    if j == 0:
        two.append("*" * N)
    else:
        two.append("*" + ((N - 2) * " ") + "*")
two.append("*" * N)

for f, t in zip(first, two):
    print(f + '\t' + t)


    