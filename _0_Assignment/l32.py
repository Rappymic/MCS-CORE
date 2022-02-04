class Solution:
    @staticmethod
    def robotSim(commands: list, obstacles: list) -> int:
        position = [0,0]
        position1 = [0,0]
        index = 1
        multiplier = 1
        direction = 1 # 1- North, 2- east, 3- South, 4- West
        for comm in commands:
            if direction > 4:
                direction = 1
            elif direction < 1:
                direction = 4
            if comm == -1:
                direction += 1
                continue
            elif comm == -2:
                direction -= 1
                continue
            if direction == 1:
                index = 1
                multiplier = 1
            elif direction == 2:
                index = 0
                multiplier = 1
            elif direction == 3:
                index = 1
                multiplier = -1
            elif direction == 4:
                index = 0
                multiplier = -1
            position[index] += comm * multiplier
        return position[0]**2 + position[1]**2




commands = [4,-1,3]
obstacles = []

print(Solution.robotSim(commands, obstacles))