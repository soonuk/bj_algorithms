#유클리드 호제법을 이용한 최대공약수 구하기
def gcd(a,b):
    
    while b!=0:
        r = a % b
        a = b
        b = r
    return a

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    gNum = gcd(a,b)
    val = int(a*b/gNum)
    print(val)