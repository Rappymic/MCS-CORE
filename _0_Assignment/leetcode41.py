class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        def generateColumn(prev, count):  # find all possible column colour combinations
            if count == m: return [0]
            columns = []
            for colour in (1, 2, 4):
                if colour == prev: continue
                for suffix in generateColumn(colour, count + 1):
                    columns.append((colour << count * 3) | suffix)  # count * 3 because each colour has 3 bits
            return columns

        possibleColumns = generateColumn(0, 0)

        @lru_cache(None)
        def dfs(prevColumn, columnIndex):
            if columnIndex >= n: return 1
            res = 0
            for column in possibleColumns:
                if prevColumn & column: continue
                res = (res + dfs(column, columnIndex + 1)) % MOD
            return res

        return dfs(0, 0)