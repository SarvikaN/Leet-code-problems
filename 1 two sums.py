class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i,num in enumerate(nums):
            c=target-num
            if c in m:
                return[m[c],i]
            m[num]=i
        return []
