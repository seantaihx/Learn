#Iterator
'''
Iterator: Elements inside iterables
format: iterator_variable = iter(mutuple)

To access the next iterator
format: print(next(iterator_variable))

!!!for loop creates an iterator object and execute the next() function for each loop
'''


#Create Iterator
'''
format:
class class_name:
  def __iter__(self):
    statement

'''


#Stop Iteration
'''
StopIteration: just stop the iteration usually in def __next__(self):

format: raise StopIteration
'''


#yield
'''
yield: a keyword used in a function to turn it into a generator
	   It pauses the function and returns a value to the caller, 
       the state of the function is saved, so it can resume from where it left off when called again

format:
def function(pa):
	statement
    loop condition:
    	yield counter
        counter+=1
'''