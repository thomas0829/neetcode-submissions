class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            tmp = bin(i)
            count = Counter(tmp)
            ans.append(count["1"])
        return ans