class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # populate counts
        # build frequency table
        # reverse return those values

        # populate counts

       # nums = [1,2,2,2,3,3,3]

        count = defaultdict(int)

        for num in nums:
            count[num] += 1
                        
        # build freq table from count.values()

        freq_count = [[] for _ in range(len(nums) + 1)]# indices represent freq, values are a list of numbers that match that freq

        for num, freq in count.items():
            freq_count[freq].append(num)

        output = []

        for entry in reversed(freq_count):
            for num in entry:
                output.append(num)
            if len(output) == k:
                return output


        
        




            
        