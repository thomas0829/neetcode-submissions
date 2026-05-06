class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        starting_frequency = nums.count(k)
        max_duplicates = 0
        for target_value in range(1, 51):
            if target_value == k:
                continue
            current_freq = 0
            current_max = 0
            for num in nums:
                if num == target_value:
                    current_freq += 1
                elif num == k:
                    current_freq -= 1
                current_freq = max(current_freq, 0)
                current_max = max(current_max, current_freq)
            max_duplicates = max(max_duplicates, current_max)
        return max_duplicates + starting_frequency

