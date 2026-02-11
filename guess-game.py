winner = 9
count = 0
tries = 3

while count < tries:
    guess = int(input('Guess: '))
    count += 1
    if guess == winner:
        print('You are the winner')
        break
else:
    print('3 tries over all wrong')
    

