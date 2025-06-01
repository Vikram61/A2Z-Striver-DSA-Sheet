


def answer(l):
    dict={}

    for i in l:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    ans=0
    ans_key=[]
    ans=max(dict.values())
    for key,value in dict.items():
        if value==ans:
            ans_key.append(key)


    return (min(ans_key))


#Driver Code

if __name__ == '__main__':
    print("Enter elements of the array : ")
    l=list(map(int,input().split()))

    print(f"The most occuring element is : {answer(l)}")
