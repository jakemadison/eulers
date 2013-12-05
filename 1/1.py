#stub for proj 1
#=====================
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def gen():
	x = 0
	while True:
		if (x % 3 == 0) or (x % 5 == 0):
			yield x
		x+=1

def nums(n):
	tot = 0
	for each in gen():
		if each < n:
			tot+=each
		else:
			print(tot)
			return tot

nums(1000)
print("\n====\ndone")

