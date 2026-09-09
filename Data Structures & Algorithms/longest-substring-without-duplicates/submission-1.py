class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # s = "zxyzxyz"
        #       s
        #       e

        # window_length = 2, max_count = 2
        # seen = z

        seen = set()

        count = 0

        l = 0

        for r in range(len(s)):
            # right goes through everything single character
            while s[r] in seen:
                seen.remove(s[l])
                l += 1    
            seen.add(s[r])
            count = max(count, len(s[l:r]) + 1)
        return count

            


        