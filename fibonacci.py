startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))

def fib(n):
    if n ==0 :
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print map(fib, range(startNumber, endNumber))