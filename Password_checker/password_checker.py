def check_password(password):
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        else:
            has_special = True

    length_check = len(password) >= 8

    requirements = [
        length_check,
        has_upper,
        has_lower,
        has_number,
        has_special
    ]

    satisfied = sum(requirements)

    print("\nPassword Analysis")
    print("-" * 20)
    print("At least 8 characters:", "Yes" if length_check else "No")
    print("Contains uppercase letter:", "Yes" if has_upper else "No")
    print("Contains lowercase letter:", "Yes" if has_lower else "No")
    print("Contains a number:", "Yes" if has_number else "No")
    print("Contains special character:", "Yes" if has_special else "No")

    if satisfied <= 2:
        strength = "WEAK"
    elif satisfied <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    print("\nStrength:", strength)


while True:
    password = input("\nEnter your password: ")
    check_password(password)

    choice = input("\nDo you want to try again? (Y/N): ")

    if choice == "Y" or choice == "y":
        continue
    elif choice == "N" or choice == "n":
        print("Program exited.")
        break
    else:
        print("Invalid input. Program exited.")
        break