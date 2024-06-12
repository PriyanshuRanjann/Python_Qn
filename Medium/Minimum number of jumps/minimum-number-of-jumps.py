#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    if n<=1:
	        return 0
	    if arr[0]>=n-1:
	        return 1
	    if arr[0]==0:
	        return -1
	    maxR=arr[0]
	    step=arr[0]
	    jump=1
	    
	    
	    for i in range(1,n):
	        if i==n-1:
	            return jump
	        if arr[i]>=(n-1)-i:
	            return jump+1
	        maxR=max(maxR,i+arr[i])
	        step=step-1
	        
	        if step==0:
	            jump=jump+1
	            if(i>=maxR):
	                return -1
	            step=maxR-i
        return -1
	        
	        
	    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends