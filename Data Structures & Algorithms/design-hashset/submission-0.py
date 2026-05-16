# Node untuk linked list
class ListNode:
    def __init__(self, key):
        self.key = key          # nilai yang disimpan
        self.next = None        # pointer ke node berikutnya


class MyHashSet:

    def __init__(self):
        # Membuat 10000 bucket
        # Setiap bucket diawali dummy node
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        # Tentukan bucket berdasarkan hash
        index = key % len(self.set)

        # Mulai dari dummy node
        cur = self.set[index]

        # Traversal linked list
        while cur.next:

            # Kalau key sudah ada, stop
            # HashSet tidak boleh duplikat
            if cur.next.key == key:
                return

            # Geser ke node berikutnya
            cur = cur.next

        # Kalau sampai sini berarti key belum ada
        # Tambahkan node baru di akhir
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        # Cari bucket
        index = key % len(self.set)

        # Mulai dari dummy
        cur = self.set[index]

        # Traversal linked list
        while cur.next:

            # Kalau node berikutnya adalah key yang dicari
            if cur.next.key == key:

                # Skip node tersebut
                # Node sekarang langsung menunjuk ke node setelahnya
                cur.next = cur.next.next
                return

            # Geser maju
            cur = cur.next

    def contains(self, key: int) -> bool:
        # Cari bucket
        index = key % len(self.set)

        # Mulai dari dummy
        cur = self.set[index]

        # Traversal linked list
        while cur.next:

            # Kalau ketemu
            if cur.next.key == key:
                return True

            # Geser maju
            cur = cur.next

        # Kalau habis dan tidak ketemu
        return False