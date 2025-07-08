def longestConsecutive(nums) -> int:
    st=set()
    res=0
    cnt=0
    for i in nums:
        st.add(i)
        
    for val in nums:

        if val in st and (val-1) not in st:

            cur=val
            cnt=0
            while cur in st:

                st.remove(cur)
                cur+=1
                cnt+=1
                res=max(res,cnt)
    return res
        


#Driver Code

if __name__=="__main__":
    arr=[100,4,200,1,3,2]
    n=len(arr)

    
    print(f"The longest consecutive sequence is : {longestConsecutive(arr)}")