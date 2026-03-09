# Word Game Notes

## App States
What is the game's condition right at the beginning, before any guesses? (Is there a phase for preparing the word or initializing the display?)
What state is the game in while the player is actively making guesses? (How does it handle correct and incorrect inputs during this ongoing phase?)
What happens when the player successfully guesses the entire word? (What state signals a win?)
What occurs if the player exhausts all allowed wrong guesses without completing the word? (What state indicates a loss?)
Are there any other transitional or special states? (For example, could there be a pause, restart, or error-handling state?)
## App Variables
What fixed information defines the core challenge? (For example, something that doesn't change once set.)
What needs to be updated as the player guesses? (How might you track what letters have been tried or revealed?)
How do you monitor attempts or limits? (What counts wrong guesses or enforces the maximum allowed?)
What represents the current game display or progress? (How do you show the word's state to the player?)
Are there any flags for the game's overall status? (What indicates if it's still active, won, or lost?)

## App Rules and Invariants
What are the core rules for starting and playing? (For example, how is the secret word chosen, and what constitutes a valid guess?)
How are correct and incorrect guesses handled? (What happens when a letter is in the word versus not, and how does that affect the display or attempts?)
What determines the end of the game? (Under what conditions does the player win or lose?)
What invariants must always be true? (For instance, what can't change or go below zero, and what ensures the game remains fair?)
Are there rules for special cases? (How does the game handle repeated letters, case sensitivity, or edge scenarios like guessing the whole word at once?)

## App Bugs
 What could go wrong with player input? (For example, how might non-alphabetic characters, uppercase/lowercase mismatches, or empty inputs break the game?)
How might tracking guesses fail? (What if the game doesn't properly update or check for already-guessed letters, or miscounts wrong attempts?)
What edge cases exist in word handling? (For instance, what happens with words containing spaces, hyphens, or repeated letters?)
How could state transitions cause problems? (What if the game doesn't correctly detect a win/loss, allowing play to continue indefinitely or ending prematurely?)
What about display or feedback issues? (How might the word reveal incorrectly, or counters go negative/invalid?)