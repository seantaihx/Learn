a = input("Which house does Harry Potter got into (Gryffindor, Hufflepuff, RavenClaw, Slytherin): ")

match a:
    case 'Hufflepuff'|"Ravenclaw"|"Slytherin":
        print("Wrong! It's Gryffindor!\n")
    case 'Gryffindor':
        print("You're right!\n")

'''Explanation
We ask for user to input their answer

Then we start matching which answer does the user input, 
if not Gryffindor then print theyre wrong, if yes, then theyre right
'''

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Guide/5Selection/5.3Matching_Practice.py
Which house does Harry Potter got into (Gryffindor, Hufflepuff, RavenClaw, Slytherin): Ravenclaw 
Wrong! It's Gryffindor!

@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Guide/5Selection/5.3Matching_Practice.py
Which house does Harry Potter got into (Gryffindor, Hufflepuff, RavenClaw, Slytherin): Gryffindor
You're right!
'''