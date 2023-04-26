def solve(grid):

    def recur(i,j,n,m,now):
        j=j%m
        if(j%m==(now-1)%m):
            if(i==0 or i==n-1):
                dp[i][j][0]=grid[i][j]
                return grid[i][j]

            else:
                return -1


        if(dp[i][j][0]>0):
           return dp[i][j][0]
        else:
            a=recur((i+1)%n,j+1,n,m,now)
            b=recur(i,j+1,n,m,now)
            c=recur((i-1)%n,j+1,n,m,now)  
            k=[a,b,c]
            c=max(k)
            if(c>=1):
                dp[i][j][0]=c+grid[i][j]
                if(a==c):
                    dp[i][j][1]=1
                elif(b==c):
                    dp[i][j][1]=0
                else:
                    dp[i][j][1]=-1
                return c+grid[i][j]
            else:
                return 0

    n=len(grid)
    m=len(grid[0])
    
    tot=[]
    for i in range(m):
        dp=[[[0,0] for i in range(m)] for j in range(n)]
        k=recur(0,i,n,m,i)
        k=[k]+dp
        tot.append(k)
    for i in range(m):
        dp=[[[0,0] for i in range(m)] for j in range(n)]
        k=recur(n-1,i,n,m,i)
        k=[k]+dp
        tot.append(k)
    k=0
    ind=-1
    for i in range(len(tot)):
        if(tot[i][0]>k):
            k=tot[i][0]
            ind=i
    printer=[]
    dp=tot[ind][1:]
    if(ind<=m):
        row=0
        col=ind%m
        printer=[1,col]
    else:
        row=n-1
        col=ind%m
        printer=[0,col]

        
    cou=m-1
    while(cou):
        cou-=1
        printer.append(-dp[row%n][col%m][1])
        if(dp[row%n][col%m][1]==-1):
            row-=1
        if(dp[row%n][col%m][1]==1):
            row+=1
        col+=1
    return printer

grid = [[3, 4, 1, 2, 8, 6],
        [6, 1, 8, 2, 7, 4],
        [5, 4, 3, 9, 9, 5],
        [5, 9, 8, 3, 2, 6],
        [8, 7, 2, 9, 6, 4]]


print(*solve(grid))
