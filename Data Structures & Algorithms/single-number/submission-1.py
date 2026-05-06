class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = {}
        for n in nums:
            table[n] = table.get(n, 0) + 1
        
        result = [k for k, v in table.items() if v == 1]
        
        return result[0]