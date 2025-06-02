
def reverse(arr,start,end):
    while(start<end):
        arr[start]=arr[start]^arr[end]
        arr[end]=arr[start]^arr[end]
        arr[start]=arr[start]^arr[end]
        start+=1
        end-=1



#Driver Code
arr=[1,2,3,4,5,6,7]
k=3
n=len(arr)
reverse(arr,0,n-1)
reverse(arr,0,k-1)
reverse(arr,k,n-1)
print(f"After rotating by {k} elements: {arr}")