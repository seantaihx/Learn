'''
Grading System (Comparison + If-Elif-Else)
Ask for a score (0-100).
Use conditions to print the grade:
	•	90-100: A
	•	80-89: B
	•	70-79: C
	•	60-69: D
	•	Below 60: F
'''

#Get user user input and change the type into integer type
grade = int(input("Enter grade: "))

#For each grade match the respective lettergrade
if grade >= 90:
    lettergrade = 'A'
elif grade >= 80:
    lettergrade = 'B'
elif grade >= 70:
    lettergrade = 'C'
elif grade >= 60:
    lettergrade = 'D'
else:
    lettergrade = 'F'

print(f'The lettergrade of {grade} is {lettergrade}.')


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ python Q3ans.py
Enter grade: 76
The lettergrade of 76 is C.
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ 
'''