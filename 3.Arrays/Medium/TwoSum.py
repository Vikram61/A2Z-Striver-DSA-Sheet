
def twoSum(arr,n,target):

    dict={}

    for i,num in enumerate(arr):

        if target-num in dict:
            return [dict[target-num],i]
        
        dict[num]=i
    
    return [-1,-1] 



#Driver Code
if __name__ == "__main__":
    arr=[2,7,11,15]
    n=len(arr)
    target=9
    ans=twoSum(arr,n,target)
    print(f"The indices of the two elements are : {ans}")