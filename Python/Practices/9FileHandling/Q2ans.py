'''
Write a function log_message(msg) that writes the message to log.txt. 
If the file already exists, append the message to a new line.
'''

def log_message(msg):
    with open('Q3ans.txt', 'at') as f:
        f.write(msg)


while True:
    msg = input("Enter something you want to append to the file (q to quit): ")
    if msg == 'q':
        break
    log_message(msg)

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/9FileHandling (main) $ python Q2ans.py
Enter something you want to append to the file (q to quit): Sean
Enter something you want to append to the file (q to quit): Tai
Enter something you want to append to the file (q to quit): Han
Enter something you want to append to the file (q to quit): Xuan
Enter something you want to append to the file (q to quit): q
@seantaihx ➜ .../Practice/Python/Practices/9FileHandling (main) $ 
'''