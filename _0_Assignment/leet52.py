class Solution:
    @staticmethod
    def countServers(grid) -> int:
        count = 0
        for index, value in enumerate(grid):
            for sub_ind, sub_val in enumerate(value[:-1]):
                if sub_val == 1:
                    if sub_val == value[sub_ind + 1]:
                        count+=2
                        try:
                            if value[sub_ind-1] == 1:
                                count -= 1
                        except:
                            pass
                    if sub_val == grid[index+1][sub_ind]:
                        count +=2
                        try:
                            if sub_val == grid[index-1][sub_ind]:
                                count -= 1
                        except:
                            pass
        return count
        pass





grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

print(Solution.countServers(grid))

