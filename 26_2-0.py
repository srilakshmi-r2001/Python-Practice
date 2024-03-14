class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L=[]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    L.extend(i,j)
                j=j+1
            i=i+1
        return L
sol = Solution()
nums=[2,7,11,15]
target = 9
list1=sol.twoSum(nums, target)
print(list1)