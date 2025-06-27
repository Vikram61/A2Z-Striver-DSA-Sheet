
def next_permutation(arr,n):
    
    n=len(arr)
    i=n-2

    while i>=0 and arr[i]>=arr[i+1]:
        i-=1
    
    if i>=0:
        j=n-1

        while arr[j]<=arr[i]:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[i+1:]=reversed(arr[i+1:])




#Driver Code:

if __name__ == '__main__':
    arr=[1,2,3]
    n=len(arr)

    print(f"Before array : {arr}")

    next_permutation(arr,n)

    print(f"After array : {arr}")