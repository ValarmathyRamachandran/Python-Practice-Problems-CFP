# Python Program to find the factors of a number

def primeFactors(n):

	c = 2
	while n > 1:

		if n % c == 0:
			print(c, end=" ")
			n = n / c
		else:
			c = c + 1


n = 20
primeFactors(n)


