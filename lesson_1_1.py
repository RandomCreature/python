#Creating cycle
while True:
#Suggesting user to enter the variable. For our purpose, we make a caution about its type.    
    i=int(input('Please, enter the variable\'s value (it must be integer): '))
    if 0<i<10:
        print('Thanks, that\'s what I needed. Its square is '+str(i**(2)))
        break
    else:
        print('Oh, sorry, there\'s a condition - the variable value should be between 0 and 10...Please, try again.')
        continue
