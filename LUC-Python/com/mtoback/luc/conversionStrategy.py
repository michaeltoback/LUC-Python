'''
Created on Apr 6, 2017

@author: mtoback
'''

class ConversionStrategy(object):
    '''
    classdocs
    '''
    

    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    def convert(self, obj, dest):
        raise NotImplementedError