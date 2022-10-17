import sys
#none
sentence = sys.stdin.readline().rstrip()

box =""
reversed_str=""
newSentence=""
chk=0

for i in range(len(sentence)):
    if sentence[i]==" " and chk == 0:    
        reversed_str = box[::-1]
        reversed_str+=sentence[i]

        newSentence+=reversed_str
        box=""

    elif sentence[i] =="<":   
        if box:
            reversed_str = box[::-1]
            newSentence+=reversed_str
            box=""

        chk = 1
        box+=sentence[i]
        
    
    elif sentence[i] ==">":
        box+=sentence[i]
        chk =0
        newSentence+=box
        box=""

    elif i==len(sentence)-1 and box:
        box+=sentence[i]
        reversed_str = box[::-1]
        newSentence+=reversed_str


    else:
        box+=sentence[i]

print(newSentence)

