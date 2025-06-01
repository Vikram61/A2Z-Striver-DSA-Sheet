
def insertion(l):

    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=key



#Driver Code

if __name__ == '__main__':

    print("Enter the elements of array : ")
    l=list(map(int,input().split()))

    print('Before Sorting :')
    print(l)

    insertion(l)

    print("After Sorting")
    print(l)