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

grade = int(input("Enter grade: "))

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