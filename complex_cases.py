from importlib import import_module
from subset import sup5of4, sub4of5, subsets


def decide_one(sub5, decided4, decided5):
    if sub5 in decided5:
        return True
    sub4of5_ = [*sub4of5(sub5)]
    for sub4, elem in sub4of5_:
        if sub4 in decided4:
            continue
        decided4[sub4] = elem % 2
        for sup5, i in sup5of4(sub4):
            if sup5 not in decided5:
                decided5[sup5] = i
        return True
    return False


def decide(subs5, decided4, decided5):
    index = 0
    for sub5 in subs5:
        index += 1
        result = decide_one(sub5, decided4, decided5)
        if not result:
            raise RuntimeError(f"Impossible for {sub5}")
        if index % 100000 == 0:
            print(index + 1)


if __name__ == "__main__":
    FROM = None
    TO = 'complex_cases_result'

    if FROM is None:
        decided4 = {}
        decided5 = {}
    else:
        module = import_module(FROM)
        decided4 = module.decided4
        decided5 = module.decided5

    decide(subsets(52, 5), decided4, decided5)

    with open(TO + '.py', 'w') as file:
        file.write(f'decided4 = {decided4}\ndecided5 = {decided5}')