
def move_to_end(arr,n):

    insert=0
    for num in arr:
        if num!=0:
            arr[insert]=num
            insert+=1
    while insert<n:
        arr[insert]=0
        insert+=1


#Driver COde

if __name__ == "__main__":

    print("Enter the elements of the array : ")
    arr=list(map(int,input().split()))

    move_to_end(arr,len(arr))

    print(f"After Moving the Zeroes to end the array is : {arr}")