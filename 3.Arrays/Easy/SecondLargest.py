def second(arr):
    n=len(arr)
    second=l[0]
    first_max=max(l)
    for i in range(1,n):

        if l[i]!=first_max:
            if l[i]>second:
                second=l[i]
    return second



#Driver Code

if __name__ == '__main__':
    print("Enter elements of the array")
    l=list(map(int,input().split()))
    print(f"The second largest element is : {second(l)}")