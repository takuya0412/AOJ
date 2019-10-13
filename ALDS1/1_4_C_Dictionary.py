N = int(input())
dic = []
res = []


def h1(key,m):
    return key%m

def h2(key, m):
    return 1+(key%(m-1))

def h(key,i,m):
    return (h1(key,m)+i*h2(key,m))

def insert(T, key):
    i = 0
    while True:
        j = h(key, i)
        if T[i] ==  "":
            T[j] = key
            return j
        else:
            i += 1

def search(T, key):
    i = 0
    while True:
        j = h1(key, m)
        if T[j] == key:
            return j
