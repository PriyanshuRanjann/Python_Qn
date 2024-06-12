
class Solution:
    def countNumberswith4(self, n : int) -> int:
        x=0
        for i in range (1,n+1):
            convert=str(i)
            if "4" in convert:
                x=x+1
        return x
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends