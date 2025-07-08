
def minimumCommonLength(s1,s2):
    n1=len(s1)
    n2=len(s2)
    idx=0
    minlen=min(n1,n2)
    while idx < minlen and s1[idx]==s2[idx]:

        idx+=1
    return idx


def longestCommonPrefix(arr):

    res=arr[0]
    n=len(arr)

    for i in range(1,n):

        minLen=minimumCommonLength(res,arr[i])
        res=res[:minLen]
    return res





#Driver COde

if __name__=="__main__":

    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(longestCommonPrefix(arr))