class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        result = []

        for n in count:
            if count[n] > len(nums) // 3:
                result.append(n)

        return result