class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, v in enumerate(nums):
            match = target - v

            if match in seen:
                return [seen[match], i]
            
            seen[v] = i