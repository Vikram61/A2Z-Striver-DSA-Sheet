
def count_of_digits(n):

    count=0      

    while n!=0:
        n=n//10               
        count+=1

    return count




#Driver Code
if __name__ == '__main__':

    n=int(input("Enter a number"))

    print(count_of_digits(n))