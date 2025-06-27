
def find_leaders(arr,n):

    max_right=arr[n-1]
    res=[]
    res.append(max_right)
    for i in range(n-2,-1,-1):

        if arr[i]>=max_right:
            res.append(arr[i])
            max_right=arr[i]
    res.reverse()
    return res



#Driver code

if __name__ == '__main__':
    arr= [16, 17, 4, 3, 5, 2]
    n= len(arr)
    leaders=find_leaders(arr,n)
    print(f"The array leaders are : {leaders}")