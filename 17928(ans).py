import sys

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
stack=0
ans=[]
val=0
#none
for i in range(n):
    if stack==0:
        stack+=1
        val = lis[i]
        if lis[i] == max(lis):
            ans.append('-1')
            stack=0
            val=0
    
    elif lis[i]>val:
        ans += stack*str(lis[i])
        val = lis[i]
        stack=1
    elif lis[i]<=val:
        stack+=1
        
ans+=("-1"*stack)
print(ans)
K = list(map(int,ans))
print(K)