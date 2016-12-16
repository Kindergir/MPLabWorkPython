a = list()
sa = input("Enter numbers: ").split(" ")

for s in sa:
    a.append(int(s))

min = a[0]
max = a[0]

for x in a:
    if x > max:
        max = x
    if x < min:
        min = x

print("Max: {0}, min: {1}".format(max, min))

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(15))