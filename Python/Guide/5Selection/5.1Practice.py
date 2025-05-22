respond = input("Do you want to guess how old am I: ")

if respond=='YES' or respond=='yes' or respond=='Yes':              #First if condition
    guess = input('What\'s your guess (between 18 to 20): ')

    match guess:                            #match the variable guess
        case ('18' | '19'):                 #case 1
            print("NO")
        case '20':                          #case 2
            print("Correct!")

elif respond=='NO' or respond=='no' or respond=='No':               #Second if condition
    print("OK then, bye")

else:                                                      #Every other possible condition that's not mentioned
    print("What?")

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/5Selection (main) $ python 5.1Practice.py
Do you want to guess how old am I: yes
What's your guess (between 18 to 20): 18
NO

@seantaihx ➜ .../Practice/Python/Guide/5Selection (main) $ python 5.1Practice.py
Do you want to guess how old am I: yes
What's your guess (between 18 to 20): 20
Correct!

@seantaihx ➜ .../Practice/Python/Guide/5Selection (main) $ python 5.1Practice.py
Do you want to guess how old am I: no
OK then, bye

@seantaihx ➜ .../Practice/Python/Guide/5Selection (main) $ python 5.1Practice.py
Do you want to guess how old am I: 2e
What?
'''