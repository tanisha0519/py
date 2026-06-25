start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
print("Armstrong numbers between start and end are:")
for num in range(start, end + 1):
    original = num
    n = len(str(num))
    sum_digits = 0
    while num > 0:
        digit = num % 10
        sum_digits += digit ** n
        num //= 10
    if sum_digits == original:
        print(original, end=" ")
