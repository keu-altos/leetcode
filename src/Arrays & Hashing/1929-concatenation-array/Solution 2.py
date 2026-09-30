from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i, item in enumerate(nums):
            ans.insert(i, item)
            ans.append(item)
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [1,4,1,2]
    print(solution.getConcatenation(nums))
    nums = [22,21,20,1]
    print(solution.getConcatenation(nums))