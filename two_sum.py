from typing import List


class SolutionTwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            difference = target - nums[i]
            if nums.__contains__(difference).__index__():
                if nums.index(difference) != i:
                    return [i, nums.index(difference)]

