x=int(input('How many lines/columns do you want the game to have ? '))
bombs=int(input('How many bombs do you want? '))
#Creating The Base
tb=[["-" for i in range(x)] for j in range(x)]
set=list(range(1,x+1))
print (set)
#Placing the bombs
for i in range (bombs):
        import random
        tb[random.randrange(x)][random.randrange(x)]='*'
        m=0
while m<bombs:
        m=0
        for i in range (x):
                for j in range (x):
                        if tb[i][j]=="*":
                                m=m+1#Counting if bombs are as many as they should
                                #Placing the ones
                                if i<x-1:
                                        tb[i+1][j]=1
                                if i>0:
                                        tb[i-1][j]=1
                                if j<x-1:
                                        tb[i][j+1]=1
                                if j>0:
                                        tb[i][j-1]=1 
        if m!=bombs:
                for i in range (bombs-m):
                        import random
                        tb[random.randrange(x)][random.randrange(x)]='*'
for i in tb:
    print(*i, sep=" ")
	