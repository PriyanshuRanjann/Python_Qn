#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        MOD = 10**9 + 7
    
        if n == 0 or n == 1 or n == 2:
            return 1
        
        # Initialize the first three elements of the Padovan sequence
        P0, P1, P2 = 1, 1, 1
        
        for i in range(3, n + 1):
            P_next = (P1 + P0) % MOD
            # Shift the values for the next iteration
            P0, P1, P2 = P1, P2, P_next
        
        return P2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends