def factorial(n):
	mul = 1
	for i in range(1,n+1):
		mul *= i
	return mul

if __name__ == "__main__":
	n = int(input("Enter a number to find its factorial: "))
	print(f"factorial of {n} = {factorial(n)}")