#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        initial_diff=arr[n-1]-arr[0]
        min_height=arr[0]+k
        max_height=arr[n-1]-k
        
        for i in range(n-1):
            min_h=min(min_height,arr[i+1]-k)
            max_h=max(max_height,arr[i]+k)
            if min_h<0:
                continue
            initial_diff=min(initial_diff,max_h-min_h)
        return initial_diff
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends