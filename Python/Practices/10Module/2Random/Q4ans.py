import random as rd

list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1000):
    j = rd.randint(2, 12)
    list[j]+=1

print(list)



'''SAMPLE OUTPUT
@seantaihx ➜ .../Python/Practices/10Module/2Random (main) $ python Q4ans.py
[0, 0, 106, 105, 84, 94, 82, 94, 85, 80, 94, 87, 89]
@seantaihx ➜ .../Python/Practices/10Module/2Random (main) $ 
'''