import csv
from itertools import product


def task(path):
    n = -1
    with open(path, newline="") as csvfile:
        filedata = list(csv.reader(csvfile, delimiter=",", quotechar='|'))

    filedata = [[int(s) - 1 for s in row] for row in filedata]
    for a, b in filedata:
        n = max(n, a, b)

    r1 = [] 
    r2 = [] 
    r3 = [] 
    r4 = [] 
    r5 = [] 
    gr = [[] for _ in range(n + 1)]
    p = []
    for a, b in filedata:
        r1.append([a, b])  
        r2.append([b, a]) 
        gr[a].append(b)
        p.append(b)
    root = (n + 1) * n // 2 - sum(p)

    def gs(x, stack):
        for node in stack:
            r3.append([node, x])  # 0 - управление, 1 - подчинение
            r4.append([x, node])
        for node1, node2 in product(gr[x], gr[x]):
            if node1 != node2:
                r5.append([node1, node2])
        stack.append(x)
        for node in gr[x]:
            gs(node, stack)
        stack.pop()

    stack1 = []
    gs(root, stack1)

    def p1(x):
        return [[i + 1 for i in row] for row in x]

    def p1t(x):
        return [tuple(i + 1 for i in row) for row in x]

    r3 = [list(l) for l in set(p1t(r3)) - set(p1t(r1))]
    r4 = [list(l) for l in set(p1t(r4)) - set(p1t(r2))]

    r1 = p1(r1)
    r2 = p1(r2)
    r5 = p1(r5)

    task1_ans = [[[] for _ in range(5)] for _ in range(n + 1)]
    task2_ans = [[] for _ in range(5)]
    r = [r1, r2, r3, r4, r5]
    for i in range(5):
        for a, b in r[i]:
            task1_ans[a - 1][i].append(b)
            task2_ans[i].append(a)
        task2_ans[i] = list(sorted(set(task2_ans[i])))

    print(task1_ans, sep="\n")
    print(task2_ans, sep="\n")


if __name__ == '__main__':
    task("graph.csv")
