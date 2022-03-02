class Solution:
    @staticmethod
    def countNegatives(grid: list[int]) -> int:
        count = 0
        for li in grid:
            for i in li[::-1]:
                if i < 0:
                    count += 1
                else:
                    break
        return count

        


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(Solution.countNegatives(grid))