'''
Created on Apr 6, 2017

@author: mtoback
'''
from com.mtoback.luc.centimetersConversionStrategy import CentimetersConversionStrategy
from com.mtoback.luc.feetConversionStrategy import FeetConversionStrategy
from com.mtoback.luc.inchesConversionStrategy import InchesConversionStrategy
from com.mtoback.luc.kilometersConversionStrategy import KilometersConversionStrategy
from com.mtoback.luc.metersConversionStrategy import MetersConversionStrategy
from com.mtoback.luc.milesConversionStrategy import MilesConversionStrategy
from com.mtoback.luc.units import Units

class ConversionStrategies(object):
    '''
    classdocs
    '''
    convStratMap = {
        Units.INCHES: InchesConversionStrategy(),
        Units.FEET: FeetConversionStrategy(),
        Units.MILES: MilesConversionStrategy(),
        Units.CENTIMETERS: CentimetersConversionStrategy(),
        Units.METERS : MetersConversionStrategy(),
        Units.KILOMETERS: KilometersConversionStrategy()
    }
    def __init__(self):
        '''
        Constructor
        '''
        pass
        