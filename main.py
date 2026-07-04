import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts_left = 7
    
    while attempts_left > 0:
        print(f"\nYou have {attempts_left} attempts remaining.")
        user_input = input("Take a guess: ").strip()
        
        try:
            guess = int(user_input)
        except ValueError:
            print("That's not a valid number. Try entering digits only.")
            continue
            
        if guess < 1 or guess > 100:
            print("Out of bounds! Please guess a number between 1 and 100.")
            continue
            
        if guess == secret_number:
            print(f"Spot on! You got it in {8 - attempts_left} tries.")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
            
        attempts_left -= 1
        
    print(f"\nGame over! You ran out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nWant to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Thanks for playing!")
            break