'''
Created on Apr 5, 2017

@author: mtoback
'''
from com.mtoback.luc.conversionStrategy import ConversionStrategy
from com.mtoback.luc.units import Units

class KilometersConversionStrategy(ConversionStrategy):
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
            obj.length *=  39370.07874
            obj.unit = dest

        elif dest == Units.FEET:
            obj.length *=  3280.839895
            obj.unit = dest
        
        elif dest == Units.MILES:
            obj.length *=  0.62137119
            obj.unit = dest
            
        elif dest == Units.CENTIMETERS:
            obj.length *=  100000.0
            obj.unit = dest
            
        elif dest == Units.METERS:
            obj.length *=  1000.0
            obj.unit = dest
            
        elif dest == Units.KILOMETERS:
            obj.length *=  1.0
            obj.unit = dest
        return obj