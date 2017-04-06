'''
Created on Apr 6, 2017

@author: mtoback
'''
import unittest

from com.mtoback.luc.LUCMain import convert

class CLITests(unittest.TestCase):


    def testHappyPath1(self):
        result = convert("5", "cm", "cm")
        self.assertEqual(result.unit, "cm")
        self.assertEqual(result.length, 5)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()