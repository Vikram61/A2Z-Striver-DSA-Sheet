def union(arr1,arr2):

    arr3=[]
    dict={}

    for i in arr1:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in arr2:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    arr3=sorted(dict.keys())
    return arr3


#Driver Code

if __name__ == '__main__':

    arr1=[1,1,2,3,4,5]
    arr2=[1,1,2,4,5,6,7]

    arr3=union(arr1,arr2)
    print(f"The union of two sorted arrays is {arr3}")