class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible={}
        for index,value in enumerate(nums):
            if target - value in possible :
                return [possible[target-value],index]
            possible[value]=index