class Solution:
    def isPalindrome(self, s: str) -> bool:
        # is alphanum and case-sensitive

        word = ""

        for char in s.lower():
            if char.isalnum():
                word += char
        
        print(word)
        
        return word == word[::-1]
        