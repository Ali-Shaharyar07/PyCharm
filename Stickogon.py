import numpy as np

c = [ ]
ans = 0
n = int(input())
a = str(input())
lengths = a.split()

for i in lengths:

    c.append(int(i))

u, uc = np.unique(c, return_counts=True)

for j in range(0, len(uc)):
    for k in range(3, 100):
        if uc[j]%k == 0 and uc[j]/k >= 1:
            ans += int(uc[j]/k)
            break
print(ans)




