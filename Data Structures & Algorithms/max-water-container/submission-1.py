class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        maxArea = 0

        while l < r:

            # Hitung lebar container
            width = r - l

            # Tinggi container ditentukan oleh
            # bar yang lebih pendek
            containerHeight = min(height[l], height[r])

            # Hitung luas
            area = width * containerHeight

            # Simpan area terbesar
            maxArea = max(maxArea, area)

            # Geser pointer yang lebih pendek
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea