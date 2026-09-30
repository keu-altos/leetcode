from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 3]
    print(solution.hasDuplicate(nums))  # True

    nums = [1, 2, 3, 4]
    print(solution.hasDuplicate(nums))  # False
