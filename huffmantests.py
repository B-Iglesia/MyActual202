
from priorityqueue import *
from huffman import *

import unittest

class Asg4(unittest.TestCase):
   def test_priorityqueue_1(self):
      pq = PriorityQueue()
      pq.enqueue('a', 0)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('z', 100)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZ', -1)
      self.assertEqual(pq.front(), 'z')         
        
   def test_huffman_1(self):
      sent = 'aaaaggccttt'; codes = dict(); root = huffman(sent)

      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)  

      self.assertDictEqual(codes, {'a': '0', 'g': '111', 'c': '110', 't': '10'})
        
if __name__ == '__main__':  
   unittest.main()
