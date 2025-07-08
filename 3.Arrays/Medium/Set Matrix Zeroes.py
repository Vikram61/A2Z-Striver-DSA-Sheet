

#Driver Code

if __name__ == '__main__':

    arr=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    m=len(arr[0])
    n=len(arr)
    rows=[False]*n
    cols=[False]*m
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                rows[i]=True
                cols[j]=True
    for i in range(n):
        for j in range(m):
            if rows[i] or cols[j]:
                arr[i][j]=0
    print(arr)

