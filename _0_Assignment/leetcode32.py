def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    s = []
    ans = [0] * n
    last = 0
    for i, log in enumerate(logs):
        _id, action, time = log.split(":")
        if action == "start":
            if s:
                ans[int(s[-1])] += int(time) - last
            last = int(time)
            s.append(_id)
        else:
            ans[int(s[-1])] += int(time) - last + 1
            s.pop()
            last = int(time) + 1
    return ans