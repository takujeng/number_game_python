## Guest Random Number from 1 to 10 ##
## Artha Nugraha Jonar ##
import random

random_number = random.randint(1,10)
guess_number = []
allowed_gueses = 5

while len(guess_number)<5:
    input_number = input ("guess your number from 1 to 10: ")
    try:
        pass_number = int(input_number)
    except:
        print("it's not a number")
        break

    if pass_number < 1 or pass_number > 10:
        print ("your number not in range")
        break
    
    guess_number.append(pass_number)
    if pass_number > random_number:
        print("your guess bigger than number. you try #{}".format(len(guess_number)))
        continue
    elif pass_number < random_number:
        print("your guess smaller than number. you try #{}".format(len(guess_number)))
        continue
    else:
        print("{} is correct number".format(pass_number))
        print("you are guess {} times".format(len(guess_number)))
        break