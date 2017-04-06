'''
Created on Apr 6, 2017

@author: mtoback
'''
import unittest

from com.mtoback.luc.lengthUnitImpl import LengthUnitImpl
from com.mtoback.luc.units import Units
class CentimeterTests(unittest.TestCase):


    def testCMtoInches(self):
        lu1 = LengthUnitImpl(3.0,Units.CENTIMETERS)
        lu2 = lu1.convert(Units.INCHES)
        self.assertLessEqual(abs(lu2.length - 1.1811), 0.001)
        self.assertEqual(lu2.unit, Units.INCHES)
        self.assertTrue(lu1 == lu2)

    def testCMtoFeet(self):
        lu1 = LengthUnitImpl(3.0,Units.CENTIMETERS)
        lu2 = lu1.convert(Units.FEET)
        self.assertLessEqual(abs(lu2.length - 0.0984), 0.001)
        self.assertEqual(lu2.unit, Units.FEET)
        self.assertTrue(lu1 == lu2)
    
    def testCMtoMiles(self):
        lu1 = LengthUnitImpl(3.0,Units.CENTIMETERS)
        lu2 = lu1.convert(Units.MILES)
        self.assertLessEqual(abs(lu2.length - 18.64e-6), 1e-8)
        self.assertEqual(lu2.unit, Units.MILES)
        self.assertTrue(lu1 == lu2)

    def testCMtoCM(self):
        lu1 = LengthUnitImpl(3.0,Units.CENTIMETERS)
        lu2 = lu1.convert(Units.CENTIMETERS)
        self.assertLessEqual(abs(lu2.length - 3.0),0.001)
        self.assertEqual(lu2.unit, Units.CENTIMETERS)
        self.assertTrue(lu1 == lu2)

    def testCMtoMeters(self):
        lu1 = LengthUnitImpl(3.0,Units.CENTIMETERS)
        lu2 = lu1.convert(Units.METERS)
        self.assertLessEqual(abs(lu2.length - 0.03), 0.0001)
        self.assertEqual(lu2.unit, Units.METERS)
        self.assertTrue(lu1 == lu2)

    def testCMtoKilometers(self):
        lu1 = LengthUnitImpl(3.0,Units.CENTIMETERS)
        lu2 = lu1.convert(Units.KILOMETERS)
        self.assertLessEqual(abs(lu2.length - 3.0e-5), 1.0e-7)
        self.assertEqual(lu2.unit, Units.KILOMETERS)
        self.assertTrue(lu1 == lu2)


if __name__ == "__main__":
    #import syssys.argv = ['', 'Test.testConvertCMToCM']
    unittest.main()