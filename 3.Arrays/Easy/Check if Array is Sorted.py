
def check(arr,n):

    count=0

    for i in range(n):

        if arr[i]>arr[(i+1)%n]:
            count+=1
        
    return count<=1



#Driver Code
if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(check(arr,n))
