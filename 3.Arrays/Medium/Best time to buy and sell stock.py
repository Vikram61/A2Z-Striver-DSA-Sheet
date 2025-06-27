
def max_profit(arr,n):

    profit=0
    buy=arr[0]

    for i in range(1,n):

        if arr[i]<buy:
            buy=arr[i]
        elif arr[i]-buy>profit:
            profit=arr[i]-buy

    return profit


#Driver Code
if __name__ == '__main__':
    arr=[7,1,5,3,6,4]
    n=len(arr)

    print(f"The max profit is : {max_profit(arr,n)}")