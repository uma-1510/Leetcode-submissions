class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetMap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in targetMap:
                return [targetMap[diff], i]
            targetMap[val] = i
        return

        