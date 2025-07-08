def reverseWords(s,n):

    s=s.strip()
    sc=s.split()
    s1=""

    for i in range(len(sc)-1,-1,-1):
        s1+=sc[i]
        s1+=" "
    
    return s1.strip()


#Driver code

if __name__=="__main__":
    s="the sky is     blue"
    n=len(s)

    print(f"After reversing the words : {reverseWords(s,n)}")