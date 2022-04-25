def solve(n, touchScreen):
    # a b
    # c d
    # a == d and c == b

    a, b, c, d = 0, 0, 0, 0
    for r in range(n*2):
        s = touchScreen[r]
        if r < n:
            a += s[:n].count('I')
            b += s[n:].count('I')
        else:
            c += s[:n].count('I')
            d += s[n:].count('I')

    return abs(a-d) + abs(c-b)


caseNum = int(input())
for caseno in range(caseNum):

    ## process input
    n = int(input())
    touchScreen = []
    for _ in range(2*n):
        touchScreen.append(input())

    ## solve
    res = solve(n, touchScreen)

    print(f'Case #{caseno+1}: {res}')