def pecZero(n):
    
    #10을 만들 5와2
    dec=5
    dc=2

    #5와 2의 제곱수가 갯수
    cnt5=0
    cnt2=0
    
    #출력값
    val5=0
    val2=0

    #5갯수 찾기
    while n//dec>=1:
        cnt5+=1
        dec *=5
    for i in range(1,cnt5+1):
        val5 += n // (5**(i))

    #2갯수 찾기
    while n//dc>=1:
        cnt2+=1
        dc *=2

    for i in range(1,cnt2+1):
        val2 += n // (2**(i))

    return [val5,val2]

n, m =map(int, input().split())

num1 =pecZero(n)
num2 =pecZero(n-m)
num3 =pecZero(m)

val5=num1[0]-num2[0]-num3[0]
val2=num1[1]-num2[1]-num3[1]

print(min(val5,val2))

