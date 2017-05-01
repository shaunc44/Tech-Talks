import timeit


start = timeit.default_timer()


def factorial(n):

	if n == 1:
		return 1
	else:
		#returns n * n-1 * (n-2) * (n-3) * ... * (1)
		#after 5 is passed into the function, factorial(5) runs
		#then factorial(4) runs inside factorial(5)
		#and then factorial(3) runs inside factorial(4) which runs inside factorial(5)
		#until we reach factorial(1)
		return n * factorial(n-1)


n = 5000
print ("\nFactorial(",n,") = ", factorial(n) )


stop = timeit.default_timer()
print ("\nSeconds to run: ", (stop - start), '\n')