class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = nums.copy()
        answer = [None, None]
        while True:
            popped = nums.pop(0)
            rest = target - popped
            if rest in nums:
                break
        answer[0] = nums_copy.index(popped)
        answer[1] = nums_copy.index(rest)
        if answer[0] == answer[1]:
            answer[1] = nums_copy.index(rest, answer[1] + 1)
        return answer
