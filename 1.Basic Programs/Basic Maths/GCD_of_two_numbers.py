
def gcd(n1,n2):
    while n2!=0:
        n1,n2=n2,n1%n2
    return n1




#Driver Code

if __name__ == '__main__':

    print("Enter two number")
    n1,n2=map(int,input().split())

    print(f" The GCD of two number is {gcd(n1,n2)}")