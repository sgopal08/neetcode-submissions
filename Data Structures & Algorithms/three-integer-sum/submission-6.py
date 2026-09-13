class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #  nums = [-1,0,1,2,-1,-4]
        #           r           
        #             l
        # nums = [-4,-1,-1,0,1,2]
        # 

        # count = {}
        # keys = 

        nums.sort()

        res = []

        count = defaultdict()

        for i, num in enumerate(nums):

            # duplicates
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    # it's a duplicate so shift                
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 
                    
                    # updating pointers:

        return res











        