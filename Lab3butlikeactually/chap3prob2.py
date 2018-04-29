def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
def main():
    x = int(input("Please enter a number "))
    
    print(factorial(x))
    
    
if __name__ == "__main__":
    main()