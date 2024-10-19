import random
def user_guess_start(secretNUMBER , lowerBOND , higherBOND):
    guess = int(input(f"Guess the number between {lowerBOND} and {higherBOND} : "))
    
    if guess == secretNUMBER : 
        print("Yayyy , You Guessed the right number :)")
        return
    elif guess > secretNUMBER : 
        print("You Guessed the too high  :(")
        user_guess_start(secretNUMBER , lowerBOND , guess - 1)
    elif guess < secretNUMBER : 
        print("You guessed the too low :(")
        user_guess_start(secretNUMBER ,  guess + 1 , higherBOND )

def start_guessing_game():
    lowerBOND = int(input("Enter the lower boundry of the limit : "))
    higherBOND = int(input("ENter the Higher boundary of the limit : "))
    secretNUMBER = random.randint(lowerBOND , higherBOND)
    user_guess_start(secretNUMBER , lowerBOND , higherBOND)
start_guessing_game()
