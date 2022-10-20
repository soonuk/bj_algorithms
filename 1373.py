import sys
stringNum = sys.stdin.readline().rstrip()
num2 = '0b'+stringNum
num8 = int(num2,8)
print(num8)

print(oct(int(input(),2))[2:])
'''
stringNum =list(input())
ans10=0
for i in range(len(stringNum)):
    if stringNum[-1]=="1":
        ans10 += 2**i
    stringNum.pop()

val8=format(ans10, 'o')
print(val8)
'''