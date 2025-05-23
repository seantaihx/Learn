'''
Math Challenge (Assignment + Conditions)
Start with points = 0
Ask the user:
“What is 7 * 8?”
	•	If right, add 5 points (+=)
	•	If wrong, subtract 2 points (-=)
Print the final score.
'''

points = 0

ans = int(input("What is 7 * 8: "))
if ans != 7*8:
    points -= 2
else:
    points += 5

print('Your final score is {}'.format(points))