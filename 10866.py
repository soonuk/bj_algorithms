import sys

N = int(sys.stdin.readline())
li=[]

for i in range(N):
    command = list(sys.stdin.readline().split())
    
    if command[0]=="push_back":
        li.append(command[1])
    
    elif command[0]=="push_front":
        li.reverse()
        li.append(command[1])
        li.reverse()

    elif command[0]=="pop_front":

        if li:
            li.reverse()
            print(li.pop())
            li.reverse()
        else:
            print(-1)
    elif command[0]=="pop_back":

        if li==[]:
            print(-1)
            
            
        else:
            print(li.pop())

    elif command[0]=="size":
        print(len(li))
    
    elif command[0]=="empty":
        if li:
            print(0)
        else:
            print(1)

    elif command[0]=="front":
        if li:
            print(li[0])
        else:
            print(-1)
    
    elif command[0]=="back":
        if li:
            print(li[len(li)-1])
        else:
            print(-1)