class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sums = sum(distance)
        if start>destination:
            left=(sum(distance[start:])+ sum(distance[:destination]))
        else: 
            left = sum(distance[start:destination])
        first_distance = sums - left
        return min(first_distance, left)

        
