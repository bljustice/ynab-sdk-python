import os
import unittest

class TestCommon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.personal_token = os.environ['YNAB_PERSONAL_TOKEN']
