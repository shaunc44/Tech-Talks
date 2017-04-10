## How does recursion affect memory?  


```python
def factorial(n):

	if n == 1:
		return 1
	else:
		#returns n * n-1 * (n-2) * (n-3) * ... (1)
		#after 5 is passed into the function, factorial(5) runs
		#then factorial(4) runs inside factorial(5)
		#and then factorial(3) runs inside factorial(4) which runs inside factorial(5)
		#until we reach factorial(1)

		return n * factorial(n-1)

print ( factorial(5) )
```


1. Recursion, especially tail recursion, is expensive because it requires allocation of a new stack  

2. RecursionError: maximum recursion depth exceeded in comparison (Stack Overflow)  


##### *Sources:*  
<http://stackoverflow.com/questions/72209/recursion-or-iteration>  
<http://stackoverflow.com/questions/2651112/is-recursion-ever-faster-than-looping/2651200#2651200>  
<http://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it>  
