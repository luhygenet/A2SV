class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pref = [0] * (n + 1)

        for i in bookings:
            l = i[0]
            r = i[1]
            booked = i[2]
            pref[l-1] += booked
            pref[r] -= booked
        
        for i in range(1,n):
            pref[i] += pref[i-1]
        return pref[:n]
