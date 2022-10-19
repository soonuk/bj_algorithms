def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

N, S = map(int, input().split())
pos = list(map(int, input().split()))

distanceList=[]
for i in pos:
    dis = i - S
    distanceList.append(abs(dis))

stand = distanceList[0]

start=1
#세수의 최대공약수는 두수의 최대공약수의 결과값을 계속 가져와 반복하는것과 동일
while start<len(pos):
    stand = gcd(stand,distanceList[start])
    start+=1
print(stand)
