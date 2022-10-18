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
            ans.append(-1)
            stack=0
            val=0

    elif lis[i] == max(lis):
        for j in range (stack):
            ans.append(lis[i])
        ans.append(-1)
        stack=0
        val=0

    elif lis[i]>val:
        #문자열 삽입말고 숫자 삽입 ans += stack*str(lis[i])
        for j in range (stack):
            ans.append(lis[i])
        val = lis[i]
        stack=1
    elif lis[i]<=val:
        stack+=1
        
#문자열 삽입말고 숫자 삽입ans+=(-1*stack)
for i in range (stack):
    ans.append(-1)
#인트 숫자 출력 ? str로 바꾸는게 나을려나?    
for i in ans:
    print(i, end=" ")

