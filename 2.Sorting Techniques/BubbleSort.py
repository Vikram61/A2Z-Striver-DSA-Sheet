def bubble_sort(l):
    n=len(l)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j]=l[j]^l[j+1]
                l[j+1]=l[j]^l[j+1]
                l[j]=l[j]^l[j+1]
                


#Driver code

if __name__ == '__main__':

    print("Enter elements in the array : ")
    l=list(map(int,input().split()))

    print('Before Sorting : ')
    print(l)

    bubble_sort(l)

    print('After Sorting : ')
    print(l)