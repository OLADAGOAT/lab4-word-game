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
    new_guessed_letters = guessed_letters + [guess]

    if guess not in secret_word:
        lives = lives - 1

    return new_guessed_letters, lives


def test_update_game_state():
    """Test cases for update_game_state function."""
    # Correct guess
    result = update_game_state("apple", ["a"], "p", 5)
    assert result == (["a", "p"], 5), f"Correct guess failed: {result}"

    # Incorrect guess
    result = update_game_state("apple", ["a"], "z", 5)
    assert result == (["a", "z"], 4), f"Incorrect guess failed: {result}"

    # Duplicate correct guess
    result = update_game_state("apple", ["p"], "p", 5)
    assert result == (["p", "p"], 5), f"Duplicate correct guess failed: {result}"

    # Case sensitivity
    result = update_game_state("Apple", ["a"], "A", 5)
    assert result == (["a", "A"], 5), f"Case sensitivity failed: {result}"

    # Multiple char guess
    result = update_game_state("apple", [], "pp", 5)
    assert result == (["pp"], 5), f"Multiple char guess failed: {result}"

    print("All tests passed!")


if __name__ == "__main__":
    test_update_game_state()