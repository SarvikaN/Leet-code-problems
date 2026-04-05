class Solution(object):
    def lengthOfLongestSubstring(self, s):
        c=0
        for i in range(len(s)):
            se=""
            for j in range(i,len(s)):
                if s[j] in se:
                    break
                se+=s[j]
            c=max(c,len(se))
        return c
