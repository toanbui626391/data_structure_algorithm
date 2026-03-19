"""
Given an integer array nums and an integer k,
return the k most frequent elements. You may
return the answer in any order.

Example:
  Input:  nums=[1,1,1,2,2,3], k=2
  Output: [1,2]

Constraints:
  Bucket sort by frequency avoids a heap for O(n).
"""


def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Build frequency map manually with a plain dict.
    freq_map: dict[int, int] = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Index represents frequency; avoids sorting.
    buckets: list[list[int]] = [
        [] for _ in range(len(nums) + 1)
    ]

    # Place each value into the bucket for its count.
    for value, frequency in freq_map.items():
        buckets[frequency].append(value)

    # Collect from highest-frequency buckets first.
    result: list[int] = []
    for i in range(len(buckets) - 1, 0, -1):
        for element in buckets[i]:
            result.append(element)
            if len(result) == k:
                return result

    return result


if __name__ == "__main__":
    # Expected: [1, 2]
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))

    # Expected: [1]
    print(topKFrequent([1], 1))
