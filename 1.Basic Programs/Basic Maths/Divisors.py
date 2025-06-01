
def divisors(n):
    a=[]
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)
    return a


#Driver Code

if __name__ == "__main__":
    n=int(input("Enter a number : "))
    a=divisors(n)
    for i in a:
        print(i,end=" ")
    print()