from collections import defaultdict
t = int(input())
for i in range(t):
    length = int(input())
    n = input()
    n2 = [eval(n[i]) for i in range(len(n))]

    pref = [0] * (len(n2) + 1)
    for i in range(len(n2)):
        pref[i + 1 ] = pref[i] + n2[i]
    pref = pref[1:]
    hashi = defaultdict(int)
    hashi[1] = 1
    
    count = 0
    for i in range(len(pref)):
        diff = pref[i] - i
        if diff in hashi:
            count += hashi[diff]
        hashi[diff] += 1
    print(count)