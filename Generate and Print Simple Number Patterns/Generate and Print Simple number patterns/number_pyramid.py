# Simple Number Pyramid Pattern Generator

def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        print(' ' * (rows - i), end='')
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  # Newline after each row

def print_left_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

def print_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

if __name__ == "__main__":
    print("Select a number pattern to print:")
    print("1. Left-aligned triangle")
    print("2. Right-aligned triangle")
    print("3. Pyramid")
    print("4. Inverted pyramid")
    try:
        choice = int(input("Enter your choice (1-4): "))
        n = int(input("Enter the number of rows: "))
        if choice == 1:
            print_left_triangle(n)
        elif choice == 2:
            print_right_triangle(n)
        elif choice == 3:
            print_number_pyramid(n)
        elif choice == 4:
            print_inverted_pyramid(n)
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
    except ValueError:
        print("Please enter a valid integer.")
