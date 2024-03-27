def merge2(left,right):
    global ans
    i = 0
    j = 0
    ansi = []
    temp = 0
    while i < len(left) and j < len(right):

        if left[i] > right[j]:
            ansi.append(right[j])
            temp +=1
            j += 1
        else:
            ansi.append(left[i])
            i += 1
            ans += temp
    # if i <len(left):
    #     ansi.extend(left[i:])
    #     #ans += temp
    for a in range(j,len(right)):
        ansi.append(right[a])
        #ans += temp
    for j in range(i,len(left)):
        ansi.append(left[j])
        ans += temp
    return ansi

def merge(l,r,nums): 
    if l == r:
        return [nums[l]]
    m = l + ((r-l)//2)
    nums_l = merge(l,m,nums)
    nums_r = merge(m + 1,r,nums)

    return merge2(nums_l,nums_r)

t = int(input())
for _ in range(t):
    ans = 0
    q = int(input())
    res = []
    for _ in range(q):
        app = list(map(int,input().split()))
        res.append(app)
    res.sort()
        
    mt = [el[1] for el in res]
    #print(mt)

    merge(0,len(mt)-1,mt)
    print(ans)