import numpy as np
import matplotlib.pyplot as plt
import time
from binarytree import heap 
class Node: 
    def __init__(self, name): 
        self.left = None
        self.right = None
        self.value = name
    
def InOrderTraversal(root): 
    if root:   
        InOrderTraversal(root.left) 
        print(root.value)
        InOrderTraversal(root.right) 
    
def PostOrderTraversal(root): 
    if root:   
        PostOrderTraversal(root.left) 
        PostOrderTraversal(root.right) 
        print(root.value)
  
def PreOrderTraversal(root): 
    if root:   
        print(root.value)
        PreOrderTraversal(root.left) 
        PreOrderTraversal(root.right) 

def Test():
	A=[];
	T=[];
	Cases=[];
	for i in range(1,101):
		root = heap(height=2)
		A.append(root)
		Cases.append(i)
	for i in A:
		start=time.time()
		InOrderTraversal(i)
		# PostOrderTraversal(i)
		# PreOrderTraversal(i)
		T.append(time.time()-start)
	plt.plot(Cases,T,"-o")
	plt.xlabel('List Cases')
	plt.ylabel('List Time')
	plt.title('BinaryTreeTraversals') 
	plt.show()
Test()


