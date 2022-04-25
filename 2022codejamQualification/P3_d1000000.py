import heapq

def solve(dice):
    heapq.heapify(dice)

    curNum = 1
    while(dice):
        item = heapq.heappop(dice)
        if item >= curNum:
            curNum += 1

    return curNum-1

caseNum = int(input())
for caseno in range(caseNum):

    ## process input
    input()
    s = input().split(" ")
    dice = [int(d) for d in s]

    ## solve
    res = solve(dice)

    print(f'Case #{caseno+1}: {res}')