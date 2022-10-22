t  = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
ans =[]
for i in range(4, 11):
    dp[i] =dp[i-1]+dp[i-2]+dp[i-3]

for i in range(t):
    numInput = int(input())
    ans.append(dp[numInput])
    
for i in ans:
    print(i)
