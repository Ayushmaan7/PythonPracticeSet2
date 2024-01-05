def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    try:
        choice = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").upper()

        if choice == 'C':
            celsius_value = float(input("Enter temperature in Celsius: "))
            converted_temperature = celsius_to_fahrenheit(celsius_value)
            print(f"{celsius_value} degrees Celsius is equal to {converted_temperature:.2f} degrees Fahrenheit.")

        elif choice == 'F':
            fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
            converted_temperature = fahrenheit_to_celsius(fahrenheit_value)
            print(f"{fahrenheit_value} degrees Fahrenheit is equal to {converted_temperature:.2f} degrees Celsius.")

        else:
            print("Invalid choice. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")
