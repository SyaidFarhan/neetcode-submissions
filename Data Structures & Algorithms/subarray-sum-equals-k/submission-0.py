class Solution:
    def subarraySum(self, nums, k):
        count = {0: 1}
        prefix = 0
        answer = 0

        for n in nums:
            prefix += n

            answer += count.get(prefix - k, 0)

            count[prefix] = count.get(prefix, 0) + 1

        return answer