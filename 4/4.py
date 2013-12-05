#stubb for project:  4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

#decrement down from max, find a palindrome, then good!
#how many elements are left? if 3 or more, compare 1st and last elem
#send the string without first and last elems to same function




maxnum = 998001

def isPalindrome(n):
	n = str(n)
	print(len(n))
	print(n[0], end=' ')
	print(n[-1])

	if len(n) == 1:
		return True

	if len(n) == 2:
		if n[0] == n[-1]:
			return True

	if len(n)> 2:
		subs = n[1:-1]
		print(subs)

		#edges are equal, send sub to same function
		if n[0] == n[-1]:
			print("equal!")
			isPalindrome(subs)

#need to have a case for when there are two

isPalindrome(9999999)


