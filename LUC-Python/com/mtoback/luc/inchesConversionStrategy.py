'''
Created on Apr 5, 2017

@author: mtoback
'''
from com.mtoback.luc.conversionStrategy import ConversionStrategy
from com.mtoback.luc.units import Units

class InchesConversionStrategy(ConversionStrategy):
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
            obj.length *=  1.0
            obj.unit = dest

        elif dest == Units.FEET:
            obj.length *= 0.0833333
            obj.unit = dest
        
        elif dest == Units.MILES:
            obj.length *=  1.5782828e-5
            obj.unit = dest
            
        elif dest == Units.CENTIMETERS:
            obj.length *=  2.54
            obj.unit = dest
            
        elif dest == Units.METERS:
            obj.length *=  0.0254
            obj.unit = dest
            
        elif dest == Units.KILOMETERS:
            obj.length *=  2.54e-5
            obj.unit = dest
        return obj