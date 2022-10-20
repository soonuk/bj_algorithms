def pec(n):
    a=1
    while n>0:
        a *=N
        n-=1
    return a

N = int(input())
ch4 = 4
cnt=1
#4의 배수로 몇자리수인지?
while (4**(cnt)-1)/3<N:
    cnt+=1