def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    temp = float(input("Enter the temperature value: "))
    direction = input('Choose conversion direction ("C to F" or "F to C"): ').strip().upper()

    if direction == "C TO F":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {result:.2f}°F")
    elif direction == "F TO C":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is equal to {result:.2f}°C")
    else:
        print('Invalid conversion direction. Please enter "C to F" or "F to C".')

if __name__ == "__main__":
    main()