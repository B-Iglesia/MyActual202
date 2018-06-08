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
      pq.enqueue('a', 0)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('z', 100)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZ', -1)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZZZ', -10)
      self.assertEqual(pq.front(), 'z')
        
   def test_priorityqueue_3(self):
      pq = PriorityQueue()
      pq.enqueue('a', 0)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('z', 100)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZ', -1)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZZZ', 1000)
      self.assertNotEqual(pq.front(), 'ZZ')  
        
   def test_priorityqueue_4(self):
      pq = PriorityQueue()
      pq.enqueue('ZZ', -1)
      self.assertEqual(pq.front(), 'ZZ')
      pq.enqueue('ZZZZ', 1000)
      self.assertEqual(pq.dequeue(), 'ZZZZ')
        
   def test_priorityqueue_5(self):
      pq = PriorityQueue()
      pq.enqueue(list(), -1)
      self.assertEqual(pq.front(), [])
      pq.enqueue(tuple([1,2,3]), 1000); pq.enqueue('bbc', 1000)
      pq.enqueue(int('78'), 1000000)
      self.assertEqual(pq.dequeue(), 78)    
      
   def test_priorityqueue_6(self):
      pq = PriorityQueue()
      pq.enqueue('aa', 7)
      self.assertEqual(pq.front(), 'aa')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'aa')
      pq.enqueue('j', 100)
      self.assertEqual(pq.front(), 'j')
      pq.enqueue('f', 2222)
      self.assertEqual(pq.front(), 'f')
   
   def test_priorityqueue_7(self):
      pq = PriorityQueue()
      pq.enqueue('a', -1)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('c', 100)
      self.assertEqual(pq.front(), 'c')
      pq.enqueue('D', 6999)
      self.assertEqual(pq.front(), 'D')
      
      
   def test_priorityqueue_8(self):
      pq = PriorityQueue()
      pq.enqueue('a', 10)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('c', 100)
      self.assertEqual(pq.front(), 'c')
      pq.enqueue('D', 4)
      self.assertEqual(pq.front(), 'c')       
   
   def test_priorityqueue_9(self):
      pq = PriorityQueue()
      pq.enqueue('a', 10)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 15)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('c', 1)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('D', 4)
      self.assertEqual(pq.front(), 'b')         
     
   def test_code_helper1(self):
      self.assertEqual(code_helper(['L','L','L']), '000')
   def test_code_helper2(self):
      self.assertEqual(code_helper(['L','R','L']), '010')
   def test_code_helper3(self):
      self.assertEqual(code_helper(['L','R','L','R','L']), '01010')
   def test_code_helper4(self):
      self.assertEqual(code_helper(['L','L','L','L','L','R']), '000001')
   def test_code_helper5(self):
      self.assertEqual(code_helper(['R','R','R','R','R','R','R']), '1111111')
   def test_code_helper6(self):
      self.assertEqual(code_helper(['R','R','R','R','R','R','L']), '1111110')
   def test_code_helper7(self):
      self.assertEqual(code_helper(['R','R','R','R','R','L','R']), '1111101')
   def test_code_helper8(self):
      self.assertEqual(code_helper(['R','R','R','R','L','R','R']), '1111011')      
      
   def test_huffman_1(self):
      sent = 'aaaaggccttt'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)  
            
      self.assertDictEqual(codes, {'a': '0', 'g': '111', 'c': '110', 't': '10'})
     
   def test_huffman_2(self):
      sent = 'asdf;k;lkjasdfk dasiirFFDg'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)  
            
      self.assertDictEqual(codes, \
                             {'a': '001', 's': '100', 'd': '010', 'f': '1011', \
                              ';': '1101', 'k': '011', 'l': '11100', 'j': \
                              '11111', ' ': '11000', 'i': '000', 'r': '11101',\
                              'F': '1010', 'D': '11001', 'g': '11110'})
       
   def test_huffman_3(self):
      sent = 'asdf;k;lkjasdfk'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)  
            
      self.assertDictEqual(codes, {'a': '100', 's': '011', 'd': '101', \
                                      'f': '010', ';': '111', 'k': '00', \
                                      'l': '1101', 'j': '1100'})  
        
   def test_huffman_4(self):
      sent = 'testing this string'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)
       
      self.assertDictEqual(codes, {'t': '01', 'e': '10110', 's': '111', \
        'i': '110', 'n': '100', 'g': '001', ' ': '000', 'h': '10111', \
            'r': '1010'} )
                           
   def test_huffman_5(self):
      sent = 'StringTeessttt'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)
       
      self.assertDictEqual(codes, {'S': '0100', 't': '11', 'r': \
        '1001', 'i': '1011', 'n': '1000', 'g': '1010', 'T': '0101', \
            'e': '011', 's': '00'})
   def test_huffman_6(self):
      sent = 'test'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)
       
      self.assertDictEqual(codes, {'t': '1', 's': '01', 'e': '00'})
      
   def test_huffman_7(self):
      sent = 'juullkdeoo'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)
       
      self.assertDictEqual(codes, {'d': '010', 'e':'011','j':'000','k':'001','l':'110','o':'111','u':'10'})      
if __name__ == '__main__':  
   unittest.main()
      