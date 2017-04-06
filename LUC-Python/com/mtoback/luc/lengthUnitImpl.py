'''
Created on Apr 5, 2017

@author: mtoback
'''
from com.mtoback.luc.conversionStrategy import ConversionStrategy
from com.mtoback.luc.conversionStrategies import ConversionStrategies
from com.mtoback.luc.lengthUnit import LengthUnit
class LengthUnitImpl(LengthUnit):
    '''
    classdocs
    '''

    def __init__(self, length, unit):
        '''
        Constructor
        '''
        self.length = length 
        self.unit = unit
        if self.unit is not None and self.unit not in ConversionStrategies.convStratMap:
            raise ValueError(self.unit, " invalid, must be one of: ", ','.join(ConversionStrategies.convStratMap.keys()))
        if self.unit is not None:
            self.strategy = ConversionStrategies.convStratMap[self.unit]
        
    def __equals__(self, another):
        if self.unit == another.unit:
            if self.length == another.length:
                return True
            else:
                return False
        else:
            other = another.convert(self.unit)
            if other.length == self.length:
                return True
            else:
                return False
        
    def convert(self, dest):
        if self.strategy is None:
            self.strategy = ConversionStrategies.convStratMap[self.unit]
        return self.strategy.convert(self, dest)
    
    def __str__(self):
        return str(self.length) + " " + self.unit