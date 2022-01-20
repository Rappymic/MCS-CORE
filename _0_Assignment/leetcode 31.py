class Solution:
    @staticmethod
    def maxArea(height: list) -> int:
        area = 0
        h1 = 0
        for index in range(len(height)):
            if h1 > height[index]:
                continue
            h2 = 0
            for i in range(len(height)- 1,0, -1):
                if h2 > height[i]:
                    continue
                if i > index:
                    h1 = height[index]
                    h2 = height[i]
                    print(h1, h2)
                    h = min(h1, h2)
                    b = i - index
                    temp_area = h * b
                    if temp_area > area:
                        area = temp_area
        return area





height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(Solution.maxArea(height))