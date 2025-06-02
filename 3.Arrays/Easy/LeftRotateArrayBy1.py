


def reverse(arr,start,end):
    while(start<end):
        arr[start]=arr[start]^arr[end]
        arr[end]=arr[start]^arr[end]
        arr[start]=arr[start]^arr[end]
        start+=1
        end-=1


#Driver Code
if __name__ == '__main__':
    arr=[3,4,1,5,3,-5]
    k=1
    n=len(arr)
    reverse(arr,0,n-1)
    reverse(arr,0,n-k-1)
    reverse(arr,n-k,n-1)
    print(f"After rotaing the array by {k} elements to the left: {arr}")




