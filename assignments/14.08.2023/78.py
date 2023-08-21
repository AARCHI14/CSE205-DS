class Solution(object):
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        def reccursiveFunction(i,path):
            result.append(path)
            for j in range(i,len(nums)):
                reccursiveFunction(j+1,path+[nums[j]])
        result = []
        reccursiveFunction(0,[])
        return result