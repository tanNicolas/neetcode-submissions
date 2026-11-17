class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            popped = nums.pop()
            if popped in nums:
                return True
        return False
        
