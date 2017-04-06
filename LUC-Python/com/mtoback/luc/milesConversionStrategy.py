'''
Created on Apr 5, 2017

@author: mtoback
'''
from com.mtoback.luc.conversionStrategy import ConversionStrategy
from com.mtoback.luc.units import Units


class MilesConversionStrategy(ConversionStrategy):
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
            obj.length *=  63360.0
            obj.unit = dest

        elif dest == Units.FEET:
            obj.length *=  5280.0
            obj.unit = dest
        
        elif dest == Units.MILES:
            obj.length *=   1.0
            obj.unit = dest
            
        elif dest == Units.CENTIMETERS:
            obj.length *=  160934.4
            obj.unit = dest
            
        elif dest == Units.METERS:
            obj.length *=   1609.344
            obj.unit = dest
            
        elif dest == Units.KILOMETERS:
            obj.length *=  1.609344
            obj.unit = dest
        return obj