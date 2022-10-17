import sys

ins = sys.stdin.readline().rstrip()

laser =0
bar = 0 #현재바
total =0 #토탈 갯수
for i in range(len(ins)):
    if ins[i]=="(":
        bar +=1
    else:
        if ins[i-1]=="(":   #레이저의 경우
            bar -=1
            total += bar
        else:               #")"는 쇠막대기인 경우
            bar -=1
            total +=1 

    i+=1
print(total)
#221017