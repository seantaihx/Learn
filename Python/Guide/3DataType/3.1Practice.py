a = 1
b = 1.5
c = 1 + 2j
d = "4"
e = "True"
f = True

print(type(a))              #Check type
a = str(a)                  #Change the type of the value in the variable
print(type(a))              #Check again the type
print('\n')


print(type(b))
b = int(b)
print(b)
print(type(b))
print('\n')


print(type(c))
c = str(c)
print(type(c))
print('\n')


print(type(d))
d = int(d)
print(type(d))
print('\n')


print(type(e))
e = bool(e)
print(type(e))
print('\n')


print(type(f))
f = str(f)
print(type(f))
print('\n')

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/3DataType (main) $ python 3.1Practice.py


<class 'int'>
<class 'str'>


<class 'float'>
1
<class 'int'>


<class 'complex'>
<class 'str'>


<class 'str'>
<class 'int'>


<class 'str'>
<class 'bool'>


<class 'bool'>
<class 'str'>


@seantaihx ➜ .../Practice/Python/Guide/3DataType (main) $ 
'''