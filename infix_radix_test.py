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
    def test_radix_2(self):
        unsortedlst = ['bubble', 'boots', 'alabama', 'arkansas', 'acorn', 'cantelope']
        sortedlst = radixsort( unsortedlst, len(unsortedlst) )        
        self.assertListEqual(sortedlst,  ['acorn', 'alabama', 'arkansas', 'boots', 'bubble', 'cantelope'] )   
    def test_radix_3(self):
        unsortedlst = ['zebra', 'yak', 'yellow', 'broa', 'north', 'south']
        sortedlst = radixsort( unsortedlst, len(unsortedlst) )        
        self.assertListEqual(sortedlst,  ['broa', 'north', 'south', 'yak', 'yellow', 'zebra'] )         
    def test_radix_4(self):
        unsortedlst = ['butter', 'better' , 'bitter', 'biter' , 'also', 'aliso', 'alonso' , 'alls' ]
        sortedlst = radixsort(unsortedlst,len(unsortedlst))
        self.assertListEqual(sortedlst, ['aliso', 'alls', 'alonso', 'also', 'better', 'biter', 'bitter', 'butter'])
    def test_radix_4(self):
        unsortedlst = ['elephant', 'elite', 'forest', 'foreign', 'matador', 'mater', 'natural', 'apple', 'also', 'burn']
        sortedlst = radixsort(unsortedlst,len(unsortedlst))
        self.assertListEqual(sortedlst, ['also', 'apple', 'burn', 'elephant', 'elite', 'foreign', 'forest', 'matador', 'mater', 'natural'])    
    def test_radix_5(self):
        unsortedlst = ['donut', 'delicious', 'keeper', 'cancer', 'killer', 'zebra', 'yo-yo', 'link', 'loops', 'more', 'oreo']
        sortedlst = radixsort(unsortedlst,len(unsortedlst))
        self.assertListEqual(sortedlst, ['cancer', 'delicious', 'donut', 'keeper', 'killer', 'link', 'loops', 'more', 'oreo', 'yo-yo', 'zebra'])      
if __name__ == '__main__':  
    unittest.main()
