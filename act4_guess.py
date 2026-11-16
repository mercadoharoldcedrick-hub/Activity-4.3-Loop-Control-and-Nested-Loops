
secret = 27
tries = 0

while True:
    guess = int(input("Guess: "))
    tries += 1

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct! You got it in", tries, "tries.")
        break
