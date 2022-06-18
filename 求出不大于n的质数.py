#n为大于等于2的正整数，求出不大于n的所有质数
#解法1
n = eval(input())
for i in range(2,n+1):
    ok = True
    for k in range(2,i):
        if i%k == 0:
            ok = False
            break
    if ok:
        print(i)
#解法2
n = eval(input())
print(2)
for i in range(3,n+1,2):
    ok = True
    for k in range(3,i,2):
        if i%k == 0
            ok = False
            break
        if pow(k,2) > i
            break
    if ok:
        print(i)