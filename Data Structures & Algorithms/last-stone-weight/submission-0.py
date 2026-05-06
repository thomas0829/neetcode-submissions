class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        while n > 0:
            if n == 1:
                return stones[0]
            new = sorted(stones)
            x = new[-1]
            y = new[-2]

            if x - y == 0:
                stones.remove(x)
                stones.remove(y)
                n -= 2
            else:
                stones.remove(y)
                idx = stones.index(x)
                stones[idx] = x - y
                n -= 1

        return 0
