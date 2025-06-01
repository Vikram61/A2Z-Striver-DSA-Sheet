def max_ele(l):
    n=len(l)

    ans=l[0]

    for i in range(1,n):
        if l[i]>ans:
            ans=l[i]
    return ans


#Driver Code

if __name__ == '__main__':
    print('Enter elements in the array')
    l=list(map(int,input().split()))
    print(f"Max element in the array is : {max_ele(l)}")