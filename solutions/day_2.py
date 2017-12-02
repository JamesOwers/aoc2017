from __future__ import division, print_function
import numpy as np
from itertools import combinations
from fractions import gcd


def checksum(X):
    return np.sum(X.max(axis=1) - X.min(axis=1))


def checksum2(X):
    X.sort(axis=1)
    ans = []
    for row in X:
        combs = combinations(row, 2)
        comb = [ii for ii in combs if (gcd(*ii) in ii)]
        assert len(comb) == 1
        comb = comb[0]
        ans += [max(comb) / min(comb)]
    return np.sum(ans)


def main():
    tests = {
        'inputs': [np.array([[5, 1, 9, 5]]), np.array([[7, 5, 3]]),
                  np.array([[2, 4, 6, 8]])],
        'outputs': [np.array(8), np.array(4), np.array(6)]
    }
    errors = 0
    fun = checksum
    for k, v in zip(tests['inputs'], tests['outputs']):
        ans = fun(k)
        if ans != v:
            print('fun({}) != {} (={})'.format(k, v, ans))
            errors += 1
    if errors == 0:
        print('Pt. 1 Tests Passed')

    tests = {
        'inputs': [np.array([[5, 9, 2, 8]]), np.array([[9, 4, 7, 3]]),
                  np.array([[3, 8, 6, 5]])],
        'outputs': [np.array(4), np.array(3), np.array(2)]
    }
    errors = 0
    fun = checksum2
    for k, v in zip(tests['inputs'], tests['outputs']):
        ans = fun(k)
        if ans != v:
            print('fun({}) != {} (={})'.format(k, v, ans))
            errors += 1
    if errors == 0:
        print('Pt. 2 Tests Passed')

    data = np.genfromtxt('./inputs/day_2.txt', dtype=int)
    ans = checksum(data)
    print('Day 2 Pt. 1 Solution: {}'.format(ans))
    ans = checksum2(data)
    print('Day 2 Pt. 2 Solution: {}'.format(ans))

if __name__ == "__main__":
    main()
