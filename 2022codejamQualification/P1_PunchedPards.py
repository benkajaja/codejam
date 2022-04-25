def solve(row, col):
    punchedCard = ""
    
    firstLine = "..+" + "-+" * (col-1)
    secondLine = "..|" + ".|" * (col-1)
    thirdLine = "+" + "-+" * col
    punchedCard = f'{firstLine}\n{secondLine}\n{thirdLine}\n'
    
    for r in range(row-1):
        punchedCard += "|" + ".|" * col + '\n'
        punchedCard += "+" + "-+" * col + '\n'

    return punchedCard


caseNum = int(input())
for caseno in range(caseNum):

    ## process input
    s = input().split(" ")

    ## solve
    res = solve(int(s[0]), int(s[1]))

    print(f'Case #{caseno+1}:\n{res}', end="")