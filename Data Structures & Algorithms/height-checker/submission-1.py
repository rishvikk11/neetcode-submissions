class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # to avoid sorting runtime, we can use count array
        cnt = [0] * 101 # only 100 numbers provided in constraint
        for h in heights:
            cnt[h] += 1

        expected = []
        for i in range(1, len(cnt)):
            for _ in range(cnt[i]):
                expected.append(i)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res