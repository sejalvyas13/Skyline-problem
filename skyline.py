def getSkyline(buildings):
    xpos = []
    result=[[-1,0]]
    for b in buildings :
        xpos.append(b[0])  
        xpos.append(b[1])
    xpos.sort()
    for i in xpos :
        print("(0,", i , ")")
    
    for p in xpos :
        i = 0
        h = 0
        while i < len(buildings) and buildings[i][0]<=p :
            if buildings[i][1] > p :
                h = max(h, buildings[i][2])
            i = i+1
        if result[len(result)-1][1] == h :
            continue
        else :
            result.append([p,h])
    result.pop(0)
    print(result)
    

buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
getSkyline(buildings)