def max2(lst):
    max = lst[0]
    for i in lst:
        if (i > max):
            max = i
    return max

def findLong(lst, n):
    for st in lst:
        if len(st) > n:
            print(st)

def chet(lst):
    chet = []
    nech = []
    for c in lst:
        if c % 2:
            nech.append(c)
        else:
            chet.append(c)
    return chet, nech

def fact(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

num = [1, 55554, 867, 2]
str = ["abcdefg", "aaaaaaaaaaaaaaaaaaa", "", "f"]

print(max2(num))
findLong(str, 1)
print(chet(num))
print(fact(4000))
