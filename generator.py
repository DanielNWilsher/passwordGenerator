'''
Password Generator
Daniel Wilsher
7/15/21
10:40AM
'''


import random
import string
string.ascii_letters
def getPassword():
    password = int(input('Enter a password length between 12 and 16 '))

    if type(password) == str:
        print('Enter a number you numpty.')
        getPassword()
    elif type(password) == int:
        return password
    else:
        try:
            int(password)
        except ValueError:
            try:
                int(password)
            except ValueError:
                print('Enter a number you numpty.')

def generator(password):
    if password < 12 :
        print('Weakness disgusts me, pick a longer password.')
    elif password >= 12: 
        print('Good, Good, Give me a moment.')
    elif password > 16:
        print('Don;t you know how to read? try again')
    elif type(password) == str or type(password) == float:
        print('Enter a number you numpty.')
    else:
        print('what have you done? how did you break this? Try Again')
        generator(password)
    
    passwordStorage = []

    for i in range(password):
        if i % 2:
            passwordStorage.append(str(random.randint(0, 9))) 
        else:
            passwordStorage.append(str(random.choice(string.ascii_letters)))
    print('Here is your password: ')
    print('-----------------------')
    print(*passwordStorage, sep='')


def main():
    generator(getPassword())


if __name__ == '__main__':
    main()