'''
Start with this set:
nums = {10, 20, 30}
	•	Add multiple elements using update().
	•	Then remove an element using discard() (choose an element that doesn’t exist to test it).
	•	Try using remove() on a missing element and see what happens.
'''

nums = {10, 20, 30}
a = [10, 30, 40, 50]
nums.update(a)
print(nums)
nums.discard(50)
print(nums)
nums.discard(50)
print(nums)
nums.remove(40)
print(nums)
nums.remove(40)
print(nums)


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/4Sets (main) $ python Q3ans.py
{40, 10, 50, 20, 30}
{40, 10, 20, 30}
{40, 10, 20, 30}
{10, 20, 30}
Traceback (most recent call last):
  File "/workspaces/Practice/Python/Practices/4Sets/Q3ans.py", line 19, in <module>
    nums.remove(40)
KeyError: 40
@seantaihx ➜ .../Practice/Python/Practices/4Sets (main) $ 
'''