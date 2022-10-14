import sys

li=[]
#insert값 0번==n, 1번 ==k
ins = list(map(int, sys.stdin.readline().split()))
ran = range(1,ins[0])
circle=list(ran)
pos =0
ans = []
while True:
    pos+=ins[1]
    if len(circle) <= ins[1]:
        ans.append(ran.pop())
    elif pos>len(circle):
        pos-=len(circle)

        transli1 =circle[0:pos]
        transli2 = circle[pos:]
        ans.append(transli1.pop())
        pos-=1
        circle= transli1 + transli2
    else:
        
    if circle ==[]:
        break
