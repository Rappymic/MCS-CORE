class Solution:
    @staticmethod
    def minimumEffort(tasks: list) -> int:
        task_sort = sorted(tasks, key=lambda x : x[1], reverse=True)
        print(task_sort)
        total_energy = 0
        for i in task_sort:
            total_energy += i[0]

        if total_energy >= task_sort[0][1]:
            return total_energy
        else:
            return task_sort[0][1]

tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]

print(Solution.minimumEffort(tasks))