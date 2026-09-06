import csv

FILE_NAME = "expenses.csv"


# Create the CSV file if it does not exist
try:
    file = open(FILE_NAME, "r")
    file.close()
except FileNotFoundError:
    file = open(FILE_NAME, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["ID", "Amount", "Category", "Description"])
    file.close()


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Remove Expense")
    print("4. Show Summary")
    print("5. Exit")

    choice = input("Enter choice: ")


    # Add Expense
    if choice == "1":

        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        # Find the next ID
        file = open(FILE_NAME, "r")
        reader = csv.DictReader(file)

        last_id = 0

        for row in reader:
            last_id = int(row["ID"])

        file.close()

        new_id = last_id + 1

        # Add expense to CSV file
        file = open(FILE_NAME, "a", newline="")
        writer = csv.writer(file)

        writer.writerow([new_id, amount, category, description])

        file.close()

        print("Expense added successfully.")


    # View Expenses
    elif choice == "2":

        file = open(FILE_NAME, "r")
        reader = csv.DictReader(file)

        print("\n----- Expenses -----")

        found = False

        for row in reader:

            found = True

            print(
                "ID:", row["ID"],
                "| Amount: ₹" + row["Amount"],
                "| Category:", row["Category"],
                "| Description:", row["Description"]
            )

        file.close()

        if found == False:
            print("No expenses recorded.")


    # Remove Expense
    elif choice == "3":

        file = open(FILE_NAME, "r")
        reader = csv.DictReader(file)

        expenses = []

        for row in reader:
            expenses.append(row)

        file.close()

        if len(expenses) == 0:

            print("No expenses to remove.")

        else:

            print("\n----- Expenses -----")

            for expense in expenses:

                print(
                    "ID:", expense["ID"],
                    "| Amount: ₹" + expense["Amount"],
                    "| Category:", expense["Category"],
                    "| Description:", expense["Description"]
                )

            remove_id = input("\nEnter the ID of the expense to remove: ")

            found = False
            new_expenses = []

            for expense in expenses:

                if expense["ID"] == remove_id:
                    found = True
                else:
                    new_expenses.append(expense)

            if found == True:

                file = open(FILE_NAME, "w", newline="")
                writer = csv.writer(file)

                writer.writerow(["ID", "Amount", "Category", "Description"])

                for expense in new_expenses:

                    writer.writerow([
                        expense["ID"],
                        expense["Amount"],
                        expense["Category"],
                        expense["Description"]
                    ])

                file.close()

                print("Expense removed successfully.")

            else:

                print("Expense ID not found.")


    # Show Summary
    elif choice == "4":

        file = open(FILE_NAME, "r")
        reader = csv.DictReader(file)

        total_amount = 0
        category_totals = {}

        for row in reader:

            amount = float(row["Amount"])
            category = row["Category"]

            total_amount = total_amount + amount

            if category in category_totals:
                category_totals[category] = category_totals[category] + amount
            else:
                category_totals[category] = amount

        file.close()

        print("\n----- Summary -----")
        print("Total Amount Spent: ₹", total_amount)

        if len(category_totals) == 0:

            print("No expenses recorded.")

        else:

            print("\nAmount spent in each category:")

            for category in category_totals:

                print(
                    category,
                    ": ₹",
                    category_totals[category]
                )

            highest_category = ""
            highest_amount = 0

            for category in category_totals:

                if category_totals[category] > highest_amount:

                    highest_amount = category_totals[category]
                    highest_category = category

            print("\nCategory where you spent the most:")
            print(highest_category, ": ₹", highest_amount)


    # Exit
    elif choice == "5":

        print("Thank you for using Expense Tracker.")
        break


    else:

        print("Invalid choice. Please try again.")