print('Tic Tac Toe game With Pc\n')
print('To play you have to write the nuber of column and \n then the number of the line')
bo=[["-" for i in range(3)] for j in range(3)]
i=0
game='false'
while game=='false':
    ans='false'
    while ans=='false':
        ans='false'
        if i%2==0:
            print('Your Turn')
            a=int(input('Column: '))
            b=int(input('Line: '))
            a=a-1
            b=b-1
            X='O'
            Who='You'
        else:
            print('Pc\'s Turn')
            import random
            a=random.randrange(3)
            b=random.randrange(3)
            X='X'
            Who='Pc'
        if bo[a][b]=="-":
            bo[a][b]=X
            ans='true'
            i=i+1
            for j in bo:
                print(*j, sep=" ")
            if ((bo[2][0] == X and bo[2][1] == X and bo[2][2] == X) or (bo[1][0] == X and bo[1][1] == X and bo[1][2] == X) or
            (bo[0][0] == X and bo[0][1] == X and bo[0][2] == X) or (bo[2][0] == X and bo[1][0] == X and bo[0][0] == X) or
            (bo[2][1] == X and bo[1][1] == X and bo[0][1] == X) or (bo[2][2] == X and bo[1][2] == X and bo[0][2] == X) or
            (bo[2][0] == X and bo[1][1] == X and bo[0][2] == X) or (bo[2][2] == X and bo[1][1] == X and bo[0][0] == X)):
                print('And The Winner Is: ',Who)
                game='True'
                
