#Returs True if the number is a palindrome

def is_palindrome(n):

    O_num=n
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10

    return O_num==rev



#Drive Code

if __name__ == "__main__":

    n=int(input("Enter a number :"))

    answer=is_palindrome(n)

    if answer:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")