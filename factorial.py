def factorial(n):
	mul = 1
	for i in range(1,n+1):
		mul *= i
	return mul

if __name__ == "__main__":
	#Taking input from user
	n = int(input("Enter a number to find its factorial: "))
	#printing the factorial of the number
	print(f"factorial of {n} = {factorial(n)}")