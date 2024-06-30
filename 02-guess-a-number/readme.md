# Guess the Number Game Specification

## Overview
Create a number guessing game where the computer randomly selects a number between 1 and 100, and the user has to guess it. The program should provide feedback if the guess is too high or too low and keep track of the number of attempts made by the user.

## Requirements

### Functional Requirements
1. **Random Number Generation:**
   - The program should generate a random number between 1 and 100 at the start of the game.

2. **User Input:**
   - The program should prompt the user to guess the number.
   - The user should be able to enter their guess.

3. **Feedback:**
   - The program should inform the user if their guess is too high, too low, or correct.

4. **Attempts Counter:**
   - The program should keep track of the number of attempts made by the user.
   - When the user guesses the correct number, the program should display the total number of attempts.

### Non-Functional Requirements
1. **Usability:**
   - The program should have clear and concise prompts.
   - The program should handle invalid inputs gracefully, prompting the user to enter valid data.

2. **Efficiency:**
   - The program should efficiently manage user input and provide real-time feedback.

## Implementation Details

### User Interface
- The program will run in the console/terminal.
- Use the `input()` function to get user input.
- Use the `random` module to generate a random number.

### Example Interaction
```plaintext
Welcome to the Guess the Number Game!
I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too high!
Enter your guess: 25
Too low!
Enter your guess: 37
Congratulations! You guessed the number in 3 attempts.
