import random

def choose_word():
    words = ["apple", "wine", "car", "sun", "flower", "life", "bottle", "book", "table", "chair","python"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "* "
    return display.strip()

def get_guess():
    guess = input("guess a letter: ")
    return guess.strip()

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 8

    print("Wolcome to Hang man game! ")
    print("you need to guess the random word")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"number of attempts: {attempts}")
        
        guess = get_guess()
        
        if guess in guessed_letters:
            print("you already guessed this word")
        elif guess in word:
            guessed_letters.add(guess)
            print("good guess!")
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print("")
        
        if all(letter in guessed_letters for letter in word):
            print(f"you win,the word is : {word}")
            break
    else:
        print(f"you lost, the word was: {word}")

if __name__ == "__main__":
    play_game()
