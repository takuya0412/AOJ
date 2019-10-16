def h1(key, m):
    return key % m


def h2(key, m):
    return 1+(key % (m-1))


def h(key, i, m):
    return (h1(key, m)+i*h2(key, m)) % m


def get_key(str_key):
    alpha_num = {"A": 1, "C": 2, "G": 3, "T": 4}
    res = 0
    for char in str_key:
        res *= 4
        res += alpha_num[char]
    return res


def insert(str_key, m):
    key = get_key(str_key)
    i = 0
    while True:
        j = h(key, i, m)
        if T[j] == str_key:
            return j
        elif T[j] == "":
            T[j] = str_key
            return j
        else:
            i += 1


def search(str_key, m):
    key = get_key(str_key)
    i = 0
    while True:
        j = h(key, i, N)
        if T[j] == str_key:
            return "yes"
        elif T[j] == "" or i >= m:
            return "no"
        else:
            i += 1


N = int(input())
T = [""]*N
for i in range(N):
    cmd, str_key = input().strip().split(' ')
    if cmd[0] == 'i':
        insert(str_key, N)
    else:
        print(search(str_key, N))
