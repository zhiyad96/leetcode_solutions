class Solution(object):
    def convertTemperature(self, celsius):
        kelvin=celsius + 273.15
        far=celsius*1.80+32.00
        result=[kelvin,far]
        return result
        