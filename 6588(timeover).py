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
    
primeList = prime(1000000)
while True:
    num = int(sys.stdin.readline())
    ans=[]
    gold=True

    if num==0:
        break
    
    #값 찾기

    for i in range(len(primeList)):
        if primeList[i] > num/2:
            gold=False
            break
        if num - primeList[i] in primeList:
            ans.append(primeList[i])
            ans.append(num-primeList[i])
            break
        
    #값 출력   
    if gold:
        print("%d = %d + %d" %(num, ans[0], ans[1]))
    else:
        print("Goldbach's conjecture is wrong.")

