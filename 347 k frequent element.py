class Solution(object):
    def topKFrequent(self, nums, k):
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        s=sorted(f,key=f.get,reverse=True)
        return s[:k]  
