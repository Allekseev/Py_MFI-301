def rem(s):   # убирает лишние пробелы
    words = s.split()
    return " ".join(words)


def kalk(s):   # калькулятор
    words = s.split()
    pr = {'^': 0, '*': 1, '/': 1, '+': 2, '-': 2}   # приоритеты операций
    op = {'+': lambda x,y: x+y, '-': lambda x,y: x-y, '*': lambda x,y: x*y, '/': lambda x,y: x/y, '^': lambda x,y: x**y}
    for i in range(len(words)):
        if not words[i] in pr:
            words[i] = float(words[i])

    resInd = 0
    signInd = 0
    for p in range(3):
        for i in range(len(words)):
            if words[i] == '':
                continue
            if words[i] in pr:
                signInd = i
            else:
                if signInd and pr[words[signInd]] == p:
                    words[i] = op[words[signInd]](words[resInd],words[i])
                    words[resInd] = ''
                    words[signInd] = ''
                    signInd = 0
                resInd = i

    return words[resInd]


def count(s):   # считает кол-во слов
    words = s.split()
    return len(words)


def star(s):   # заменяет гласные на *
    glas = ('a', 'e', 'i', 'o', 'u', 'y')
    l = list(s)
    for i in range(len(l)):
        if l[i] in glas:
            l[i] = '*'
    return "".join(l)


def delShort(s, c):   # удаляет слова короче c
    words = s.split()
    for i in range(len(words)):
        if len(words[i]) < c:
            words[i] = ''
    return(rem(" ".join(words)))

#print(delShort(input("введите слова\n"), int(input("минимальная длина слов: "))))
print(kalk(input()))
