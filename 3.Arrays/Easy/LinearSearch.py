def linear(arr,n,key):
    for i in range(0,n):
        if(arr[i]==key):
            return i
    return -1



#Driver Code
if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,3]
    key=3

    print(f"The samllest index of the element {key} is {linear(arr,len(arr),key)}")