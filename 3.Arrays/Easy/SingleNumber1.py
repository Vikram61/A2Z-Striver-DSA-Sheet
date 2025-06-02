
def appears_once(arr,n):

    dict={}

    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    for key,value in dict.items():
        if value==1:
            return key
    
    return -1



#Drive Code

if __name__ == "__main__":
    arr=[1, 2, 2, 4, 3, 1, 4]
    n=len(arr)

    print(f"The element that appears once is : {appears_once(arr, n)}")