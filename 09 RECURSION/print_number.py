# Print Sum of N number using recursion.
"""def sumOfN(n):
    if n == 0 :
        return 0
    return sumOfN(n-1) + n

sum = sumOfN(5)
print(f"Print Sum Of N Number is: {sum}")"""

# Print Sum of N number using loop.
n = 5
sum = 0
for i in range(1,n+1):
    sum += i

print(sum)

