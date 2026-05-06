class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            q.append((-1) * num)
        heapq.heapify(q)
        for i in range(k - 1):
            heapq.heappop(q)
        return heapq.heappop(q) * (-1)