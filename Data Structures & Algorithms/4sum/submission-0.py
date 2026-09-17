class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # Urutkan array agar two pointers bisa digunakan
        nums.sort()

        # i = angka pertama
        # Kita berhenti di len(nums) - 3 karena
        # setelah i masih membutuhkan j, l, dan r
        for i, a in enumerate(nums[:-3]):

            # Skip duplicate untuk angka pertama
            if i > 0 and a == nums[i - 1]:
                continue

            # j = angka kedua
            # Setelah j masih membutuhkan l dan r
            for j in range(i + 1, len(nums) - 2):

                # Skip duplicate untuk angka kedua
                # j pertama tetap boleh sama dengan i
                # Contoh: [1, 1, 2, 3] -> 1 + 1 + 2 + 3
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # l = angka ketiga
                # r = angka keempat
                l = j + 1
                r = len(nums) - 1

                while l < r:

                    fourSum = a + nums[j] + nums[l] + nums[r]

                    # Jumlah terlalu besar
                    # Kurangi nilai dengan menggeser r ke kiri
                    if fourSum > target:
                        r -= 1

                    # Jumlah terlalu kecil
                    # Tambah nilai dengan menggeser l ke kanan
                    elif fourSum < target:
                        l += 1

                    # Jumlah tepat sama dengan target
                    else:
                        res.append([
                            a,
                            nums[j],
                            nums[l],
                            nums[r]
                        ])

                        # Cari pasangan baru
                        l += 1
                        r -= 1

                        # Skip duplicate dari sisi kiri
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        # Skip duplicate dari sisi kanan
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

        return res