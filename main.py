"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Katarina Zorvan
email: katarina.zorvan@gmail.com
"""
import random
import time

print(f"Hi there! \n{'-' * 50} \nI've generated a random 4 digit number for you. \nLet's play a bulls and cows game.\n {'-' * 50}")

# Secret number function
def generate_secret_number():
    digits = list("0123456789")
    random.shuffle(digits)
    if digits[0] == "0":
    
        for i in range(1, len(digits)):
            if digits[i] != "0":
                digits[0], digits[i] = digits[i], digits[0]
                break
    return "".join(digits[:4])

secret_number = generate_secret_number()

#checking whether the input is a digit, doesn't begin with 0, it's exactly 4 digits, doesn't contain duplicates

def get_valid_guess():

    while True:
        user_number = input("Enter a number: ")

        if not user_number.isdigit():
            print("Please enter numbers only")
            continue

        if user_number[0] == "0":
            print("The number cannot begin with 0")
            continue

        if len(user_number) < 4:
            print("The number is too short. It must be 4 digits.")
            continue
        elif len(user_number) > 4:
            print("The number is too long. It must be 4 digits.")
            continue

        if len(set(user_number)) != len(user_number):
            print("The number must only contain unique numbers.")
            continue

        break
    return user_number

#bulls and cows function
def bulls_and_cows(user_number,secret_number):
    bulls_count = 0
    cows_count = 0
    not_bulls = []

    for i in range(len(user_number)):
        if user_number[i] == secret_number[i]:
            bulls_count +=1
        else:
            not_bulls.append(i)

    user_remaining = [user_number[i] for i in not_bulls]
    secret_remaining = [secret_number[i] for i in not_bulls]

    for i in user_remaining:
            if i in secret_remaining:
                cows_count +=1
    return bulls_count, cows_count

guess_counter = 0

start_time = time.time()
while True:
    user_number = get_valid_guess()
    guess_counter += 1
    bulls, cows = bulls_and_cows(user_number, secret_number)
    if bulls != 4:
        bull_word = "bull" if bulls == 1 else "bulls"
        cow_word = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_word}, {cows} {cow_word}")
    else:
        end_time = time.time()
        duration = end_time - start_time
        print(f"Correct, you've guessed the right number in {guess_counter} guesses, and it took you {round(duration)} seconds!\n{'-' * 50}\nThat's amazing!")
        break

    






# if bulls_count == 1:
#     print("1 bull")
# else:
#     print(f"{bulls_count} bulls")
# if cows_count == 1:
#     print("1 cow")
# else:
#     print(f"{cows_count} cows")



