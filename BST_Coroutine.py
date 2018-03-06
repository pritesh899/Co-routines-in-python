class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

#Insertion of the nodes in Binary tree 
def insert(root,node):
    if root == None:
        root = node
    else:
        if root.val < node.val:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left == None:
                root.left = node
            else:
                insert(root.left, node)

#Printing a binary tree in inorder
def Print_InOrder(root):
    if root:
        Print_InOrder(root.left) 
        print "\t" (root.val)
        Print_InOrder(root.right)

#Transverse the tree in inorder 
def InOrder(root):
    if root:
        for val in InOrder(root.left):
            yield val
        yield root.val
        for val in InOrder(root.right):
            yield val

# Comapring the two trees using Co-routines
def Compare(Tree1,Tree2):
	#Print_Inorder(Tree1)
    co_routine_1 = InOrder(Tree1)
    co_routine_2 = InOrder(Tree2)
    T1 = 1
    T2 = 1
    Equal = True
 	
    while True:
    #    try:
            T1 = next(co_routine_1,None)
            #print(V1)
            T2 = next(co_routine_2,None)
           # print(V2)
            
            if (T1 is None and T2 is not None):
            	Equal = False
            	print "\t Empty Tree EMPTY = %s" %(T2)
            	print "\t Tree 1 is smaller than Tree 2"
                break
                
            if (T1 is not None and T2 is None):
            	Equal = False
            	print "\t Empty Tree %s = EMPTY" %(T1)
                print "\t Tree 2 is smaller than Tree 1"
                break
            	
            if (T1 is not None and T2 is not None):
            		if(T1 == T2):
                		print "\t Match found %s = %s" %(T1,T2)
                		Equal = True
          	    	else:
                		print "\t Match not found %s != %s" %(T1,T2)
               	    	Equal = False
            
            if (T1 is None and T2 is None):
            	break
                
          
#Insertion for 1st tree
Tree1 = Node("B")
insert(Tree1,Node("A"))
insert(Tree1,Node("D"))
insert(Tree1,Node("C"))
insert(Tree1,Node("E"))


#Insertion for 2nd tree
Tree2 = Node("D")
insert(Tree2,Node("B"))
insert(Tree2,Node("E"))
insert(Tree2,Node("A"))
insert(Tree2,Node("C"))
insert(Tree2,Node("F"))


#Insertion for 3th tree
Tree3 = Node("D")
insert(Tree3,Node("B"))
insert(Tree3,Node("E"))
insert(Tree3,Node("A"))
insert(Tree3,Node("C"))


#Insertion for 4th tree
Tree4 = Node("X")
insert(Tree4,Node("B"))
insert(Tree4,Node("A"))
insert(Tree4,Node("C"))
insert(Tree4,Node("Y"))


#Comparisons of the trees in different cases :
print("\n CASE 1 : When both tree are equal :")
Compare(Tree1,Tree3)
print("\n CASE 2 : When both tree are equal but do not match:")
Compare(Tree1,Tree4)
print("\n CASE 3 :  When both tree are not equal and first tree is the subset of second tree:")
Compare(Tree1,Tree2)
print("\n CASE 4 :  When both tree are not equal and second tree is the subset of frist tree:")
Compare(Tree2,Tree1)




