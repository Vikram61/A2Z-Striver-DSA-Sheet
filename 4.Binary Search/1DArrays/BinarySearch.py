def binarySearch(arr,n,target):

    low=0
    high=n-1

    while low<=high:

        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

#Driver Code

if __name__ == "__main__":

    arr=[-1,0,3,5,9,12]
    n=len(arr)
    target=9

    index=binarySearch(arr,n,target)

    if index==-1:
        print(f"The element is not present in the array")
    else:
        print(f"The element is present at index {index}")