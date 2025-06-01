
def reverse(n):
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev






#Driver Code
if __name__ == '__main__':

    n=int(input("Enter a number :"))

    print("The reverse of the number is :" + str(reverse(n)))