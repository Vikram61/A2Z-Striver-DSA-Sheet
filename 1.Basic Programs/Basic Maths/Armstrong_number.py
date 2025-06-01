def is_Armstrong(n,l):
    sum=0
    O_num=n
    while n!=0:
        a=n%10
        sum = sum + a**l
        n=n//10
    return O_num==sum


#Driver Code

if __name__ == '__main__':

    n=int(input("Enter a number "))
    s=str(n)
    if len(s)<2:
        print("Please enter a number greater than 9")
    else:
        ans=is_Armstrong(n,len(s))
        if ans:
            print("The number is an Armstrong number")
        else:
            print("The number is not an Armstrong number")