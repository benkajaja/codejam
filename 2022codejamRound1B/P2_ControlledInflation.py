def solve(customerProducts):
    ## init
    preLeftPascal, preRightPascal = 0, 0
    leftMin, rightMin = 0, 0

    for i in range(len(customerProducts)):
        curLeftPascal = customerProducts[i][0]
        curRightPascal = customerProducts[i][-1]
        curInterval = curRightPascal-curLeftPascal

        ## min accumulated presses that start from left or right and end at left
        tmp1 = min(leftMin + abs(preLeftPascal-curRightPascal), rightMin + abs(preRightPascal-curRightPascal)) + curInterval

        ## min accumulated presses that start from left or right and end at right
        tmp2 = min(leftMin + abs(preLeftPascal-curLeftPascal), rightMin + abs(preRightPascal-curLeftPascal)) + curInterval

        leftMin, rightMin = tmp1, tmp2
        preLeftPascal = curLeftPascal
        preRightPascal = curRightPascal
    
    return min(leftMin, rightMin)

caseNum = int(input())
for caseno in range(caseNum):

    ## process input
    customerProducts = []
    s = input().split(" ")
    for customer in range(int(s[0])):
        product = input().split(" ")
        intParseProduct = [int(p) for p in product]
        
        ## only need to key min and max value
        customerProducts.append([min(intParseProduct), max(intParseProduct)])

    ## solve
    res = solve(customerProducts)

    print(f'Case #{caseno+1}: {res}')