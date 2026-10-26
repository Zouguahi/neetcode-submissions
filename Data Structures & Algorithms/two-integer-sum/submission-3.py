class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible={}
        n=len(nums)
        for i in range(n):
            if target - nums[i] in possible :
                return [possible[target-nums[i]],i]
            possible[nums[i]]=i