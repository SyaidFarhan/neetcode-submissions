class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k = k % len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Reverse seluruh array
        reverse(0, len(nums) - 1)

        # Reverse bagian pertama
        reverse(0, k - 1)

        # Reverse bagian kedua
        reverse(k, len(nums) - 1)