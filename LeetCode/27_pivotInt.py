#floppiana 
class Solution:
    def pivotInteger(self, n):
        sum1=0
        sum2=0
        count=0
        x=2
        m=1
        while(m):
            for i in range(1,x):
                sum1=sum1+i
                count=count+1
            for j in range(count,n):
                sum2=sum2+j
            if(sum1==sum2):
                m=0
            if(x<n):
                x=x+1
        if(sum1==sum2):
            return count 
        else:
            return -1
        
sol=Solution()
n=8
piv=sol.pivotInteger(n)
print(piv)