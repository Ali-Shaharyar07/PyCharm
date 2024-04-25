t = int(input())
while t != 0:
    c = [ ]
    uL = set()
    count = 0
    ans = 0
    n = int(input())
    a = str(input())
    lengths = a.split()
    
    for i in lengths:
    
        c.append(int(i))
        uL.add(int(i))
    
    for j in uL:
        for k in range(3, 100):
            count = c.count(j)
            if (count%k == 0) and (count/k >= 1):
                ans += int(count/k)
                break
    
    print(ans)
    t -= 1