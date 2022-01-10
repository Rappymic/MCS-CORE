class Solution:
    @staticmethod
    def minimumEffort(tasks) -> int:
        tasks.sort(key=lambda task: task[1] - task[0])

        energy = 0
        for task in tasks:
            energy = max(energy, task[1] - task[0]) + task[0]

        return energy