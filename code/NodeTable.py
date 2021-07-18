'''
File Name: NodeTable.py
Description: Class object for all mesh data at each node.
Author: Bevan Jones
Copyright Notice:
This file is property of the University of Cape Town
You may download or copy this file for use in your own program.
You may NOT download or copy this file to another site.
You may NOT download or copy this file for publication or sale.
This file is intended for teaching purposes.
'''

import numpy as np

class NodeTable:

    def Diffusion2D(self, numberofNodesX, numberofNodesY):
        """
        Initialises a node with various nodal properties.
        :param numberofNodesX: Number of nodes
        :param numberofNodesY: dimension of simulation
        """

        # General attributes of node
        self.Coordinate = np.zeros(dtype=float, shape=(numberofNodesX, numberofNodesY, 2))
        self.CellSize = np.zeros(dtype=float, shape=(numberofNodesX, numberofNodesY, 2))
        self.Volume = np.zeros(dtype=float, shape=(numberofNodesX, numberofNodesY, 1))

        # Flow at n+1
        self.TemperatureNP1 = np.zeros(dtype=float, shape=(numberofNodesX, numberofNodesY, 1))

        # Error analysis
        self.AbsoluteError = np.zeros(dtype=float, shape=(numberofNodesX, numberofNodesY, 1))
        self.AnalyticalSolution = np.zeros(dtype=float, shape=(numberofNodesX, numberofNodesY, 1))

