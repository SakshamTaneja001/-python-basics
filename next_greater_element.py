class Solution:
    def checkisgreater(self,nums):
        stack=[]
        result=[-1]*len(nums)
        for j in range(len(nums)):
            while stack and nums[j] > nums[stack[-1]]:
                idx=stack.pop()
                result[idx]=nums[j]
            stack.append(j)
        return result
a=Solution()
nums=list(map(int,input('Enter numbers:').split()))
c=a.checkisgreater(nums)
print(c)