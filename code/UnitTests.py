'''
File Name: UnitTest.py
Description: Contains unit tests to help debug various functions.
Author: Bevan Jones
Copyright Notice:
This file is property of the University of Cape Town
You may download or copy this file for use in your own program.
You may NOT download or copy this file to another site.
You may NOT download or copy this file for publication or sale.
This file is intended for teaching purposes.
'''

import unittest
import numpy as np
import MeshGenerator as mg
import Discretisation as dc
import ErrorAnalysis as ea

class TestMeshGenerator(unittest.TestCase):

    def test_GenerateMesh2DMesh_2DCoordinates(self):
        """
        Tests that nodal co-ordinates have been correctly computed.
        """
        numberofNodesX = 3
        numberofNodesY = 5
        nodeTable = mg.GenerateMesh2DMesh(numberofNodesX, numberofNodesY)
        self.assertItemsEqual(nodeTable.Coordinate[0][0], [0.0, 0.0])
        self.assertItemsEqual(nodeTable.Coordinate[1][0], [0.5, 0.0])
        self.assertItemsEqual(nodeTable.Coordinate[2][0], [1.0, 0.0])

        self.assertItemsEqual(nodeTable.Coordinate[0][1], [0.0, 0.25])
        self.assertItemsEqual(nodeTable.Coordinate[1][1], [0.5, 0.25])
        self.assertItemsEqual(nodeTable.Coordinate[2][1], [1.0, 0.25])

        self.assertItemsEqual(nodeTable.Coordinate[0][2], [0.0, 0.5])
        self.assertItemsEqual(nodeTable.Coordinate[1][2], [0.5, 0.5])
        self.assertItemsEqual(nodeTable.Coordinate[2][2], [1.0, 0.5])

        self.assertItemsEqual(nodeTable.Coordinate[0][3], [0.0, 0.75])
        self.assertItemsEqual(nodeTable.Coordinate[1][3], [0.5, 0.75])
        self.assertItemsEqual(nodeTable.Coordinate[2][3], [1.0, 0.75])

        self.assertItemsEqual(nodeTable.Coordinate[0][4], [0.0, 1.0])
        self.assertItemsEqual(nodeTable.Coordinate[1][4], [0.5, 1.0])
        self.assertItemsEqual(nodeTable.Coordinate[2][4], [1.0, 1.0])

    def test_GenerateMesh2DMesh_CellSize(self):
        """
        Tests that nodal cell sizes, in each direction have been correctly computed.
        """
        numberofNodesX = 3
        numberofNodesY = 5
        nodeTable = mg.GenerateMesh2DMesh(numberofNodesX, numberofNodesY)
        self.assertItemsEqual(nodeTable.CellSize[0][0], [0.25, 0.125])
        self.assertItemsEqual(nodeTable.CellSize[1][0], [0.5, 0.125])
        self.assertItemsEqual(nodeTable.CellSize[2][0], [0.25, 0.125])

        self.assertItemsEqual(nodeTable.CellSize[0][1], [0.25, 0.25])
        self.assertItemsEqual(nodeTable.CellSize[1][1], [0.5, 0.25])
        self.assertItemsEqual(nodeTable.CellSize[2][1], [0.25, 0.25])

        self.assertItemsEqual(nodeTable.CellSize[0][2], [0.25, 0.25])
        self.assertItemsEqual(nodeTable.CellSize[1][2], [0.5, 0.25])
        self.assertItemsEqual(nodeTable.CellSize[2][2], [0.25, 0.25])

        self.assertItemsEqual(nodeTable.CellSize[0][3], [0.25, 0.25])
        self.assertItemsEqual(nodeTable.CellSize[1][3], [0.5, 0.25])
        self.assertItemsEqual(nodeTable.CellSize[2][3], [0.25, 0.25])

        self.assertItemsEqual(nodeTable.CellSize[0][4], [0.25, 0.125])
        self.assertItemsEqual(nodeTable.CellSize[1][4], [0.5, 0.125])
        self.assertItemsEqual(nodeTable.CellSize[2][4], [0.25, 0.125])

    def test_GenerateMesh2DMesh_2DNodalVolumes(self):
        """
        Tests that nodal control volumes are have been correctly computed.
        """
        numberofNodesX = 3
        numberofNodesY = 5
        nodeTable = mg.GenerateMesh2DMesh(numberofNodesX, numberofNodesY)
        self.assertEqual(nodeTable.Volume[0][0], 0.03125)
        self.assertEqual(nodeTable.Volume[1][0], 0.0625)
        self.assertEqual(nodeTable.Volume[2][0], 0.03125)

        self.assertEqual(nodeTable.Volume[0][1], 0.0625)
        self.assertEqual(nodeTable.Volume[1][1], 0.125)
        self.assertEqual(nodeTable.Volume[2][1], 0.0625)

        self.assertEqual(nodeTable.Volume[0][2], 0.0625)
        self.assertEqual(nodeTable.Volume[1][2], 0.125)
        self.assertEqual(nodeTable.Volume[2][2], 0.0625)

        self.assertEqual(nodeTable.Volume[0][3], 0.0625)
        self.assertEqual(nodeTable.Volume[1][3], 0.125)
        self.assertEqual(nodeTable.Volume[2][3], 0.0625)

        self.assertEqual(nodeTable.Volume[0][4], 0.03125)
        self.assertEqual(nodeTable.Volume[1][4], 0.0625)
        self.assertEqual(nodeTable.Volume[2][4], 0.03125)

class TestDiscretisation(unittest.TestCase):

    def test_GetMatrixIndex(self):
        """
        Checks that the conversion from i,j co-ordinates gives the correct matrix index.
        """
        imeshRow = 5
        imeshColumn = 3
        numberNodesX = 10
        self.assertEqual(dc.GetMatrixIndex(imeshColumn, imeshRow, numberNodesX), 53)

        imeshRow = 10
        imeshColumn = 7
        numberNodesX = 10
        self.assertEqual(dc.GetMatrixIndex(imeshColumn, imeshRow, numberNodesX), 107)

        imeshRow = 5
        imeshColumn = 7
        numberNodesX = 42
        self.assertEqual(dc.GetMatrixIndex(imeshColumn, imeshRow, numberNodesX), 217)

        imeshRow = 0
        imeshColumn = 1
        numberNodesX = 25
        self.assertEqual(dc.GetMatrixIndex(imeshColumn, imeshRow, numberNodesX), 1)

        imeshRow = 1
        imeshColumn = 0
        numberNodesX = 8
        self.assertEqual(dc.GetMatrixIndex(imeshColumn, imeshRow, numberNodesX), 8)

    def test_Diffusion2DRow(self):
        """
        Checks that the row returns for the discretisation of the implicit diffusive term is correct.
        """
        meshSize = 3
        thermalConduct = 5
        nodeTable = mg.GenerateMesh2DMesh(meshSize, meshSize)
        deriRow = np.zeros(dtype=float, shape=(meshSize*meshSize, 1))
        deriRow[0] = 1.0
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 0), deriRow)
        deriRow[0] = 0.0
        deriRow[1] = 1.0
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 1), deriRow)
        deriRow[1] = 0.0
        deriRow[2] = 1.0
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 2), deriRow)
        deriRow[2] = 0.0
        deriRow[3] = 1.0
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 3), deriRow)
        generalRow = [0.0, 20.0, 0.0, 20.0, -80.0, 20.0, 0.0, 20.0, 0.0]
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 4), generalRow)
        deriRow[3] = 0.0
        deriRow[5] = 1.0
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 5), deriRow)
        deriRow[5] = 0.0
        deriRow[6] = 1.0
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 6), deriRow)
        deriRow[6] = 0.0
        deriRow[7] = 1.0
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 7), deriRow)
        deriRow[7] = 0.0
        deriRow[8] = 1.0
        self.assertItemsEqual(dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, 8), deriRow)

    def test_ComputeSource(self):
        """
        Tests that the source term is being correctly calculated.
        """
        meshSize = 4
        nodeTable = mg.GenerateMesh2DMesh(meshSize, meshSize)
        nodeCoordinate = nodeTable.Coordinate

        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 0), 0)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 1), 0)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 2), 0)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 3), 0)

        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 4), 0)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 5), 0.52674897119341568)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 6), -0.6584362139917691)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 7), 0)

        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 8), 0)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 9), -0.65843621399176921)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 10), -6.5843621399176948)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 11), 0)

        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 12), 0)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 13), 0)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 14), 0)
        self.assertAlmostEqual(dc.ComputeSource(nodeCoordinate, 15), 0)

class TestErrorAnalysis(unittest.TestCase):

    def test_AnalyicalSolution2D(self):
        """
        Checks that the analyical solution is being computed correctly.
        """
        meshSize = 4
        nodeTable = mg.GenerateMesh2DMesh(meshSize, meshSize)
        nodeCoordinate = nodeTable.Coordinate

        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[0][0]), 0)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[1][0]), 0)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[2][0]), 0)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[3][0]), 0)

        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[0][1]), 0)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[1][1]), -0.009754610577655843)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[2][1]), -0.024386526444139613)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[3][1]), 0)

        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[0][2]), 0)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[1][2]), -0.024386526444139613)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[2][2]), -0.060966316110349042)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[3][2]), 0)

        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[0][3]), 0)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[1][3]), 0)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[2][3]), 0)
        self.assertAlmostEqual(ea.AnalyicalSolution2D(nodeCoordinate[3][3]), 0)

    def test_ComputeAbsoluteError(self):
        """
        Checks that the absolute error is computed correctly.
        """
        self.assertEqual(ea.ComputeAbsoluteError(10.0, 5.0), 5.0)
        self.assertEqual(ea.ComputeAbsoluteError(-5.0, 5.0), 10.0)

    def test_ComputeErrorL2Norm(self):
        """
        Checks the the L2Norm is being computed
        """
        MeshError = np.array([1.0, 1.0e-4])
        MeshSize = np.array([10, 100])
        self.assertAlmostEqual(ea.ComputeErrorL2Norm(MeshError, MeshSize), 4.0)
        MeshError = np.array([1.0, 1.0e-5])
        MeshSize = np.array([10, 100])
        self.assertAlmostEqual(ea.ComputeErrorL2Norm(MeshError, MeshSize), 5.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)

