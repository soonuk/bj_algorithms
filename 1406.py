import sys
#초기 입력 문자열 받아서 list만들기
N = list(sys.stdin.readline())
N.pop()

# 입력할 명령어의 갯수
cnt = int(sys.stdin.readline())

#기본커서 위치 정하기
cursor = len(N)

for i in range(cnt):
    #추가 입력 명령어
    type= list(input())
    #임시 저장소
    trlist1=[]
    trlist2=[]

    if type[0]=="P":
        val = type[2]
        #list분할
        trlist1 = N[0:cursor]
        trlist2 = N[cursor:]

        trlist1.append(val)
        cursor+=1
        #새값 추가후 다시 합치기
        N = trlist1+trlist2

    elif type[0]=="B":
        #cursor가 0이면 아무것도 안함

        if cursor !=0:
            #list분할
            trlist1 = N[0:cursor]
            trlist2 = N[cursor:]

            trlist1.pop()
            cursor-=1
            N = trlist1+trlist2
         
        
    
    elif type[0]=="L":
        #커서가 최좌측 아니면 좌측으로 한칸이동
        if cursor !=0:
            cursor-=1
        
    elif type[0]=="D":
        #커서가 최우측 아니면 우측으로 한칸이동
        if cursor !=len(N):
            cursor+=1

for i in N:
    print(i, end="")

#시간초과로 실패asdas
#ch1