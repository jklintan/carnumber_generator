#!/usr/bin/env python                                                           
# -*- coding: latin-1 -*-                                                       
import os, sys

## Implementation of a binary tree in Python by Josefine Klintberg ##

#Implementation of a binary search tree, no repeated values allowed

class Node:
    def __init__(self, val, le=None, ri=None): #Constructor
        self.item = val 
        self.left = le
        self.right = ri

class binSearchTree():
    def __init__(self): #Constructor, create empty tree
        self.root = None

    def put(self, val): 
        newNode = Node(val)
        if self.root==None: #Base case, empty tree
            self.root = newNode
            return True 
        p = self.root #Set a value to the root
        while val != p.item: 
            if val < p.item: 
                if p.left == None: 
                    p.left = newNode
                    return True
                else: p = p.left 
            elif val > p.item:
                if p.right == None:
                    p.right = newNode
                    return True 
                else: p = p.right
        return False #Value was already in tree

    #Check if an item is in tree
    def exists(self, val):
        newNode = Node(val)
        if self.root == None:
            return False
        p = self.root
        while val != p.item:
            if val < p.item:
                if p.left == None:
                    return False
                else: p = p.left
            elif m > p.item:
                if p.right == None:
                    return False
                else: p = p.right
        return True

    #Check if tree is empty
    def isempty(self): 
        return self.root is None

    #Calculate the height of the tree
    def height(self): 
        def rheight(root):
            if root is None: #Base case, empty tree
                return 0
            else:
                return 1 + max(rheight(root.left), rheight(root.right))
        return rheight(self.root)
                
    #Recursive function to print out the tree, inorder
    def print(self, order):
        def rprint(root):
            if root is None: #Base case, empty tree
                return
            elif order == "inorder": 
                rprint(root.left)
                print(root.item)
                rprint(root.right)
            elif order == "postorder":
                rprint(root.left)
                rprint(root.right)
                print(root.item)
            elif order == "preorder":
                print(root.item)
                rprint(root.left)
                rprint(root.right)
            else:
                print("Not a valid order")
        return rprint(self.root)
    
