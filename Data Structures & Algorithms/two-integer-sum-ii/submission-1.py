class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [1,2,3,4]
        #              r 
        #            l

        # [-1, 2, 4, 5] target = 4

        # 

        # 1 - 3 = 2

        # target = 3

        l, r = 0, len(numbers) - 1

        while l < r:

            # if sum is GREATER than target, then move r down

            sum = numbers[r] + numbers[l]
            
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            elif sum == target:
                return [l + 1, r + 1]
        return []
            



        