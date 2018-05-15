from infix import *
from radix import *
import unittest

class Asg2Tests(unittest.TestCase):
    def test_infix_1(self):
        e = '( 1 + 2 ) * 2 * ( 2 + 1 )'
        val = eval_infix(e)        
        self.assertEqual(val, 18.0)
        
    def test_radix_1(self):
        unsortedlst = ['aaa', 'abc', 'aa', 'cc', 'cba', 'zzz']
        sortedlst = radixsort( unsortedlst, len(unsortedlst) )        
        self.assertListEqual(sortedlst,  ['aa', 'aaa', 'abc', 'cba', 'cc', 'zzz'] )  

if __name__ == '__main__':  
    unittest.main()
