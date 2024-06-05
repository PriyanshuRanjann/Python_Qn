#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        p=[]
        n=[]
        for i in range(len(arr)):
            if arr[i]<0:
                n.append(arr[i])
            else:
                p.append(arr[i])
        final=p+n
        for i in range(len(arr)):
            arr[i]=final[i]
        return arr
        # Your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends