



#Driver Code
print("Enter elements in a range : ")

arr=list(map(int,input().split()))
n=len(arr)

natural_sum= (n * (n+1))//2

print(f"The missing number in the range of 0 to {n} is : {abs(natural_sum - sum(arr))}")
