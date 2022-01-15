class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        st = ['a', 'b', 'c']
        store = []

        def generate(path):
            if len(path) == n:
                store.append("".join(path))
                return

            if len(store) > k:
                return

            for i in range(len(st)):
                if st[i] != path[-1]:
                    generate(path + [st[i]])

        for i in range(len(st)):
            generate([st[i]])

        if k - 1 > len(store) - 1: return ""
        return store[k - 1]