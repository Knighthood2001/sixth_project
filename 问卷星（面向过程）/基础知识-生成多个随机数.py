import random
def int_random(m, n, o):
    p = []
    while len(p) < o:
        new_int = random.randint(m, n)
        if (new_int not in p):
            p.append(new_int)
        else:
            pass
    return p
q = int_random(3, 8, 3)
q.sort()
print(q)
# 遍历列表内容，并打印
for r in q:
    print(r)
