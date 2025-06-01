

def merge(l,left,mid,right):
    n1=mid-left+1
    n2=right-mid
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=l[left+i]
    for j in range(n2):
        R[j]=l[mid+1+j]
    i=0
    j=0
    k=left
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            l[k]=L[i]
            i+=1
        else:
            l[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        l[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        l[k]=R[j]
        j+=1
        k+=1




def merge_sort(l,left,right):
    if left<right:
        mid=(left+right)//2
        merge_sort(l,left,mid)
        merge_sort(l,mid+1,right)
        merge(l,left,mid,right)





#Driver Code
if __name__ == '__main__':

    print('Enter elements of the array : ')

    l=list(map(int,input().split()))

    print('Before Sorting :')
    print(l)
    merge_sort(l,0,len(l)-1)
    print('After Sorting')
    print(l)