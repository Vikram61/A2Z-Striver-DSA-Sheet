def maxConsecutiveOnes(arr,n):

    max_count=0
    count=0

    for i in range(n):
        if arr[i]==1:
            count+=1
        else:
            max_count=max(max_count,count)
            count=0
    return max(max_count,count)


#Driver Code

if __name__=='__main__':

    arr=[1,1,0,1,1,1,0,1,1,0,0,1,1]
    n=len(arr)

    print(f"The count of maximum consecutive 1's is : {maxConsecutiveOnes(arr,n)}")