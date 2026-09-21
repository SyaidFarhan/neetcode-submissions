class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicateSet = set()

        for num in nums:
            if num in duplicateSet:
                return num

            duplicateSet.add(num)