import itertools
#https://www.hackerrank.com/challenges/non-divisible-subset/problem
def nonDivisibleSubset(k, S):
    n = len(S)
    while n > 1:
        sets = itertools.combinations(S, n)
        for set_ in sets:
            if all((u+v) % k for (u, v) in itertools.combinations(set_, 2)) != 0:
                return n
        n -= 1
    return 0

nonDivisibleSubset(4,[19,10,12,10,24,25,22])
"""
all = intersection
any = union
"""