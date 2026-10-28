# Engineering Unit Converter
# Converts measurements and stores conversion history.

history = []

def convert(choice, value):
    if choice == 1:
        return value / 25.4, "inches"
    elif choice == 2:
        return value * 25.4, "mm"
    elif choice == 3:
        return (value * 9/5) + 32, "°F"
    elif choice == 4:
        return (value - 32) * 5/9, "°C"
    elif choice == 5:
        return value * 2.20462, "lb"
    elif choice == 6:
        return value / 2.20462, "kg"
    elif choice == 7:
        return value / 3.6, "m/s"
    elif choice == 8:
        return value * 3.6, "km/h"


# Repeat until the user exits.
while True:
    print("\nENGINEERING UNIT CONVERTER")
    print("1. mm to inches")
    print("2. Inches to mm")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. kg to lb")
    print("6. lb to kg")
    print("7. km/h to m/s")
    print("8. m/s to km/h")
    print("9. View history")
    print("0. Exit")

    try:
        choice = int(input("Choose an option: "))

        if choice == 0:
            print("Goodbye!")
            break

        elif choice == 9:
            if history:
                for item in history:
                    print(item)
            else:
                print("No history available.")
            continue

        elif choice < 1 or choice > 9:
            print("Invalid choice!")
            continue

        value = float(input("Enter value: "))
        result, unit = convert(choice, value)

        message = f"Result: {result:.2f} {unit}"
        print(message)
        history.append(message)

    except ValueError:
        print("Invalid input! Enter a number.")￼Enter
