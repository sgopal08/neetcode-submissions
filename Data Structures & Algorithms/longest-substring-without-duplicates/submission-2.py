class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # s = "zxyzxyz"
        #.     l
        #      r

        # conditions:
        # if current character already in window, remove it
        # if it's not, then add it to window, t

        # s="pwwkew"
        #.     r
        #.    l

        # window = pw    # res = 2

        l = 0 
        window = set()

        res = 0

        for r in range(len(s)):

            while s[r] in window: # shrink if repeated character is still there
                window.remove(s[l]) 
                l += 1
            
            window.add(s[r])

            res = max(res, (r - l + 1))
        
        return res
            




        