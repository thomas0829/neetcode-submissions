class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse = True)
        tmp = self.k
        for i in range(len(self.nums)):
            tmp -= 1
            if tmp == 0:
                return self.nums[i]
