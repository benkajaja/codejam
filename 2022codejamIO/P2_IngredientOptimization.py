import heapq

def countOrders(delivery, order, U):
    h = []
    completeOrders = 0

    for i, o in enumerate(order):
        ## push arrived delivery
        while(delivery and delivery[0][0] <= o):
            d = delivery.pop(0)
            ## sort by endtime
            heapq.heappush(h, (d[0]+d[2], d[1]))
        
        needs = U
        while(h and needs):
            item = heapq.heappop(h)

            ## outdated delivery
            if item[0] <= o:
                continue

            ## valid delivery
            if item[1] <= needs:
                needs -= item[1]
            else:
                ## push remain leaves to heap
                heapq.heappush(h, (item[0], item[1] - needs))
                needs = 0
        if needs == 0:
            completeOrders += 1
        else:
            return completeOrders
    return completeOrders

caseNum = int(input())
for caseNo in range(caseNum):
    ## process input
    tmp = input().split(" ")
    D, N, U = int(tmp[0]), int(tmp[1]), int(tmp[2])
    delivery = []
    order = []
    for _ in range(D):
        tmp = input().split(" ")
        delivery.append([int(d) for d in tmp])

    tmp = input().split(" ")
    order = [int(o) for o in tmp]

    ## solve
    res = countOrders(delivery, order, U)
    print(f"Case #{caseNo+1}: {res}")