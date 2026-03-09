# Guess The Word Game

This project implements the minimal core of a hangman-style word guessing game.

## Function

`update_game_state` updates the game state after a new letter guess.

Inputs:
- `secret_word`: the word to guess
- `guessed_letters`: list of letters already guessed
- `guess`: the new guessed letter
- `lives`: remaining lives

Returns:
- updated guessed letters list
- updated number of lives

## Running tests

To run the tests:

```bash
python main.py