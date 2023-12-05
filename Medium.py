from collections import Counter

def findFrequentElements(nums):
    frequency = Counter(nums)
    result = [key for key, value in frequency.items() if value > len(nums) // 3]
    return result