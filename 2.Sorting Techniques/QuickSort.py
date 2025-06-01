
def partition(l,low,high):
    i=low-1
    pivot=l[high]
    for j in range(low,high):
        if l[j]<=pivot:
            i+=1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[high]=l[high],l[i+1]
    return i+1

def quick_sort(l,low,high):
    if low<high:
        pi=partition(l,low,high)
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)



#Driver Code
if __name__ == '__main__':

    print('Enter elements of the array : ')

    l=list(map(int,input().split()))

    print('Before Sorting :')
    print(l)
    quick_sort(l,0,len(l)-1)
    print('After Sorting')
    print(l)