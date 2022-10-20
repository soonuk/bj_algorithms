from sys import stdin

num = int(stdin.readline())
lia = [int(input()) for _ in range(num)]
big = max(lia)

array = [True for i in range(big+1)]

for i in range(2, int(big**(0.5))+1):
    if array[i]:
        for k in range(i + i, big+1, i):
            array[k] = False
for k in range(num):
    cnt =0
    for i in range(3,lia[k]//2+1):
        if array[i] and array[lia[k]-i]:
            cnt+=1
    print(cnt)        