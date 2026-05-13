from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for word in strs:

            # buat array 26 huruf alfabet
            count = [0] * 26

            # hitung setiap huruf
            for c in word:
                index = ord(c) - ord('a')
                count[index] += 1

            # list tidak bisa jadi dictionary key
            # jadi ubah ke tuple
            key = tuple(count)

            # kalau key belum ada
            if key not in anag:
                anag[key] = []

            # masukkan kata
            anag[key].append(word)

        return list(anag.values())