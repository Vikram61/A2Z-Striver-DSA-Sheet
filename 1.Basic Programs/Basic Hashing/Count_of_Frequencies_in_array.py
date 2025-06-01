#Driver Code

if __name__ == '__main__':

    l=[]
    print('Enter the array elements : ')
    l=list(map(int,input().split()))

    dict={}

    for i in l:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    for key,value in dict.items():
        print(f"{key} : {value},",end=" ")
    print()
