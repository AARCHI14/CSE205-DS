class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        array = []
        sum = 0
        for i in nums:
            if i==1:
                sum = sum+1
            elif i==0:
                array.append(sum)
                sum = 0
        array.append(sum)
        array.sort()
        return array[-1]