'''
Created on Apr 5, 2017

@author: mtoback
'''
import sys
from com.mtoback.luc.lengthUnitImpl import LengthUnitImpl
from com.mtoback.luc.conversionStrategies import ConversionStrategies
def convert(length, unit, dest):
    if unit not in ConversionStrategies.convStratMap.keys():
        raise ValueError("object unit must be one of ", ''.join(ConversionStrategies.convStratMap.keys()))
    if dest not in ConversionStrategies.convStratMap.keys():
        raise ValueError("conversion unit must be one of ", ''.join(ConversionStrategies.convStratMap.keys()))
    lu = LengthUnitImpl(float(length), unit)
    result = lu.convert(dest)
    return result

def main():
    length = sys.argv[1]
    unit = sys.argv[2]
    dest = sys.argv[3]
    result = convert(length, unit, dest)
    print(result)
    
if __name__ == '__main__':
    main()