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

a = [[1, 2, 3, 4], [5, 6, 7, 8], [7, 8, 9, 6]]
b = [[5, 6, 7, 8], [7, 8, 9, 6], [1, 2, 3, 4]]

for row in a:
    for elem in row:
        print(elem, end=" ")
    print()

for row in b:
    for elem in row:
        print(elem, end=" ")
    print()

def MatrixSum(m1, m2):
    a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            a[i][j] = m1[i][j] + m2[i][j]
    return a

ans = MatrixSum(a, b)
for row in ans:
    for elem in row:
        print(elem, end=" ")
    print()

def MatrixMulti(m1, m2):
    a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(m1)):
        for j in range(len(m2[i])):
            sum = 0
            for k in range(len(m1[i])):
                for h in range(len(m2)):
                    sum += m1[i][k] * m2[h][j]
            a[i][j] = sum
    return a

ans1 = MatrixMulti(a, b)
for row in ans1:
    for elem in row:
        print(elem, end=" ")
    print()

def IsContainsConsonants(s):
    isContain = False
    for letter in s:
        if letter.lower() in 'qwrtpsdfghjklzxcvbnm':
            isContain = True
    return isContain

def IsContainsHyphen(s):
    isContain = False
    for letter in s:
        if letter.lower() in '-':
            isContain = True
    return isContain

isContain = IsContainsConsonants(input("Enter string: "))

if (isContain):
    print("Contains")
else:
    print("Not contains")

def WordsWithoutHyphenAndWithConsontants(s):
    text = SplitIntoWords(s)
    res = list()
    for word in text:
        if (IsContainsConsonants(word) and (not IsContainsHyphen(word))):
            res.append(word)
    return res

def SplitIntoWords(s) -> list():
    l = []
    ss = ""
    for x in s:
        if x == " " or x == ',' or x == '. ' or x == '? ' or x == '! ':
            l.append(ss)
            ss = ""
        else:
            ss += x
    l.append(ss)
    return l

text = WordsWithoutHyphenAndWithConsontants(input("Enter words"))

for word in text:
    print(word, end=' ')
    print()

wordsCount = dict()

for word in text:
    lowerWord = word.lower()
    if lowerWord in wordsCount:
        wordsCount[lowerWord] = wordsCount[lowerWord] + 1
    else:
        wordsCount[lowerWord] = 1

for w in wordsCount.items():
    print("{0}:".format(w))