'''
File Name: Discretisation.py
Description: Functions related to discretising various terms in the governing equations.
Author: Bevan Jones
Copyright Notice:
This file is property of the University of Cape Town
You may download or copy this file for use in your own program.
You may NOT download or copy this file to another site.
You may NOT download or copy this file for publication or sale.
# This file is intended for teaching purposes.
'''

import numpy as np

def GetMatrixIndex(imeshColumn, imeshRow, numberNodesX):
    matrixIndex = 0
# code here...
    return matrixIndex

def Diffusion2DRow(nodeCoordinate, nodeCellSize, nodeVolume, viscocity, inode):

    numberNodesX = len(nodeCoordinate)
    numberNodesY = len(nodeCoordinate[0])
    diffusionRow = np.zeros(numberNodesX*numberNodesY)
# code here...
    return diffusionRow

def ComputeSource(nodeCoordinate, inode):

    source = 0.0
# code here...
    return source

