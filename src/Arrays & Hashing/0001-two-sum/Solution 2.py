from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        for item in nums:
            if item in hashMap:
                return True
            else:
                hashMap.add(item)
        return False
        


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 3]
    print(solution.hasDuplicate(nums))  # True

    nums = [1, 2, 3, 4]
    print(solution.hasDuplicate(nums))  # False
