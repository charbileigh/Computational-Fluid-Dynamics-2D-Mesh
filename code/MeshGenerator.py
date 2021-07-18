'''
File Name: MeshGenerator.py
Description: Generates a mesh for each node table, ie populates geometric data for each node.
Author: Bevan Jones
Copyright Notice:
This file is property of the University of Cape Town
You may download or copy this file for use in your own program.
You may NOT download or copy this file to another site.
You may NOT download or copy this file for publication or sale.
This file is intended for teaching purposes.
'''

import numpy as np
import NodeTable as nt

def ComputeInitialNodeSpacing(numberofNodes, positveStretchFactor):

    deltaX = 1.0
# code here...
    return deltaX

def GenerateMesh2DMesh(numberofNodesX, numberofNodesY):

    newNodeTable = nt.NodeTable()
    newNodeTable.Diffusion2D(numberofNodesX, numberofNodesY)
# code here...
    return newNodeTable

