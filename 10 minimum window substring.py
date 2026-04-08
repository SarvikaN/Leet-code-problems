class Solution(object):
    def minWindow(self, s, t):
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        left = 0
        count = 0
        min_len = float('inf')
        res = ""
        for right in range(len(s)):
            if s[right] in need:
                need[s[right]] -= 1
                if need[s[right]] >= 0:
                    count += 1
            while count == len(t):
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]
                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        count -= 1
                left += 1
        return res
