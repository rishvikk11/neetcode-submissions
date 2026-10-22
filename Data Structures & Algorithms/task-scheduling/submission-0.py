class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        available = [-cnt for cnt in count.values()]
        heapq.heapify(available)

        busy = deque()
        time = 0
        while available or busy:
            time += 1
            if not available:
                time = busy[0][1]
            else:
                tasks = 1 + heapq.heappop(available)
                if tasks < 0:
                    busy.append([tasks, time+n])
            if busy and busy[0][1] == time:
                heapq.heappush(available, busy.popleft()[0])

        return time