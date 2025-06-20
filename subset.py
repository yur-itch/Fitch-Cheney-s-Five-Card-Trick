from itertools import combinations

def subsets(n, k):
    yield from combinations(range(n), k)

def sub4of5(sub5):
    for i in range(len(sub5)):
        sub4 = tuple(sub5[:i] + sub5[i + 1:])
        yield (sub4, sub5[i])

def sup5of4(sub4):
    for i in range(52):
        if i in sub4:
            continue
        sub5 = tuple(sorted(list(sub4) + [i]))
        yield sub5, i