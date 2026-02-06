def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def calculator():
    while True:
        print("\n--- Safe Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "5":
            print("Bye 👋")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("❌ Invalid choice. Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == "1":
                print("✅ Result:", num1 + num2)
            elif choice == "2":
                print("✅ Result:", num1 - num2)
            elif choice == "3":
                print("✅ Result:", num1 * num2)
            elif choice == "4":
                print("✅ Result:", num1 / num2)

        except ZeroDivisionError:
            print("❌ Error: You can't divide by zero!")

calculator()
