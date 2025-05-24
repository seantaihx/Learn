def isint(s):
    try:
        v = int(s)
        return True
    except ValueError:
        return False

def isfraction(s):
    s = s.split('/')
    if len(s) == 1:
        return isint(s[0])
    elif len(s) == 2:
        return isint(s[0]) and isint(s[1]) and (int(s[1]) != 0)
    else:
        return False

def gcd(a,b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a%b)

def num(f):
    f = f.split('/')
    return int(f[0])

def den(f):
    f = f.split('/')
    if len(f) == 1:
        return 1
    else:
        return int(f[1])

def reduce(f):
    n,d = num(f), den(f)
    g = gcd(n,d)
    n = n//g
    d = d//g
    if d < 0:
        n = -n
        d = -d
    if d == 1:
	    return str(n)
    return str(n) + '/' + str(d)

def add(f1, f2):
    n1, d1 = num(f1), den(f1)
    n2, d2 = num(f2), den(f2)
    n = n1*d2 + n2*d1
    d = d1*d2
    f = str(n) + '/' + str(d)
    return reduce(f)

def sub(f1, f2):
    n1, d1 = num(f1), den(f1)
    n2, d2 = num(f2), den(f2)
    n = n1*d2 - n2*d1
    d = d1*d2
    f = str(n) + '/' + str(d)
    return reduce(f)

def mul(f1, f2):
    n1, d1 = num(f1), den(f1)
    n2, d2 = num(f2), den(f2)
    n = n1*n2
    d = d1*d2
    f = str(n) + '/' + str(d)
    return reduce(f)

def div(f1, f2):
    n1, d1 = num(f1), den(f1)
    n2, d2 = num(f2), den(f2)
    n = n1*d2
    d = d1*n2
    f = str(n) + '/' + str(d)
    return reduce(f)

def main():
    while True:
        s = input('Enter q to quit or a pair of fraction: ')
        if s == 'q':
            break
        s = s.split(' ')
        if isfraction(s[0]) == False or  isfraction(s[1]) == False:
            print('Invalid input')
            continue
        f = add(s[0], s[1])
        print('{} + {} = {}'.format(s[0], s[1], f))

        s = input('Enter another pair of fraction for subtraction: ')
        s = s.split(' ')
        if isfraction(s[0]) == False or  isfraction(s[1]) == False:
            print('Invalid input')
            continue
        g = sub(s[0], s[1])
        print('{} - {} = {}'.format(s[0], s[1], g))

        s = input('Enter another pair of fraction for multiplication: ')
        s = s.split(' ')
        if isfraction(s[0]) == False or  isfraction(s[1]) == False:
            print('Invalid input')
            continue
        m = mul(s[0], s[1])
        print('{} * {} = {}'.format(s[0], s[1], m))

        s = input('Enter another pair of fraction for division: ')
        s = s.split(' ')
        if isfraction(s[0]) == False or  isfraction(s[1]) == False:
            print('Invalid input')
            continue
        d = div(s[0], s[1])

        if s[1] == '0':
            print('Cannot divide by zero')
        else:
            print('{} / {} = {}'.format(s[0], s[1], d))

if __name__ == '__main__':
    main()


''' SAMPLE OUTPUT
Enter q to quit or a pair of fraction: Enter q to quit or a pair of fraction: 1/2 3/4
1/2 + 3/4 = 5/4
Enter another pair of fraction for subtraction: 1/2 1/2
1/2 - 1/2 = 0
Enter another pair of fraction for multiplication: 1/2 1/3
1/2 * 1/3 = 1/6
Enter another pair of fraction for division: 1/2 0
Cannot divide by zero
Enter q to quit or a pair of fraction:
'''
