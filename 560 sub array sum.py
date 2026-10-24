class Solution(object):
    def subarraySum(self, nums, k):
        d = {0: 1}
        s = 0
        count = 0
        for num in nums:
            s += num
            if (s - k) in d:
                count += d[s - k]
            d[s] = d.get(s, 0) + 1
        return count
