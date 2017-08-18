import ast
import os
import unittest

import harreplay

BASE_DIR = os.path.dirname(__file__)

TEST_DATA_DIR = os.path.join(BASE_DIR, 'test_data')

class TestStringMethods(unittest.TestCase):

    def test1(self):
        for fn in os.listdir(TEST_DATA_DIR):
            har_path = os.path.join(TEST_DATA_DIR, fn)
            har_fobj = open(har_path, 'rb')
            compile(
                harreplay.fobj_to_pystring(har_fobj),
                '<string>',
                'exec'
            )
        
