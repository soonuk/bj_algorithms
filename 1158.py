n, k = map(int, input().split())
lst = [i for i in range(1, n + 1)]

answer = []
num = -1

for i in range(n):
    num += k

    if num >= len(lst):
        num %= len(lst)
        
    answer.append(str(lst.pop(num)))
    num-=1

print("<", ", ".join(answer), ">", sep='')
#ch1