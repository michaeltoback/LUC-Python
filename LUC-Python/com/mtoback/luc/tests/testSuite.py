'''
Created on Apr 6, 2017

@author: mtoback
'''
import unittest
from com.mtoback.luc.tests.centimeterTests import CentimeterTests
from com.mtoback.luc.tests.cliTests import CLITests

class TestSuite(unittest.TestCase):
    def __init__(self):
        pass


if __name__ == "__main__":
    test_classes = [CLITests, CentimeterTests]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)