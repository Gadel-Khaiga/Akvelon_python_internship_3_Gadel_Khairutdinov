#Fibonacci

f1 = 0
f2 = 1



n = int(input(f"Please enter a number: "))
a = int(input(f"Enter the id number that you want to find no more {n}: "))

count = [f1, f2]
for i in range(1, n):
    f1, f2 = f1, f2 + f2
    count.append(f2)
print(*count)

if len(count) > a:
    print(count[0], count[a])
else:
    print(f"Number {a} more than {n}")