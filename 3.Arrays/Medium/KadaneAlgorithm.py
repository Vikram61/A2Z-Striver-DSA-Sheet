
def maxSubArraySum(arr):
    result=arr[0]
    n=len(arr)
    currsum=arr[0]

    for i in range(1,n):
        currsum=max(currsum+arr[i],arr[i])
        result=max(result,currsum)

    return result



#Driver Code

if __name__ == '__main__':

    arr=[-2,1,-3,4,-1,2,1,-5,4]

    print(f"Maximum Sub Array sum is : {maxSubArraySum(arr)}")