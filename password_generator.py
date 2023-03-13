import random

numbers = "123456789"
lower_case = "abcdefghijklmnopqrstuvwyxz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
symbols = "?@#$%^&*"

while True:
    while True:
        try:
            password_length = int(input("How long will be the password? (numbers only)\n"))
            break
        except:
            print("This is not a number. Try again.")
    print(f"Password length: {password_length}")
    password = ""
    for x in range(password_length):
        random_choice = random.randrange(0,4)
        if random_choice == 0:
            temp_password = lower_case[random.randrange(26)]
        elif random_choice == 1:
            temp_password = upper_case[random.randrange(26)]
        elif random_choice == 2:
            temp_password = numbers[random.randrange(9)]
        else:
            temp_password = symbols[random.randrange(8)]
        password = temp_password + password

    print(f"Your password is: {password}")
    while True:
        users_answer = input("Do you want to continue? (yes/no)\n")

        if users_answer == "no":
            quit()
        elif users_answer == "yes":
            break
        else:
            print("Wrong answer!")
