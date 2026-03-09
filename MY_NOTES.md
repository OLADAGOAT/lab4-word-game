# Word Game Notes

## App States
What is the initial state of the game when it first starts? (For example, is there a setup phase where a word is chosen or displayed?)

What happens during the main gameplay loop? (How does the game respond to player inputs, like guesses?)

What are the key decision points that could change the game's behavior? (For instance, when does the game check if a guess is correct, partially correct, or incorrect?)

What are the possible outcomes or endings? (How does the game determine if the player has won, lost, or if there's an intermediate status like "almost there"?)

Are there any pauses, resets, or special modes? (Could the game have states for restarting, pausing, or handling errors?)
## App Variables
What core data does the game need from the very beginning, before any guesses are made? (For example, something fixed that defines the challenge.)

What does the game need to record and update with each player action? (How might it keep track of what the player has tried or revealed?)

Are there any limits or counters that change over time? (What could enforce rules like maximum attempts or time constraints?)

How does the game know its current status? (What might indicate whether it's still in progress, finished, or in a specific phase?)

What about user-specific or session data? (Could there be anything related to the player's identity, score, or preferences?)

## App Rules and Invariants
What aspects of the game should never change once the game begins? (For example, is there something that must stay fixed to keep the challenge intact?)

What constraints should the game place on player inputs or actions? (How might it prevent invalid guesses, like repeating letters or going beyond limits?)

What must the game always check or enforce to ensure it's playable? (For instance, what prevents the game from breaking if something unexpected happens?)

How does the game determine valid progress or outcomes? (What rules ensure that wins, losses, or partial successes are calculated correctly?)

Are there any safety or boundary conditions? (What invariants protect against errors, like negative counters or impossible states?)

## App Bugs
What could happen if the player enters unexpected input? (For example, how might non-letter characters, empty strings, or overly long guesses break the game?)

How might errors occur in tracking guesses or progress? (What if the game doesn't update variables correctly after each turn, or miscalculates remaining attempts?)

What edge cases exist in the game's logic? (For instance, what happens if the secret word has repeated letters, or if the player guesses the word instantly?)

How could state transitions cause problems? (What if the game doesn't properly switch from "playing" to "won" or "lost," leading to continued play after the game should end?)

What about data integrity? (How might variables become invalid, like negative counters or corrupted word displays?)