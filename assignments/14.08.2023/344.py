class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.s = Solution.reverse(s, len(s) - 1, 0)
            
    def reverse(L, n, i):
        if i >= n:
            return L
        L[i], L[n] = L[n], L[i]
        Solution.reverse(L, n - 1, i + 1)
            