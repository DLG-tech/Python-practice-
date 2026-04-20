import random
i = random.randint(1, 100)
while True:
  guess_str = input("guess the number im thinking of it is between 1 and 100: ")
  guess = int(guess_str)
  if guess < i:
    print("higher")
  elif guess > i:
    print("lower")
  else: 
    print("congratulations you guessed the right number "+ str(i) + "!")
    break
 
