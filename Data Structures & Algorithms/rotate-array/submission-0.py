class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)

        # Kalau k lebih besar dari panjang array,
        # cukup ambil sisanya.
        k = k % n

        count = 0
        start = 0

        # count = berapa angka yang sudah dipindahkan
        while count < n:

            current = start
            prev = nums[current]

            while True:

                # Hitung index baru untuk angka sekarang
                newIndex = (current + k) % n

                # Simpan angka yang akan tertimpa
                nums[newIndex], prev = prev, nums[newIndex]

                # Kita sudah memindahkan 1 angka
                count += 1

                # Pindah ke index berikutnya
                current = newIndex

                # Kalau kembali ke titik awal,
                # cycle ini sudah selesai
                if current == start:
                    break

            # Mulai cycle berikutnya
            start += 1