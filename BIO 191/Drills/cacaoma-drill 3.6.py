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

#This code is a slightly modified version of the code from https://stackoverflow.com/questions/59499206/printing-two-different-squares-made-of-asterisks-adjacent-to-each-other?fbclid=IwAR2PvP-cmxk_Iwci9B9nDhelBiWQyz4N6pYyWGI67-2qFN5H4v-fw6fduaI