class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        array = []
        i = 1
        while (len(array)<k):
            if i not in arr:
                array.append(i)
            i=i+1
        return array[k-1]