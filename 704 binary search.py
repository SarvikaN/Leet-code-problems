class Solution(object):
    def search(self, nums, target):
        l,h=0,len(nums)-1
        while l<=h:
            m=l+(h-l)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1
        return -1
