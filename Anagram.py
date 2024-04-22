import numpy as np
def isAnagram(s, t):

    match = False
    slist = []
    tlist = []
    for letters in s:
        slist.append(letters)
    for letters2 in t:
        tlist.append(letters2)

    s1, su = np.unique(slist, return_counts=True)
    t1, tu = np.unique(tlist , return_counts=True)

    if len(s1) != len(t1): return False

    for i in range(0, len(s1)):
        if (s1[i] != t1[i]) or (su[i] != tu[i]): return False

    return True




in1 = input()
in2 = input()
isAnagram(in1, in2)

s1 = input()
s2 = input()

isAnagram(s1, s2)