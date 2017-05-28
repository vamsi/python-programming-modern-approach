import random

guesses_taken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guesses_taken < 6:
    print('Take a guess.')  # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guesses_taken += 1

    if guess < number:
        # There are eight spaces in front of print.
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print('Good job, ' + myName + '! You guessed my number in ' +
          guesses_taken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
