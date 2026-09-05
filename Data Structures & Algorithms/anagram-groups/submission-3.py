class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # whiteboarding:
        # list for all the character frequencies

        # step 1) for each word, create a list for char freqs
        # step 2) lists of the same will be grouped together in the same list
        # step 3) store them in a hash map: key can be the list, and the value can be a list of the words that correspond to that char freq list
        # step 4) we can return the values as a list

        word_map = {}


        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            if tuple(count) in word_map:
                word_map[tuple(count)].append(word) 
            else:
                word_map[tuple(count)] = []
                word_map[tuple(count)].append(word)
        
        return list(word_map.values())






        
        