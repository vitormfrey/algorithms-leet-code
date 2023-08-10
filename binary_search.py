from typing import List


class SolutionBinarySearch:
    def binarySearch(self, nums: List[int], value: int):
        start = 0
        end = len(nums) - 1
        count = 0
        while(start <= end):
            middle = round((start + end) / 2)
            kick = nums[middle]
            if (kick == value):
                return print(f"Value: {value} and index: {middle}")
            if (kick > value):
                end = middle - 1
            else:
                start = middle + 1
        return None






