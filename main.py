import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&\#*();:.,'

number = input('Amount of password to generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere is your password:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)    