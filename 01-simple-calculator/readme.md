# Simple Calculator Program

## Overview
Create a simple calculator program in Python that can perform basic arithmetic operations: addition, subtraction, multiplication, and division. The program should take user input for the operation and the numbers involved, then display the result.

## Requirements

### Functional Requirements
1. **User Input:**
   - The program should prompt the user to enter two numbers.
   - The program should prompt the user to choose an operation (addition, subtraction, multiplication, division).

2. **Operations:**
   - The program should be able to perform the following operations:
     - Addition (`+`)
     - Subtraction (`-`)
     - Multiplication (`*`)
     - Division (`/`)

3. **Output:**
   - The program should display the result of the chosen operation.
   - If the user tries to divide by zero, the program should display an error message.

### Non-Functional Requirements
1. **Usability:**
   - The program should have clear and concise prompts.
   - The program should handle invalid inputs gracefully, prompting the user to enter valid data.

2. **Modularity:**
   - The program should use functions to perform each arithmetic operation.
   - There should be a main function to control the program flow.

## Implementation Details

### User Interface
- The program will run in the console/terminal.
- Use `input()` function to get user input.

### Example Interaction
```plaintext
Enter the first number: 10
Enter the second number: 5
Choose an operation (+, -, *, /): +
Result: 10 + 5 = 15
