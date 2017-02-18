# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:43:41 2017

@author: jadotis
"""
import numpy as np
import random as rand
import math
import queue as Q

def graphTypeOne(n):
    '''
    Makes a graph where the edge weights are chosen
    uniformly between [0,1]
    '''
    Matrix = np.ones(shape = (n,n))
    for i in range(0,n-1):
        for j in range(i+1,n):
            Matrix[i][j] = rand.uniform(0,1)
            Matrix[j][i] = Matrix[i][j]
            
    return Matrix
    
def graphTypeTwo(n):
    '''
    Makes a graph where the weights are the Euclidean Distance
    from one node to another
    '''
    Nodes = [0]*n
    for i in range(n):
        Nodes[i] =  (rand.uniform(0,1), rand.uniform(0,1))
    
    #Constructs the Matrix
    Matrix = np.ones(shape = (n,n))
    for i in range(0,n-1):
        for j in range(i+1, n):
            Matrix[i][j] = math.sqrt(((Nodes[i][0] - Nodes[j][0])**2) + ((Nodes[i][1] - Nodes[j][1])**2))  
            Matrix[j][i] = Matrix[i][j]
    
    return Matrix   
    

def findMinIndex(array, n):
    minVal = 1.01
    minIndex = 0
    for i in range(len(array)):
        if array[i] < minVal and array[i] != 0:
            minVal = array[i]
            minIndex = i
          
    return minIndex


def prims(Matrix):
    global edges 
    edges = []
    length = len(Matrix[0])
    global unexploredNodes 
    unexploredNodes = [x for x in range(length)]
    global Sum 
    Sum = 0
    
    edges += [x for x in Matrix[:,0]]         #The first column
    del unexploredNodes[0]                    #removes Index 0
    Matrix[0,:] = [1.01]                      # Removes the First Row
    global minIndexEdges 
    minIndexEdges = findMinIndex(edges, length)
    Sum += edges[minIndexEdges]
    edges[minIndexEdges] = 1.01
    
    global colIndex 
    colIndex = minIndexEdges 
    
    while(len(unexploredNodes) != 0):
        edges += [x for x in Matrix[: , colIndex]]
        Matrix[colIndex, :] = [1.01]            #Syntax may need to change
        minIndexEdges = findMinIndex(edges, length)
        print("Sum: ", Sum)
        print("Min Edges: ", edges[minIndexEdges])
        Sum += edges[minIndexEdges]
        edges[minIndexEdges] = 1.01
        colIndex = minIndexEdges % length
        del unexploredNodes[0]
        
    return Sum
                  
        
x = graphTypeTwo(4)
print(x)      
prims(x)
    
     
        
