import random


WORDS = ["apple", "banana", "grapes", "peach", "mango"]
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")


def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """Update game state after a guess.

    Adds the new guess to guessed_letters and decreases lives
    if the guess is not in the secret word.
    """
    new_guessed_letters = guessed_letters + [guess]

    if guess not in secret_word:
        lives = lives - 1

    return new_guessed_letters, lives


def choose_word(words: list[str]) -> str:
    """Return a random word from the list."""
    return random.choice(words)


def mask_word(secret_word: str, guessed_letters: list[str]) -> str:
    """Return the masked word using guessed letters only."""
    masked = ""

    for letter in secret_word:
        if letter in guessed_letters:
            masked += letter
        else:
            masked += "_"

    return masked


def get_incorrect_guesses(secret_word: str, guessed_letters: list[str]) -> list[str]:
    """Return guessed letters that are not in the secret word."""
    incorrect = []

    for letter in guessed_letters:
        if letter not in secret_word and letter not in incorrect:
            incorrect = incorrect + [letter]

    return incorrect


def is_game_won(secret_word: str, guessed_letters: list[str]) -> bool:
    """Return True if all letters in the secret word were guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def is_valid_guess(guess: str, guessed_letters: list[str]) -> bool:
    """Check that the guess is a single new alphabetic character."""
    return len(guess) == 1 and guess.isalpha() and guess not in guessed_letters


def get_auto_guess(guessed_letters: list[str]) -> str:
    """Return a letter the computer has not guessed yet."""
    available_letters = []

    for letter in ALPHABET:
        if letter not in guessed_letters:
            available_letters = available_letters + [letter]

    return random.choice(available_letters)


def play_game(words: list[str]) -> None:
    """Run one full normal game."""
    secret_word = choose_word(words)
    guessed_letters: list[str] = []
    lives = 6

    while lives > 0 and not is_game_won(secret_word, guessed_letters):
        print("\nWord:", " ".join(mask_word(secret_word, guessed_letters)))
        print("Guessed letters:", guessed_letters)
        print("Incorrect guesses:", get_incorrect_guesses(secret_word, guessed_letters))
        print("Lives left:", lives)

        guess = input("Guess a letter: ").lower()

        if not is_valid_guess(guess, guessed_letters):
            print("Invalid guess. Enter one new letter only.")
        else:
            guessed_letters, lives = update_game_state(
                secret_word,
                guessed_letters,
                guess,
                lives
            )

    if is_game_won(secret_word, guessed_letters):
        print("\nYou win! The word was:", secret_word)
    else:
        print("\nYou lose! The word was:", secret_word)


def auto_play_game(words: list[str]) -> None:
    """Run one full auto-play game."""
    secret_word = choose_word(words)
    guessed_letters: list[str] = []
    lives = 6

    print("\nAuto Play Mode started.")

    while lives > 0 and not is_game_won(secret_word, guessed_letters):
        print("\nWord:", " ".join(mask_word(secret_word, guessed_letters)))
        print("Guessed letters:", guessed_letters)
        print("Incorrect guesses:", get_incorrect_guesses(secret_word, guessed_letters))
        print("Lives left:", lives)

        guess = get_auto_guess(guessed_letters)
        print("Computer guesses:", guess)

        guessed_letters, lives = update_game_state(
            secret_word,
            guessed_letters,
            guess,
            lives
        )

    if is_game_won(secret_word, guessed_letters):
        print("\nComputer won! The word was:", secret_word)
    else:
        print("\nComputer lost! The word was:", secret_word)


def main() -> None:
    """Run the game and support replay."""
    play_again = "y"

    while play_again == "y":
        print("\nChoose mode:")
        print("1. Normal play")
        print("2. Auto play")

        choice = input("Enter 1 or 2: ")

        if choice == "1":
            play_game(WORDS)
        elif choice == "2":
            auto_play_game(WORDS)
        else:
            print("Invalid choice.")

        play_again = input("\nDo you want to start again? (y/n): ").lower()


if __name__ == "__main__":
    main()