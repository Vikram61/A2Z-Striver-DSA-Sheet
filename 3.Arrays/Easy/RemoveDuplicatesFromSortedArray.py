
def unique(arr):

    i=0
    for j in range(1,len(arr)):

        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    
    return i+1

#Driver Code

if __name__ == '__main__':

    print("Enter the elements : ")
    arr = list(map(int, input().split()))

    print(f"The total number of unique elements are : {unique(arr)}")