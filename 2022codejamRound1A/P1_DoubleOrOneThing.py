def solve(s):
    ## init
    res = ""
    cur = ""

    ## iterate each character
    while(s):
        cur = s[0]*2 + s[1:]
        if cur < s:
            res += s[0]*2
        else:
            res += s[0]
        s = s[1:]

    return res

caseNum = int(input())
for caseno in range(caseNum):

    ## process input
    s = input()

    ## solve
    res = solve(s)

    print(f'Case #{caseno+1}: {res}')
