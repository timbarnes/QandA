
import sys
import unittest

sys.path.append('..')

import quanda

class TestScanFunctions(unittest.TestCase):

    def setUp(self):
        pass


    def test_rate_answer1(self):
        self.assertEqual(quanda.rate_answer('New York, 1916', 'New York 1916'), 0)
        

    def test_rate_answer2(self):
        self.assertEqual(quanda.rate_answer('Break up the surface', 'Break up vertical surfaces'), 0)
        

    def test_rate_answer3(self):
        self.assertEqual(quanda.rate_answer("4'", "4'"), 1)
        

    def test_rate_answer4(self):
        self.assertEqual(quanda.rate_answer('no idea', 'Typically orient east-west to balance light and heat'), -1)
        
            
    def test_list_topics(self):
        self.assertEqual(quanda.list_topics('test.xlsx'),
                         [u'Circulation', u'Climate', u'Comfort', u'Costing',
                          u'Drainage', u'Foundations', u'Historical', u'Parking',
                          u'Retaining devices', u'Roads', u'Siting', u'Soil testing',
                          u'Soil types', u'Utilities', u'Zoning'])

        
if __name__ == '__main__':
    unittest.main()
