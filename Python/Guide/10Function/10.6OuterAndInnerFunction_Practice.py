def outer(name):
    def inner():
        return "Hello, " + name
    return inner()

greeting = outer("Alice")
print(greeting)  


'''Explanation
outer(name)
This is the outer function which takes one argument: name.

inner()
This is an inner function, defined inside outer() and has access to the name variable from the outer function.

return inner()
The outer function calls and returns the result of the inner function.
'''
