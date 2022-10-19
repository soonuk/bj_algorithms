num = int(input())
out=1

while num >0:   
    out *= num
    num-=1
outStr =str(out)

cnt=0
for i in range( len(outStr)):
    if outStr[-i-1]=="0":
        cnt+=1
    else:
        break
print(cnt)