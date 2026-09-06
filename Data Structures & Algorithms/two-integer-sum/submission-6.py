class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # target - curr = what we need
        # if what we need is in the dict, return it's indices

        count = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in count:
                return [count[diff], i]
            else:
                # we didn't want to say the DIFFERENCE was in the dictionary, we wanted to say the COUNT of the number was in the dictionary
                count[num] = i
