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