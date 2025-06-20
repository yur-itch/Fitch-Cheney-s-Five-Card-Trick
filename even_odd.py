from importlib import import_module
from itertools import combinations
from subset import sup5of4, sub4of5

def even_subsets():
    evens = [*range(0, 52, 2)]
    yield from combinations(evens, 5)

def odd_subsets():
    odds = [*range(1, 52, 2)]
    yield from combinations(odds, 5)

def decide_one(sub5, is_even, decided4, decided5):
    if sub5 in decided5:
        return True
    sub4of5_ = [*sub4of5(sub5)]
    for sub4, elem in sub4of5_[::-1]:
        if sub4 in decided4:
            continue
        decided4[sub4] = int(not is_even)
        for sup5, i in sup5of4(sub4):
            if sup5 not in decided5:
                decided5[sup5] = i
        return True
    return False

def decide(odd, even, decided4, decided5):
    for i in odd:
        decide_one(i, False, decided4, decided5)
    for i in even:
        decide_one(i, True, decided4, decided5)

if __name__ == "__main__":
    FROM = None
    TO = "even_odd_result"

    odd = odd_subsets()
    even = even_subsets()

    if FROM is None:
        decided4 = {}
        decided5 = {}
    else:
        module = import_module(FROM)
        decided4 = module.decided4
        decided5 = module.decided5

    decide(odd, even, decided4, decided5)

    with open(TO + '.py', 'w') as file:
        file.write(f'decided4 = {decided4}\ndecided5 = {decided5}')