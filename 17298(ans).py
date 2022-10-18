
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

stack = []; answer =[-1] * n

# solution
for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(*answer)

