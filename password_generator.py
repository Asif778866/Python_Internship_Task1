import random
import string

print("===== Password Generator =====")

while True:
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            continue

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        print("Generated Password:", password)

        again = input("Do you want to generate another password? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")