import sys
#insert값 0번==n, 1번 ==k
n, k = map(int, sys.stdin.readline().split())
circle=[i for i in range(1,n+1)]
pos =0
ans = []
while circle:

    if pos == k-1:
        ans.append(str(circle.pop(0)))
        pos=0
    else:
        circle.append(circle.pop(0))
        pos+=1 
    
print("<", ", ".join(ans), ">", sep='')
#ch1

