class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if (not diff in myMap):
                myMap[nums[i]] = i
            else:
                return [myMap[diff], i]