def solve_capcha(capcha_str):
    capcha = [int(cc) for cc in list(capcha_str)]
    total = 0
    for ii in range(len(capcha)):
         if capcha[ii] == capcha[ii - 1]:
             total += capcha[ii]
    return total


def solve_capcha2(capcha_str):
    capcha = [int(cc) for cc in list(capcha_str)]
    total = 0
    capcha_len = len(capcha)
    for ii in range(capcha_len):
         if capcha[ii] == capcha[ii - capcha_len//2]:
             total += capcha[ii]
    return total


def main():
    tests = {
        '1122': 3,
        '1111': 4,
        '1234': 0,
        '91212129': 9
    }
    errors = 0
    for k, v in tests.iteritems():
        ans = solve_capcha(k)
        if ans != v:
            print('solve_capcha({}) != {} (={})'.format(k, v, ans))
            errors += 1
    if errors == 0:
        print('Pt. 1 Tests Passed')

    tests = {
        '1212': 6,
        '1221': 0,
        '123425': 4,
        '123123': 12,
        '12131415': 4
    }
    errors = 0
    for k, v in tests.iteritems():
        ans = solve_capcha2(k)
        if ans != v:
            print('solve_capcha({}) != {} (={})'.format(k, v, ans))
            errors += 1
    if errors == 0:
        print('Pt. 2 Tests Passed')

    with open('./input/day_1.txt') as f:
        data = f.read().strip()
        ans = solve_capcha(data)
        print('Day 1 Pt. 1 Solution: {}'.format(ans))
        ans = solve_capcha2(data)
        print('Day 1 Pt. 2 Solution: {}'.format(ans))

if __name__ == "__main__":
    main()
