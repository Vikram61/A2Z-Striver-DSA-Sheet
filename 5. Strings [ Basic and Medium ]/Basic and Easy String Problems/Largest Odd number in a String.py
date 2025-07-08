def largestOddNumber(num: str) -> str:
    index=-1
    n=len(num)
    for i in range(n-1,-1,-1):
        k=int(num[i])
        if k%2==1:
            index=i
            break
    
    if index==-1:
        return ""
    
    return num[:index+1]

if __name__=="__main__":
    s="35427"
    print(largestOddNumber(s))