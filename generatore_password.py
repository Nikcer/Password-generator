import random
import string

print("Welcome to the Random Password Generator!")
print("The number of characters in the password must be between 8 and 15.")


while True:
    len_pswd = int(input("Choose password length: "))

    if len_pswd >= 8 and len_pswd <= 15:
        print(f"The password length is {len_pswd} characters")

        break

    else:
        print("The number of characters does not meet the requirements! Enter again.")
        continue




addChr = input(("Add symbols to your password? y/n: "))
if  addChr.lower() == "y":
    symbols = string.punctuation
else: 
    symbols = ""
    print("The password does not contain symbols")
    

characters = string.ascii_letters
numbers = string.digits

password = ""
for i in range(0, len_pswd):
    password += random.choice(characters + numbers + symbols)
print("The password is:", password)
print("Thank you!")
        

    

