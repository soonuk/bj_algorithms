import sys
#에라토스테네스의 체 방법 사용
def prime(a):
    alist = [True]*(a)
    b = int(a**(0.5))

    for i in range (2,b+1):
            if alist[i] == True:           # i가 소수인 경우 
                for j in range(i+i, a, i): # i이후 i의 배수들을 False 판정
                    alist[j] = False

    return [i for i in range(2,a) if alist[i]==True]
    
primeList = prime(10000001)

N = int(sys.stdin.readline())
for k in range (N):
    num = int(sys.stdin.readline())
    ans=0
    gold=True

    if num==0:
        break
    
    #값 찾기

    for i in primeList:
        if i > len(primeList)//2:
            
            break
        if num - i in primeList:
            ans+=1
    print(ans)   
    