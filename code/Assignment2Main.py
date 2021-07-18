'''
File Name: Assignment2Main.py
Description: Root file to be run to answer problems set out in Assignment 2.
Author: Bevan Jones
Copyright Notice:
This file is property of the University of Cape Town
You may download or copy this file for use in your own program.
You may NOT download or copy this file to another site.
You may NOT download or copy this file for publication or sale.
This file is intended for teaching purposes.
'''

import numpy as np
import Plotter as pl
import MeshGenerator as mg
import Discretisation as dc
import ErrorAnalysis as ea


def ImplicitDiffusion(nodeTable, thermalConduct, isquiet):
    """
    Solves the heat diffusion equation implicitly.
    :param nodeTable: The node table for the mesh, with all co-ordinates, volumes and initial conditions computed.
    :param thermalConduct: The thermal conductivity of the fluid.
    :param isquiet: When true suppresses all write outs.
    :return: A node table with solved temperatures and error at each node.
    """
    # Determine number of nodes
    numberofNodesX = len(nodeTable.TemperatureNP1)
    numberofNodesY = len(nodeTable.TemperatureNP1[0])

    # Build Coefficient Matrix and Source Vectors
    SourceVector = np.zeros(dtype=float, shape=(numberofNodesX*numberofNodesY, 1))
    TemperatureVector = np.zeros(dtype=float, shape=(numberofNodesX*numberofNodesY, 1))
    DiffusionMatrix = np.zeros(dtype=float, shape=(numberofNodesX*numberofNodesY, numberofNodesX*numberofNodesY))

    for inode in range(numberofNodesX*numberofNodesY):
        DiffusionMatrix[:][inode] -= dc.Diffusion2DRow(nodeTable.Coordinate, nodeTable.CellSize, nodeTable.Volume, thermalConduct, inode)
        SourceVector[inode] = dc.ComputeSource(nodeTable.Coordinate, inode)

    # Solve implicit system Ax = b.
    # hint: use np linear algebra to solve the system, ie your line should look like TemperatureVector = ....
# code here...

    # Transfer solution to node table
    for irow in range(numberofNodesY):
        for icolu in range(numberofNodesX):
            nodeTable.TemperatureNP1[icolu][irow] = TemperatureVector[dc.GetMatrixIndex(icolu, irow, numberofNodesX)]

    # Perform error analysis
    for irow in range(numberofNodesY):
        for icolu in range(numberofNodesX):
            nodeTable.AnalyticalSolution[icolu][irow] = ea.AnalyicalSolution2D(nodeTable.Coordinate[icolu][irow])
            nodeTable.AbsoluteError[icolu][irow] = ea.ComputeAbsoluteError(nodeTable.TemperatureNP1[icolu][irow], nodeTable.AnalyticalSolution[icolu][irow])

    if not isquiet:
        print("\nSimulation completed")
    return nodeTable

'''
***************************************************************************************************************************************************************
Solve part C.
***************************************************************************************************************************************************************
'''
# Set up variables
NumberofNodesX = 2
NumberofNodesY = 2
ThermalConductivity = 4.0

#Set up plotter (customise plotter here)
plotter = pl.Plotter("Assignment 2 - Part C", 2, 2, 3)
plotter.Add2DPlot(1, "Temperature distrabution", "Co-ordiante", "Temperature", NumberofNodesX, NumberofNodesY, True)
plotter.Add2DPlot(2, "Temperature Analytical", "Co-ordiante", "Temperature", NumberofNodesX, NumberofNodesY, True)
plotter.Add2DPlot(3, "Error Absolute", "Co-ordiante", "Absolute Error", NumberofNodesX, NumberofNodesY, True)

nodeTable = mg.GenerateMesh2DMesh(NumberofNodesX, NumberofNodesY)
# code here...

# Report result and plot
print('Maximum error in the mesh is: ' + str(np.amax(nodeTable.AbsoluteError)))
plotter.Update2DPlotData(1, nodeTable.TemperatureNP1, "Temperature")
plotter.Update2DPlotData(2, nodeTable.AnalyticalSolution, "Analytical Temperature")
plotter.Update2DPlotData(3, nodeTable.AbsoluteError, "Absolute Error")
plotter.Plot(True)

'''
***************************************************************************************************************************************************************
Solve part D.
***************************************************************************************************************************************************************
'''
# Set up variables
ThermalConductivity = 4
MeshSize = []
MeshAbsoluteError = []

# code here...

# Set up plotter (customise plotter here)
plotter = pl.Plotter("Assignment 2 - Part D", 1, 1, 1)
plotter.Add1DPlot(1, "Temperature distrabution", "Co-ordiante", "Temperature", "", "-", False)

# code here...

# State l2Norm and plot mesh error vs size.
print('L2Norm is: ' + str(ea.ComputeErrorL2Norm(MeshAbsoluteError, MeshSize)))
plotter.Update1DPlotData(1, MeshSize, MeshAbsoluteError, "")
plotter.Plot(True)

'''
***************************************************************************************************************************************************************
Solve part E.
***************************************************************************************************************************************************************
'''
# Set up variables
NumberofNodesX = 10
NumberofNodesY = 10
ThermalConductivity = 4.0
ErrorTolerence = 1.0e-5
MaxAbsoluteError = ErrorTolerence * 10.0 # change to ErrorTolerence * 10.0 to actually solve the problem

# Set up plotter (customise plotter here)
plotter = pl.Plotter("Assignment 2 - Part E", 2, 2, 3)
plotter.Add2DPlot(1, "Temperature distrabution", "Co-ordiante", "Temperature", NumberofNodesX, NumberofNodesY, True)
plotter.Add2DPlot(2, "Temperature Analytical", "Co-ordiante", "Temperature", NumberofNodesX, NumberofNodesY, True)
plotter.Add2DPlot(3, "Error Absolute", "Co-ordiante", "Absolute Error", NumberofNodesX, NumberofNodesY, True)

while MaxAbsoluteError > ErrorTolerence:
# code here...
    print("Mesh Size: " + str(NumberofNodesX) + 'x' + str(NumberofNodesY) + '\tAbsolute error: ' + str(MaxAbsoluteError))

# code here...

# Re-run final solution to obtain the plots for the mesh with the least number of nodes.
nodeTable = mg.GenerateMesh2DMesh(NumberofNodesX, NumberofNodesY)
nodeTable = ImplicitDiffusion(nodeTable, ThermalConductivity, True)
plotter.Update2DPlotData(1, nodeTable.TemperatureNP1, "Temperature")
plotter.Update2DPlotData(2, nodeTable.AnalyticalSolution, "Analytical Temperature")
plotter.Update2DPlotData(3, nodeTable.AbsoluteError, "Absolute Error")
plotter.Plot(True)

