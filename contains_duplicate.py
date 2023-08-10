from typing import List


class Solution(object):

    def contains_duplicate(self, nums: List[int]) -> bool:
        hash_dict = set()

        if 1 >= len(nums):
            return False

        for num in nums:
            if hash_dict.__contains__(num):
                return True
            else:
                hash_dict.add(num)

        return False
