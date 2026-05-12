class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # dictionary untuk menyimpan:
        # angka : index
        seen = {}

        # loop semua isi nums
        # i   = index
        # num = nilai angka
        for i, num in enumerate(nums):

            # cari angka pasangan yang dibutuhkan
            # agar num + gap = target
            gap = target - num

            # cek apakah gap sudah pernah ditemukan sebelumnya
            if gap in seen:

                # kalau ada:
                # ambil index gap dari dictionary
                # lalu return index pasangan
                return [seen[gap], i]

            # simpan angka sekarang beserta indexnya
            # format:
            # seen[angka] = index
            seen[num] = i

        # fallback kalau tidak ada jawaban
        return []