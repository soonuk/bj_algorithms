import sys

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))



for i in range(n):
    j=i
    if lis[i]>max(lis[i:]):
        print(-1, end=" ")

    else:
        while lis[i]>=lis[j]:
            j +=1

            if j==n:
                j-=1
                break

    if lis[j] > lis[i]:
        print((lis[j]), end =" " )
    else:
        print(-1, end=" ")

    i+=1
             


