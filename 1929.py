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

M, N = map(int, sys.stdin.readline().split())
c = prime(M)
d = prime(N)
e = [i for i in d if i not in c]
for i in e:
    print(i)
