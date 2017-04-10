import timeit


start = timeit.default_timer()


def factorial(n):

	if n == 1:
		return 1
	else:
		#returns n * n-1 * (n-2) * (n-3) * ... (1)
		#after 5 is passed into the function, factorial(n) runs inside factorial(n) which runs inside factorial(n) ...
		return n * factorial(n-1)


n = 5000
print ("Factorial(",n,") = ", factorial(n) )


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )