secret_number = 100
guess_count=0
guess_limit = 3

start = int(input("Welcome to M Guess App press 1 to continue and 0 to terminate ?"))

while guess_count < guess_limit and start == 1 and not start == 0:
    guess_number = int(input("Guess Number?  "))
    guess_count = guess_count + 1

    if guess_number == secret_number:
        print("Congrats! You won")
        break
else:
    print("Sorry you Failed ")

    
