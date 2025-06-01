import math
def isPrime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

#)
#Driver Code

if __name__ == '__main__':

    n=int(input('Enter a number : '))

    ans=isPrime(n)
    if ans:
        print("It is a prime number")
    else:
        print("It is not a prime number")