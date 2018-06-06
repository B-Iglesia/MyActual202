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
   
   def test_priorityqueue_2(self):
      pq = PriorityQueue()
      pq.enqueue('aa', 7)
      self.assertEqual(pq.front(), 'aa')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'aa')
      pq.enqueue('j', 100)
      self.assertEqual(pq.front(), 'j')
      pq.enqueue('f', 2222)
      self.assertEqual(pq.front(), 'f')
   
   def test_priorityqueue_3(self):
      pq = PriorityQueue()
      pq.enqueue('a', -1)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('c', 100)
      self.assertEqual(pq.front(), 'c')
      pq.enqueue('D', 6999)
      self.assertEqual(pq.front(), 'D')
      
      
   def test_priorityqueue_4(self):
      pq = PriorityQueue()
      pq.enqueue('a', 10)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('c', 100)
      self.assertEqual(pq.front(), 'c')
      pq.enqueue('D', 4)
      self.assertEqual(pq.front(), 'c')       
   
   def test_priorityqueue_5(self):
      pq = PriorityQueue()
      pq.enqueue('a', 10)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 15)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('c', 1)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('D', 4)
      self.assertEqual(pq.front(), 'b')         
              
   def test_huffman_1(self):
      sent = 'aaaaggccttt'; codes = dict(); root = huffman(sent)

      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)  

      self.assertDictEqual(codes, {'a': '0', 'g': '111', 'c': '110', 't': '10'})
        
if __name__ == '__main__':  
   unittest.main()
