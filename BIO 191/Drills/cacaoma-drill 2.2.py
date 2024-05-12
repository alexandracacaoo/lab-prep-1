age = int(input("Please enter your age: "))
natural_born_citizen = input("Are you a natural born citizen of the U.S.? (yes/no) ").lower() == "yes"
resident_of_the_US = int(input("How many years have you resided in the U.S.? "))

eligible = False

if age > 35 and natural_born_citizen and resident_of_the_US >=14:
    eligible = True

if eligible:
    print ("You can run for president of USA")
else:
    print("You cannot run for president of USA")

#I made this code using the examples on the Drill as guide. 