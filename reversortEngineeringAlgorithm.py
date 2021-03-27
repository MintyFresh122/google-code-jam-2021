def encode(n, c):
    L = list(range(1,n+1))
    #target amount of cost to add to the list, cost = complexity
    costToGo = c - (n-1)
    for i in range(2,n+1):
        #j goes from n-2 to 0
        j = n - i
        #reverse as much as possible if cost to go is higher than we can do in this step
        if costToGo > i-1:
            if j == 0:
                L = L[:j] + L[::-1]
            else:
                L = L[:j] + L[:j-1:-1]
            costToGo -= i-1
        else:
            if j == 0:
                L = L[:j] + L[j+costToGo::-1] + L[j+costToGo+1:]
            else:
                L = L[:j] + L[j+costToGo:j-1:-1] + L[j+costToGo+1:]
            break
    for x in range(0, len(L)):
        L[x] = str(L[x])

    return " ".join(L)




def overall (length, cost):

    if cost < length -1:
        return "IMPOSSIBLE"

    else:
        maxcost = 0
        for i in range (0,length-1):
            maxcost += length- i

        if maxcost < cost:
            return "IMPOSSIBLE"

        else:
            candidatelist = encode(length, cost)
            return candidatelist



numbertest = int(input ())
for case in range (0, numbertest):
    testcase = input().split(" ")
    answer = overall(int(testcase[0]),int(testcase[1]))
    print("Case #"+str(case+1)+": "+answer)
