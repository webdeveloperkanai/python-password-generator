# Author : Web Developer Kanai
import random  
from datetime import datetime 
import constant
now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
chars = constant.chars
chars_list = list(chars)
guess_password = ""
length = int(input("Enter password length : "))
count = int(input("How many password do you want to generate ? "))
passwords = []
for x in range(0,count): 
    guess_password = random.choices(chars_list,k=length) 
    print(''.join(guess_password))
    passwords.append(''.join(guess_password)+"\n") 

if len(passwords)>0:
    file = open( f'{now}.password.txt', 'w')
    file.write(''.join(passwords))
    file.close()