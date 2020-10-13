class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        ans = cur = start = 0
        for index,c in enumerate(s):
            if c in seen and seen[c] >= start:
                ans = max(ans,cur)
                cur = index - seen[c]
                start = seen[c] + 1
            else:
                cur += 1
            seen[c] = index
        return max(ans,cur)
