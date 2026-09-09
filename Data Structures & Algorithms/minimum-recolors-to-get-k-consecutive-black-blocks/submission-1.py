class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        min_ops = float('inf')
        ops = 0

        for r in range(len(blocks)):
            color = blocks[r]
            if color == "W" and r-l+1 < k:
                ops += 1
            elif r-l+1 == k:
                if color == "W":
                    ops += 1
                min_ops = min(min_ops, ops)
                if blocks[l] == "W":
                    ops -= 1
                l += 1
            
        return min_ops
            