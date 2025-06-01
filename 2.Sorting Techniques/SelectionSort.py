def selection(l):

    for i in range(len(l)):
        min_index=i

        for j in range(i+1,len(l)):

            if l[j] < l[min_index]:
                min_index=j

        l[i],l[min_index]=l[min_index],l[i]
        

#Driver Code

if __name__ == '__main__':

    print('Enter the elements of array : ')
    l=list(map(int,input().split()))

    print("Before Sorting : ")

    print(l)

    selection(l)

    print("After Sorting : ")

    print(l)