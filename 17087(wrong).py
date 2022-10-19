N, S = map(int, input().split())
pos = list(map(int, input().split()))

#동생위치 만들기
truePos = [False]*(max(pos)+1)
for i in pos:
    truePos[i]=True

#동생위치 찾기
d=0
while True:
    
    if truePos[S-d] or truePos[S+d] ==True :
        if S-d <0:
            d = S + max(pos) - d
        break
    d+=1
print(d)