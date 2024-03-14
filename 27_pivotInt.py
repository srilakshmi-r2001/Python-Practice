class Solution:
    def pivotInteger(self,n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        sum=0
        for i in range(1,n):
            sum=i+sum
            count=count+1
            sum1=i+count-1
            for j in range(i+count,n):
                sum1=j+sum1
                j=j+1
            if(sum==sum1):
                piv=i+count
                return piv
            else:
                return -1
            i=i+1

sol=Solution()
n=8
output=sol.pivotInteger(n)
print(output)