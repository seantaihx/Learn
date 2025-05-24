age = int(input("What's your age: "))
print("Access Level: \n  1 = Teen Mode (age 13-17) \n  2 = Adult Mode (18+) \n  3: Exit")
level = input("Enter level: ")

check = isinstance(age, int)

if check:
    match level:
        case '1':
            if age >= 13 and age <= 17:
                print("Access granted")
            else:
                print("Access deny")
        case '2':
            if age >= 18:
                print("Access granted")
            else:
                print("Access deny")
        case '3':
            print("Bye")
