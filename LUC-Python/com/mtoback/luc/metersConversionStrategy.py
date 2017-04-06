'''
Created on Apr 5, 2017

@author: mtoback
'''
from com.mtoback.luc.conversionStrategy import ConversionStrategy
from com.mtoback.luc.units import Units

class MetersConversionStrategy(ConversionStrategy):
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
            obj.length *=  39.37007874
            obj.unit = dest

        elif dest == Units.FEET:
            obj.length *=  3.280839895
            obj.unit = dest
        
        elif dest == Units.MILES:
            obj.length *=  6.2137119e-4 
            obj.unit = dest
            
        elif dest == Units.CENTIMETERS:
            obj.length *= 100.0
            obj.unit = dest
            
        elif dest == Units.METERS:
            obj.length *= 1.0
            obj.unit = dest
            
        elif dest == Units.KILOMETERS:
            obj.length *= 1.0e-3
            obj.unit = dest
        return obj