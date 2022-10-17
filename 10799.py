import sys

bar = sys.stdin.readline().rstrip()
currentBar = 0 #기존 살아있는 바

totalBar=0 #출력값

cnt = 0 #한획당 바 카운트
trVal=0
for i in range(len(bar)):

    if bar[i]==")":
        trVal = i #현재위치 저장
        
        while i >=0:
            
            if bar[i] =="(":
                cnt+=1
            else:
                cnt-=1
            i-=1
        i =trVal    #현재위치 복귀
        
        if cnt < currentBar:
            totalBar += (currentBar-cnt)
            currentBar = cnt
        
        else:
            currentBar = cnt
            totalBar+=currentBar
        
        cnt=0
        
    
    i+=1

print(totalBar)  
#ch1  