from typing import List

class Solution:
    def getPrimes(self, n: int) -> List[int]:
        if n < 4:
            return [-1, -1]

        # Sieve of Eratosthenes to find all primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        # Find the smallest pair (a, b) such that a + b = n
        for a in range(2, n + 1):
            if is_prime[a]:
                b = n - a
                if b >= 2 and is_prime[b]:
                    return [a, b]

        return [-1, -1]

        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends