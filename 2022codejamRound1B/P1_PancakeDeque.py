def solve(p):
    ## init
    front, tail = 0, len(p)-1
    curMax = 0
    paidCustomers = 0
    
    ## pop panckage
    while(front <= tail):

        ## find the smallest one
        if p[front] < p[tail]:
            if p[front] >= curMax:
                paidCustomers += 1
                curMax = p[front]
            front += 1
        else:
            if p[tail] >= curMax:
                paidCustomers += 1
                curMax = p[tail]
            tail -= 1
    
    return paidCustomers

caseNum = int(input())
for caseno in range(caseNum):

    ## process input
    input()
    s = input().split(" ")
    pancakes = [int(p) for p in s]

    ## solve
    res = solve(pancakes)

    print(f'Case #{caseno+1}: {res}')