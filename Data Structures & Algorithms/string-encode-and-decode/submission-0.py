class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # cari delimiter '#'
            while s[j] != "#":
                j += 1

            # ambil panjang string
            length = int(s[i:j])

            # ambil isi string
            word = s[j+1 : j+1+length]
            res.append(word)

            # pindah ke string berikutnya
            i = j + 1 + length

        return res