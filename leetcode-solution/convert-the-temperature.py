class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=celsius+273.15
        f=(celsius*9/5)+32
        ans=[kelvin, f]
        return ans