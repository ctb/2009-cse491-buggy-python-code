import random
secret = random.randint(1, 100)

guess = -1
while guess != secret:
    guess = input("Guess a number!")
    guess = int(guess)
    if guess > secret:
        print "Too high!"
    else:
        print "Too low!"

print "You got it!"
