class Solution:
    # Define a method that returns the k most frequent values.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count how many times each value appears.
        frequency = {}
        
        # Process every value in the input array.
        for value in nums:
            # Increase the current value's count by one.
            frequency[value] = frequency.get(value, 0) + 1
        
        # Create one bucket for every possible frequency from zero through n.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Place each value into the bucket matching its frequency.
        for value, count in frequency.items():
            # Append the value to its frequency bucket.
            buckets[count].append(value)
        
        # Create the list that will store the final answer.
        result = []
        
        # Scan frequencies from highest to lowest.
        for count in range(len(nums), 0, -1):
            # Process every value with this frequency.
            for value in buckets[count]:
                # Add the value to the result.
                result.append(value)
                
                # Stop once k values have been collected.
                if len(result) == k:
                    return result
        
        # Return the result as a fallback.
        return result