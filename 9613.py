import sys

def gcd(a,b):
    while b!=0:
        r= a%b
        a = b
        b =r
    return a

n = int(sys.stdin.readline())

for i in range(n):
    numList = list(map(int, sys.stdin.readline().split()))
    output=0
    for j in range(1,numList[0]):
        for k in range(j+1,numList[0]+1):
            output+= gcd(numList[j], numList[k])
            
            
    print(output)