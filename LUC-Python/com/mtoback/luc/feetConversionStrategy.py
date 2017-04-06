'''
Created on Apr 5, 2017

@author: mtoback
'''
from com.mtoback.luc.units import Units
from com.mtoback.luc.conversionStrategy import ConversionStrategy
class FeetConversionStrategy(ConversionStrategy):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def convert(self, obj, dest):
        if dest == Units.INCHES:
            obj.length *=  12.0
            obj.unit = dest

        elif dest == Units.FEET:
            obj.length =  obj.getLength() * 1.0
            obj.unit = dest
        
        elif dest == Units.MILES:
            obj.length *=  0.00018939394
            obj.unit = dest
            
        elif dest == Units.CENTIMETERS:
            obj.length *=  30.48
            obj.unit = dest
            
        elif dest == Units.METERS:
            obj.length *= 0.3048
            obj.unit = dest
            
        elif dest == Units.KILOMETERS:
            obj.length *=  0.0003048
            obj.unit = dest
        return obj
