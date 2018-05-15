from infix import *
from radix import *
import unittest

class Asg2Tests(unittest.TestCase):
    def test_infix_1(self):
        e = '( 1 + 2 ) * 2 * ( 2 + 1 )'
        val = eval_infix(e)        
        self.assertEqual(val, 18.0)
    def test_infix_2(self):
        e = '( 6 + 5 ) * 4 - 9'
        val = eval_infix(e)        
        self.assertEqual(val, 35.0)
    def test_infix_3(self):
        e = ' 6 / 2 * 4'
        val = eval_infix(e)        
        self.assertEqual(val, 12.0)
    def test_infix_4(self):
        e = ' ( 6 + 2 ) * 4'
        val = eval_infix(e)        
        self.assertEqual(val, 32.0)        
    def test_infix_5(self):
        e = ' ( 6 - 2 ) * ( 4 + 3 ) / 2'
        val = eval_infix(e)        
        self.assertEqual(val, 14.0)          
        
    def test_radix_1(self):
        unsortedlst = ['aaa', 'abc', 'aa', 'cc', 'cba', 'zzz']
        sortedlst = radixsort( unsortedlst, len(unsortedlst) )        
        self.assertListEqual(sortedlst,  ['aa', 'aaa', 'abc', 'cba', 'cc', 'zzz'] )  

if __name__ == '__main__':  
    unittest.main()
