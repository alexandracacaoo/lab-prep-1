age = int(input("What is your age? "))
has_license = input("Do you have a fishing license in MN? (yes/no) ")== "yes"
parent_has_license = input("Does your parent have a fishing license? (yes/no) ").lower() == "yes"

if age <= 15 and parent_has_license or (age >= 16 and has_license):
        print("You are legal to fish in MN.")
else:
        print("You are not allowed to fish in MN.")

#I made this code using the examples on the Drill as guide. 