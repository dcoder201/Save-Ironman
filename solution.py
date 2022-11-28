#User function Template for python3

def saveIronman (s) : 
    #Complete the function
    fina=''
    for i in s:
        if i.isalnum():
            fina+=i.lower()
    if fina==fina[::-1]:
        return(True)
    else:
        return(False)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    s = input()
    ans = saveIronman(s)
    if(ans == True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends
