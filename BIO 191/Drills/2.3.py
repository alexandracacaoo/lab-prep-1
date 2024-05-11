a = int(input("Please enter an integer: "))
b = int(input("Please enter another integer: "))
c = int(input("Please enter the third integer: "))

maxNum = a 
if b > maxNum:
    maxNum = b
if c > maxNum:
    maxNum = c

odd = maxNum%2== 1

if (maxNum and odd):
    print(maxNum, "is the largest odd integer.")
else:
    print("There are no odd integers.")