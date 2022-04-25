def solve(printers):
    ## init
    totalNeeds = 10**6
    cartridges = 4
    maxAvailableInk = [0] * cartridges

    ## find maxAvailableInk that printer could use for each cartridges
    for ink in range(cartridges):
        maxAvailableInk[ink] = min(printers[0][ink],printers[1][ink],printers[2][ink])

    if sum(maxAvailableInk) < totalNeeds:
        return "IMPOSSIBLE"

    needsInk = [0] * cartridges
    for ink in range(cartridges):
        if maxAvailableInk[ink] > totalNeeds:
            needsInk[ink] = totalNeeds
            break
        else:
            totalNeeds -= maxAvailableInk[ink]
            needsInk[ink] = maxAvailableInk[ink]

    return " ".join([str(i) for i in needsInk])

caseNum = int(input())
for caseno in range(caseNum):

    ## process input
    printers = []
    for _ in range(3):
        s = input().split(" ")
        printers.append([int(p) for p in s ])

    ## solve
    res = solve(printers)

    print(f'Case #{caseno+1}: {res}')