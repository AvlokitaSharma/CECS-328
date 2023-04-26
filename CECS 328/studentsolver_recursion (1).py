def solve(grid):

    def gen(lis,tot,col):
        if(tot==col-1):
            ans.append(lis[::])
        else:
            lis.append(0)
            gen(lis,tot+1,col)
            lis.pop()

            lis.append(1)
            gen(lis,tot+1,col)
            lis.pop()

            lis.append(-1)
            gen(lis,tot+1,col)
            lis.pop()


    ans=[]
    rows = len(grid)
    columns = len(grid[0])
    gen([],0,columns)
    fill = ans[::]
    
    glob=[]
    for i in range(columns):
        for j in fill:
            now=[0,i]
            check=grid[now[0]][now[1]]
            
            for k in j:
                now=[(now[0]-k)%rows,(now[1]+1)%columns]
                check+=grid[now[0]][now[1]]
            if(now[0]==0 or now[0]==rows-1):
                glob.append([check,1,-i,j])
    for i in range(columns):
        for j in fill:
            now=[rows-1,i]
            check=grid[now[0]][now[1]]
            
            for k in j:
                now=[(now[0]-k)%rows,(now[1]+1)%columns]
                check+=grid[now[0]][now[1]]
            if(now[0]==0 or now[0]==rows-1):
                glob.append([check,0,-i,j])
    glob.sort(reverse=True)
    glob=glob[0]
    ret=[]
    ret.append(glob[1])
    ret.append(-glob[2])
    for i in glob[3]:
        ret.append(i)
    return ret
    

# grid = [[3, 4, 1, 2, 8, 6],
#         [6, 1, 8, 2, 7, 4],
#         [5, 4, 3, 9, 9, 5],
#         [5, 9, 8, 3, 2, 6],
#         [8, 7, 2, 9, 6, 4]]


# grid = [[9, 9, 8, 3, 8, 2, 5, 4, 9], 
#         [5, 5, 9, 1, 3, 2, 3, 2, 4], 
#         [3, 9, 1, 4, 4, 4, 5, 4, 2], 
#         [3, 7, 4, 8, 5, 5, 7, 7, 8], 
#         [9, 5, 1, 1, 3, 9, 8, 9, 8], 
#         [1, 4, 8, 2, 6, 8, 6, 9, 2]]

# grid = [[9, 9, 8, 3, 8, 2, 5, 4, 9], [5, 5, 9, 1, 3, 2, 3, 2, 4], [3, 9, 1, 4, 4, 4, 5, 4, 2], [3, 7, 4, 8, 5, 5, 7, 7, 8], [9, 5, 1, 1, 3, 9, 8, 9, 8], [1, 4, 8, 2, 6, 8, 6, 9, 2]]


# grid = [[479, 798], 
#         [80, 867], 
#         [50, 441], 
#         [218, 486], 
#         [412, 111], 
#         [173, 249], 
#         [348, 276], 
#         [887, 503], 
#         [844, 524], 
#         [383, 477]]
# path = solve(grid)
# print(path)

