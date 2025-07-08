
def isIsomorphic(s,t):
    a,b={},{}

    for ch1,ch2 in zip(s,t):
        if ch1 in a:
            if a[ch1]!=ch2:
                return False
        else:
            a[ch1]=ch2
        
        if ch2 in b:
            if b[ch2]!=ch1:
                return False
        else:
            b[ch2]=ch1
    return True

#Driver Code

if __name__=="__main__":
    s="egg"
    t="add"
    print(isIsomorphic(s,t))
    