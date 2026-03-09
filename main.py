def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:

    # add the new guess to the guessed letters
    new_guessed_letters = guessed_letters + [guess]

    # if the guess is not in the secret word, lose a life
    if guess not in secret_word:
        lives = lives - 1

    return new_guessed_letters, lives