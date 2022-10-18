import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

#각 숫자 갯수용 리스트 만들기
numsCount =[0]*1000001
for i in range (n):
    numsCount[nums[i]]+=1

#index저장용 stack과 출력값 생성
stack =[] 
answer =[-1] * n

for i in range(n):
    while stack and numsCount[nums[stack[-1]]] < numsCount[nums[i]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
