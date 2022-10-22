N = int(input())

numCnt = [0]*(N+1)

for i in range (2,N+1):
    numCnt[i] = numCnt[i-1] + 1

    if i %2 ==0:
        numCnt[i] = min(numCnt[i],numCnt[i//2]+1)
    if i %3 ==0:
        numCnt[i] = min(numCnt[i], numCnt[i//3]+1)

print(numCnt[N])