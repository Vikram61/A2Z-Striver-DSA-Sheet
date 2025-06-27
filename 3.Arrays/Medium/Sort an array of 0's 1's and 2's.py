
def sort_arr(nums,n):

    n=len(nums)
    lo=0
    mid=0
    hi=n-1

    while mid<=hi:
        if nums[mid]==0:
            nums[lo],nums[mid]=nums[mid],nums[lo]
            lo+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[hi]=nums[hi],nums[mid]
            hi-=1
            
        

#Driver COde
if __name__ == "__main__":
    nums=[0,1,0,2,1,1,2,0,0,0,0,1,2,1,2]
    n=len(nums)
    print(f"Before sorting the array : {nums}")
    sort_arr(nums,n)
    print(f" After sorting the array : {nums}")