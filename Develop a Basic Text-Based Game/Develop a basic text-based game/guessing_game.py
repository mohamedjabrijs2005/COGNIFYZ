import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    number = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = input("Take a guess: ")
        attempts += 1
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        
        if guess < 1 or guess > 10:
            print("Your guess is out of range. Try again.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()
