def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """Update game state after a guess in word guessing game.

    Adds guess to guessed_letters. Decreases lives if guess not in secret_word.

    Args:
        secret_word: The target word (case-sensitive).
        guessed_letters: Current list of guessed letters.
        guess: New letter guess (should be single char, not validated here).
        lives: Remaining lives.

    Returns:
        Tuple of (updated_guessed_letters, updated_lives).

    Note: Does not check for duplicates or invalid inputs.
    """
    # add the new guess to the guessed letters
    new_guessed_letters = guessed_letters + [guess]

    # if the guess is not in the secret word, lose a life
    if guess not in secret_word:
        lives = lives - 1

    return new_guessed_letters, lives