import random 

number_i_think = random.randint(1, 100)
number_of_guesses = 0

while number_of_guesses < 10:
    print('Enter your guess:')
    guess = input()
    guess = int(guess)
    number_of_guesses = number_of_guesses + 1

    if guess < number_i_think:
        print('Too low')
    elif guess > number_i_think:
        print('Too high')
    elif guess == number_i_think:
        print('Congratulations! That is the number I was thinking of.')

    if number_of_guesses >= 10:
        print(f'Aww you ran out of guesses.The  number I was thinking of was {number_i_think}')