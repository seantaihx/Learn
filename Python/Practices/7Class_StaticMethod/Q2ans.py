'''
Create a class User with a class variable user_count.
	•	Add a @classmethod called create_guest() that returns a user with name "Guest" and increases user_count.
 '''

class User:
    user_count = 0  # Class variable to track number of users

    def __init__(self, name):
        self.name = name
        User.user_count += 1

    @classmethod
    def create_guest(cls):
        return cls("Guest")

# Create a regular user
user1 = User("Alice")

# Create a guest user
guest = User.create_guest()

# Output names and user count
print(user1.name)   
print(guest.name)   
print(User.user_count)  

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/7Class_StaticMethod (main) $ python Q2ans.py
Alice
Guest
2
@seantaihx ➜ .../Practice/Python/Practices/7Class_StaticMethod (main) $ 
'''