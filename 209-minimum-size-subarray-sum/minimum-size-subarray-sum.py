class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left =0
        right =0
        currSum =0
        minLen = float('inf')

        for right in range(len(nums)):
            currSum = currSum + nums[right]
            while currSum >= target:
                minLen = min(minLen, right -left +1)

                currSum -= nums[left]
                left +=1

        return 0 if minLen == float('inf') else minLen

