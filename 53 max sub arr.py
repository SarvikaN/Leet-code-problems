class Solution(object):
    def maxSubArray(self, nums):
        m=c=nums[0]
        for i in nums[1:]:
            c=max(i,c+i)
            m=max(m,c)
        return m
