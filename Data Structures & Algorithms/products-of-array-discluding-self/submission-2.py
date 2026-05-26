class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # prefix: product semua angka di kiri i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # postfix: product semua angka di kanan i
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res