
def fibonacci(n):
    a = 0
    b = 1
    print(a, end=' ')
    print(b, end=' ')
    for i in range(2,n):
        add = a + b
        a = b
        b = add
        print(b, end=' ')

if __name__ == "__main__":
	#Taking input from user
	n = int(input("Enter a number to create fibonacci series: "))
	fibonacci(n)