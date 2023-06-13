import random

ans = random.randint(1,100)
tries = []
play = True
print("Guess my number between 1 and 100")
num = int(input("Enter your guess (1-100):"))
tries.append(num)
while play:
    if num > 100 or num < 1:
        print("Invalid input.",end=" ")
        num = int(input("Guess again:"))
    else:
        if num < ans:
            print("Too low.",end=" ")
            num = int(input("Guess again:"))
            tries.append(num)
        elif num > ans:
            print("Too high.",end=" ")
            num = int(input("Guess again:"))
            tries.append(num)
        elif num == ans:
            print("Congratulations! You guessed the number in %d tries." % (len(tries)))
            print("Previous guesses :",tries)
            play = False
hist = [0]*10
for i in tries:
    range_num =  i //10
    hist[range_num] +=1
    
print("Histogram:")
for i in range(10):
    print("%03d-%03d:" % (1+10*i, 10+10*i),"*"*hist[i])
