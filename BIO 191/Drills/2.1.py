

def can_fish(age, has_license, parent_has_license):
    return (age <= 15 and parent_has_license) or (age >= 16 and has_license)

def main():
    age = int(input("What is your age? "))
    has_license = input("Do you have a fishing license? (yes/no) ")== "yes"
    parent_has_license = input("Does your parent have a fishing license? (yes/no) ").lower() == "yes"

    if can_fish(age, has_license, parent_has_license):
        print("You are legal to fish in Minnesota.")
    else:
        print("You are not allowed to fish in Minnesota.")

if __name__ == "__main__":
    main ()
