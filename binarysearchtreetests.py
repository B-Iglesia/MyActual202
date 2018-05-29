from binarytreevis import *
import unittest

class Asg3Tests(unittest.TestCase):
    def test_binsearchtree_constructor1(self):
        bt1 = BinarySearchTree( contents=[0, 1, 2, 5, 90, -1] )
        bt2 = BinarySearchTree( contents=[0, 1, 2, 5, 90, -1] ) 
        
        self.assertListEqual( bt1.inorder(), bt2.inorder() )
        self.assertListEqual( bt1.preorder(), bt2.preorder() )
        self.assertListEqual( bt1.postorder(), bt2.postorder() )
        self.assertListEqual( bt1.levelorder(), bt2.levelorder() )
    def test_binsearchtree_constructor2(self):
        bt1 = BinarySearchTree( contents = [10, 7, 13, 4, 8,7.5,12, 14,2,5,15, 16])
        bt2 = BinarySearchTree( contents = [10, 7, 13, 4, 8,7.5,12, 14,2,5,15, 16] ) 
        
        self.assertListEqual( bt1.inorder(), bt2.inorder() )
        self.assertListEqual( bt1.preorder(), bt2.preorder() )
        self.assertListEqual( bt1.postorder(), bt2.postorder() )
        self.assertListEqual( bt1.levelorder(), bt2.levelorder() )     
    def test_binsearchtree_constructor3(self):
        bt1 = BinarySearchTree( contents = [10, 4, 8,7.5,12, 14,2,5,15, 16])
        bt2 = BinarySearchTree( contents = [10, 4, 8,7.5,12, 14,2,5,15, 16] ) 
        
        self.assertListEqual( bt1.inorder(), bt2.inorder() )
        self.assertListEqual( bt1.preorder(), bt2.preorder() )
        self.assertListEqual( bt1.postorder(), bt2.postorder() )
        self.assertListEqual( bt1.levelorder(), bt2.levelorder() )    
    def test_binsearchtree_constructor3(self):
        bt1 = BinarySearchTree( contents = [10, 4, 8, 14,2,5,15, 16])
        bt2 = BinarySearchTree( contents = [10, 4, 8, 14,2,5,15, 16] ) 
        
        self.assertListEqual( bt1.inorder(), bt2.inorder() )
        self.assertListEqual( bt1.preorder(), bt2.preorder() )
        self.assertListEqual( bt1.postorder(), bt2.postorder() )
        self.assertListEqual( bt1.levelorder(), bt2.levelorder() )          

    def test_binsearchtree_inorder1(self):
        bt = BinarySearchTree(contents=[0, -1, 1]) 
        self.assertListEqual(bt.inorder(), [-1, 0, 1]) 
    def test_binsearchtree_inorder2(self):
        bt = BinarySearchTree(contents = [2, 4, 5, 7, 7.5, 8, 10, 12, 13, 14, 15, 16]) 
        self.assertListEqual(bt.inorder(), [2, 4, 5, 7, 7.5, 8, 10, 12, 13, 14, 15, 16])      
    def test_binsearchtree_inorder3(self):
        bt = BinarySearchTree(contents=[5,4,3,2,1]) 
        self.assertListEqual(bt.inorder(), [1,2,3,4,5])          
    def test_binsearchtree_inorder4(self):
        bt = BinarySearchTree(contents = [10, 7, 13, 4, 8,7.5,12, 14,2,5,15 ]) 
        self.assertListEqual(bt.inorder(), [2, 4, 5, 7, 7.5, 8, 10, 12, 13, 14, 15])     
    def test_binsearchtree_preorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1] )
        self.assertListEqual( [2, 0, 1], bt.preorder() )
    def test_binsearchtree_preorder2(self):
        bt = BinarySearchTree( contents = [10, 7, 4, 2, 5, 8, 7.5, 13, 12, 14, 15, 16]  )
        self.assertListEqual( [10, 7, 4, 2, 5, 8, 7.5, 13, 12, 14, 15, 16] , bt.preorder() )    
    def test_binsearchtree_preorder3(self):
        bt = BinarySearchTree( contents = [5,4,6,2,7]  )
        self.assertListEqual( [5,4,2,6,7], bt.preorder() )       
    def test_binsearchtree_preorder4(self):
        bt = BinarySearchTree( contents = [5,4,6,1,7]  )
        self.assertListEqual( [5,4,1,6,7], bt.preorder() )         
    
    def test_binsearchtree_postorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1] )
        self.assertListEqual( [1, 0, 2], bt.postorder() ) 
    def test_binsearchtree_postorder2(self):
        bt = BinarySearchTree( contents=[5, 2, 4, 7.5, 8, 7, 12, 16, 15, 14, 13, 10] )
        self.assertListEqual( [4, 2, 7, 10, 13, 14, 15, 16, 12, 8, 7.5, 5], bt.postorder() )    
    def test_binsearchtree_postorder3(self):
        bt = BinarySearchTree( contents=[5,4,6,1,7] )
        self.assertListEqual( [1,4,7,6,5], bt.postorder() )         
        
    def test_binsearchtree_levelorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1, 6, 10] ) 
        self.assertListEqual( [2, 0, 6, 1, 10], bt.levelorder() ) 
    def test_binsearchtree_levelorder2(self):
        bt = BinarySearchTree( contents=[ 1, 6, 10] ) 
        self.assertListEqual( [  1,6, 10], bt.levelorder() )      
    def test_binsearchtree_levelorder3(self):
        bt = BinarySearchTree( contents=[10, 7, 13, 4, 8,7.5,12, 14,2,5,15, 16]) 
        self.assertListEqual( [10, 7, 13, 4, 8, 12, 14, 2, 5, 7.5, 15, 16] , bt.levelorder() )        
    def test_binsearchtree_levelorde4(self):
        bt = BinarySearchTree( contents=[4,3,5,1,6]) 
        self.assertListEqual( [4,3,5,1,6] , bt.levelorder() )           
        
    def test_binsearchtree_insert1(self):
        bt = BinarySearchTree() 
        bt.insert(0); bt.insert(-1); bt.insert(1)
        self.assertListEqual(bt.inorder(), [-1, 0, 1])    
    def test_binsearchtree_insert2(self):
        bt = BinarySearchTree() 
        bt.insert(4); bt.insert(-3); bt.insert(2); bt.insert(16); bt.insert(11)
        self.assertListEqual(bt.inorder(), [-3, 2, 4, 11, 16])
    def test_binsearchtree_insert3(self):
        bt = BinarySearchTree() 
        bt.insert(5); bt.insert(13); bt.insert(14); bt.insert(10); bt.insert(48)
        self.assertListEqual(bt.inorder(), [5, 10 , 13, 14, 48])  
    def test_binsearchtree_insert4(self):
        bt = BinarySearchTree() 
        bt.insert(2); bt.insert(5); bt.insert(6); bt.insert(4); bt.insert(3);bt.insert(1)
        self.assertListEqual(bt.inorder(), [1,2,3,4,5,6])         
        
    def test_binsearchtree_delete1(self):
        bt = BinarySearchTree(contents=[0, 1, 2]) 
        bt.delete(0)
        self.assertListEqual(bt.inorder(), [1, 2])
           
    def test_binsearchtree_delete2(self):
        bt = BinarySearchTree(contents=[0, 1, 2,-.05]) 
        bt.delete(1)
        self.assertListEqual(bt.inorder(), [-.05, 0, 2])    
    def test_binsearchtree_delete3(self):
        bt = BinarySearchTree(contents=[0, -100,1,-500,]) 
        bt.delete(0)
        self.assertListEqual(bt.inorder(), [-500,-100,1])   
        
                                 
    def test_binsearchtree_contains1(self):
        bt = BinarySearchTree(contents=[0, 1, 2]) 
        self.assertTrue(0 in bt)    
        bt.delete(0)
        self.assertFalse(0 in bt)
    def test_binsearchtree_contains2(self):
        bt = BinarySearchTree(contents=[0,-.5 ,1, 2]) 
        self.assertTrue(0 in bt)    
        bt.delete(0)
        self.assertFalse(0 in bt)        
    def test_binsearchtree_contains3(self):
        bt = BinarySearchTree(contents=[0,-.5 ,1, 2]) 
        self.assertTrue(1 in bt)    
        bt.delete(1)
        self.assertFalse(1 in bt) 
    def test_binsearchtree_contains4(self):
        bt = BinarySearchTree(contents=[0,-.5 ,1, 2]) 
        self.assertTrue(2 in bt)    
        bt.delete(2)
        self.assertFalse(2 in bt)         
    
    def test_largest1(self):
        bt = BinarySearchTree(contents=[10,9,8,11])
        self.assertEqual(bt.largestval().val, 11)
    def test_largest2(self):
        bt = BinarySearchTree(contents=[0])
        self.assertEqual(bt.largestval().val, 0)
    def test_largest3(self):
        bt = BinarySearchTree(contents=[9,10,11,2,4,6,7,5,66])
        self.assertEqual(bt.largestval().val, 66)   
    def test_largest4(self):
        bt = BinarySearchTree(contents=[9,10,5,4])
        self.assertEqual(bt.largestval().val, 10)    
    def test_finder(self):
        bt = BinarySearchTree(contents=[9,10,5,4])
        self.assertEqual(bt.find(4).val, 4)
if __name__ == '__main__':
    unittest.main()
