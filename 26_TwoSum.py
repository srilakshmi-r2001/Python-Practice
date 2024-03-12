class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=1
        for i in nums:
            for j in nums:
                if(i+j==target):
                    print("[",nums.index(i),",",nums.index(j),"]")
                j=j+1
            i=i+1   

sol=Solution()
nums=[]
size=int(input("Enter the size of the list:"))
for i in range(size):
    ele=int(input("Enter list element:"))
    nums.append(ele)
target=int(input("Enter the target:"))
print("List=",nums)
sol.twoSum(nums,target)