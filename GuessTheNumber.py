import random
random_number = random.randint(1,20)

print("Guess the number in between the 1 and 20")
print("You have only six Options to Try...")
guess_number = int(input())

conditon = True
count = 0
while (conditon):
    if guess_number > 20 or guess_number < 1:
        print("Your Expectin the Number not in between the range...so try again.")
        guess_number = int(input("Guess the number again...between the range ONLY."))
        print()
    else:
        if guess_number < random_number:
            print("Your expecting lower value! Try again.......You have remain {} chances".format(6-count))
            guess_number = int(input("Guess Number again..."))
            print()

        if count == 5:
            print("Your Out of Options...And The Correct Number is {}".format(random_number))
            print()
            conditon = False
            
        elif guess_number > random_number:
            print("Guess Number is higher value! Try again. You have remain {} chances".format(6-count))
            guess_number = int(input("Guess Number again..."))
            print()

        elif guess_number == random_number:
            print("HOLA....That's the correct Number....Perfect.")
            print()
            conditon = False
    count += 1 
    
