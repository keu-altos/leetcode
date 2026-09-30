from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

if __name__ == "__main__":
    solution = Solution()
    nums = [1,4,1,2]
    print(solution.getConcatenation(nums))
    nums = [22,21,20,1]
    print(solution.getConcatenation(nums))