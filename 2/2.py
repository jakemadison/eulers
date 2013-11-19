#stub for proj2
# Each new term in the Fibonacci sequence is generated by 
# adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the 
# Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def gen():
	yield 1
	yield 2
	start=1
	next=2
	while  True:
		result = start+next
		start = next
		next = result
		yield result

def fibs(max_val):
	tot = 0
	for itm in gen():
		if itm < max_val:
			if itm%2 == 0:
				tot += itm
		else:
			print(tot)
			return(tot)



fibs(4000000)
print("\n====\ndone.")
