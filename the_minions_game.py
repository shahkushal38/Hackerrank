def minion_game(string):
    # your code goes here
    string=string.strip()
    p1,p2=0,0
    p1=int(p1)
    p2=int(p2)
    n=int(len(string))
   
    for x in range(0,int(len(string)),1):
        
        if string[x]in ('A','E','I','O','U'): 
            p2=p2+n-x
        else:
            p1=p1+n-x
    
    if(p1>p2):
        print('Stuart', p1)
    elif(p1==p2):
        print('Draw')
    else:
        print('Kevin', p2)
##################################################

def minion_game(string):
    # your code goes here
    string=string.strip()
    p1,p2=0,0
    p1=int(p1)
    p2=int(p2)
    n=int(len(string))
    lf=[]
    lf1=[]
    for x in range(0,int(len(string)),1):
        lf=[]
        lf.append(string[x])
        lf1.append(string[x])
        for y in range(x+1,int(len(string)),1):
            lf.append(string[y])
            str1=''.join(map(str,lf))
            lf1.append(str1)

    for x in range(0,int(len(lf1)),1):
        str2=str(lf1[x])
        if(str2[0]=='A' or str2[0]=='E' or str2[0]=='I' or str2[0]=='O' or str2[0]=='U'):
            p2=p2+1
        else:
            p1=p1+1
    
    if(p1>p2):
        print('Stuart', p1)
    elif(p1==p2):
        print('Draw')
    else:
        print('Kevin', p2)

import math
if __name__ == '__main__':
    s = input()
    minion_game(s)

#######################################################





import math
if __name__ == '__main__':
