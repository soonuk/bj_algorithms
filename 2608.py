#유클리드 호제법을 이용한 최대공약수 구하기
def gcd(a,b):
    
    while b!=0:
        r = a % b
        a = b
        b = r
    return a


a, b = map(int, input().split())

#최대공약수
gNum=gcd(a, b)

print(gNum)
print(int(a*b/gNum))