#stubb for project:  3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# could interate through all prime numbers, then test if they are factors
# or could interate through all factors of a number and set if they
# are prime


def primeFactor(n):
	count = 1
	while True:
		if n % count == 0:
			test = n / count
			if isPrime(test):
				print(test)
				break
		count += 1






def isFactor(n,i):
	if i == 0 or n==0: return None 
	if n % i == 0:
		return True
	else:
		return False

	
def isPrime(n):
	limit = int(n ** 0.5)+1
	for num in range(2,limit):
		if n % num == 0: return False
	
	return True

#take in number, find largest factor
#of that number
#probably better to split the number and start at halfway up.


primeFactor(600851475143)



#why does this not (efficiency-wise) work?
# num = 600851475143
# cnt = num

# final = 0
# loop = True

# while loop:
# 	if cnt == 0: break #should never happen
	
# 	if isFactor(num,cnt): 	
# 		if isPrime(cnt): 
# 			loop = False; break

# 	cnt-=1

# print(cnt)
print("done!")

# for x in range(1,100):
	# if (isPrime(x)): print(x)

