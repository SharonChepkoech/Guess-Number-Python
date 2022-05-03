import random
max_num = 30
random_number = random.randint(1, max_num)
guess = 0
while guess != random_number:
        guess= int(input(f"Guss the number between 1 & {max_num}:"))
        if guess  < random_number:
            print ("Wrong, too low!")
        elif guess > random_number:
            print("Wrong, too high!")    
        else:
            print(f"That's right! Random number is {random_number}")