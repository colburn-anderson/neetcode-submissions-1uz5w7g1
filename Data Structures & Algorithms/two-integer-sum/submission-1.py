class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        counts = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in counts:
                return [counts[complement], i]
            counts[num] = i    
        
        
