
def majorityElement(arr,n):
    dict={}
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for key,value in dict.items():

        if value > n//2:
            return key
    return -1



#Driver Code

if __name__ == "__main__":

    arr=[2,2,1,1,1,2,2]
    n=len(arr)
    print(f"Majority Element that appears more than n/2 times is : {majorityElement(arr,n)}")