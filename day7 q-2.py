def febonaccia(n):
    if n<=1:
        return n
    return fibonacia (n-1)+fibonacia(n-2)
n=int(input("Enter the number of terms:"))
print("Fibonnacia series:")
for i in range (n):
        print (fibonacia(i), end=" ")
