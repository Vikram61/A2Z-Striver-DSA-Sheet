
def rearrange_elements(nums,n):

    pos=[]
    neg=[]

    for i in nums:
        if i>0:
            pos.append(i)
        else:
            neg.append(i)
        po,no=0,0
    for i in range(len(nums)):

        if i%2==0:
            nums[i]=pos[po]
            po+=1
        else:
            nums[i]=neg[no]
            no+=1
    return nums
        




#Driver Code
if __name__ == '__main__':

    arr=[3,1,-2,-5,2,-4]
    n=len(arr)

    print(f"Before arranging : {arr}")

    rearrange_elements(arr,n)

    print(f"After arranging : {arr}")