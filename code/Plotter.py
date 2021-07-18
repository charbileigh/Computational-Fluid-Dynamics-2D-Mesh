'''
File Name: Plotter.py
Description: PostProcessor Plotting tool
Author: Bevan Jones
Copyright Notice:
This file is property of the University of Cape Town
You may download or copy this file for use in your own program.
You may NOT download or copy this file to another site.
You may NOT download or copy this file for publication or sale.
This file is intended for teaching purposes.
'''

import numpy as np
from matplotlib import pyplot as plt

class Plotter:
    def __init__(self, windowTitle, mrow, mcolu, mplot):
        """
        Constructor of the post processing grpah plotter.
        :param windowTitle: Name of the window to be created
        :param mrow: Number of rows in the graphing window
        :param mcolu: Number of columns in the graphing window
        :param mplot: The number of plots in the window.
        """

        # Set up basic info
        self.mRow = mrow
        self.mColu = mcolu
        self.mPlot = mplot

        # Set up the window, allocate the sub plots.
        plt.ion()
        plt.show(block=True)
        self.GraphWind = plt.figure()
        self.GraphWind.subplots_adjust(left=0.1, bottom=0.05, top=0.85, wspace=0.2, hspace=0.5)
        self.GraphWind.suptitle(windowTitle)

        # Initialise all sub arrays
        self.SubPlot = []
        self.SubPlotTitle = []
        self.SubPlotXLabel = []
        self.SubPlotYLabel = []
        self.isSubPlotLege = []
        self.isSubPlotLege = []

        # 1D Specific Plot Data
        self.SubPlotYScale = []
        self.SubPlotYMarker = []

        # 2D data
        self.mNodeX = []
        self.mNodeY = []
        self.ColorBar = []

        #plt.get_current_fig_manager().resize(*plt.get_current_fig_manager().window.maxsize())

    def Add1DPlot(self, iplot, title, Xlable, Ylabel, scale, dataPointMarkers, isplotLegend):
        """
        Add a clasical plot/graph to the window
        :param iplot: The number of this plot, when adding data to this graph reference it using this graph.
        :param title: The name of this graph
        :param Xlable: The x-axis label
        :param Ylabel: The y-axis label
        :param scale: Either leave blank or set to "log" for a log scale (Affects y axis only.)
        :param dataPointMarkers: What type of data point styling. Use '-' for a line, '-x' for x data points connected via lines. See https://matplotlib.org/api/markers_api.html
        :param isplotLegend: Must this graph have a legend. Useful when plotting more than one graph on the axis.
        :return: void
        """

        if iplot <= 0:
            print("Critical Error: " + str(iplot) + " must be greater than 0.")
            exit(1)
        elif iplot > self.mPlot:
            print("Critical Error: " + str(iplot) + " must be less than " + str(self.mPlot + 1) + ".")
            exit(1)
        else:
            self.SubPlot.append(self.GraphWind.add_subplot(self.mRow, self.mColu, iplot))
            self.SubPlotTitle.append(title)
            self.SubPlotXLabel.append(Xlable)
            self.SubPlotYLabel.append(Ylabel)
            if not scale == "" and not scale == "log":
                print("Critical Error: Scale must either be left empty or set to 'log'. ")
                exit(1)
            self.SubPlotYScale.append(scale)
            self.SubPlotYMarker.append(dataPointMarkers)
            self.isSubPlotLege.append(isplotLegend)
            print("Plot " + str(title) + " created successfully.")

            # add dummy stuff
            self.mNodeX.append("")
            self.mNodeY.append("")
            self.ColorBar.append("")

    def Add2DPlot(self, iplot, title, Xlable, Ylabel, mnodeX, mnodeY, isplotLegend):
        """""
        Add a 2D colour contour plot to the window
        :param iplot: The number of this plot, when adding data to this graph reference it using this graph.
        :param title: The name of this graph
        :param Xlable: The x-axis label (probably best to use x co-ordinate)
        :param Ylabel: The y-axis label (probably best to use y co-ordinate)
        :param mnodeX: Number of nodes in X
        :param mnodeY: Number of nodes in y
        :param isplotLegend: Must the colour bar be added, recommended true
        :return: void
        """

        if iplot <= 0:
            print("Critical Error: " + str(iplot) + " must be greater than 0.")
            exit(1)
        elif iplot > self.mPlot:
            print("Critical Error: " + str(iplot) + " must be less than " + str(self.mPlot + 1) + ".")
            exit(1)
        else:
            self.SubPlot.append(self.GraphWind.add_subplot(self.mRow, self.mColu, iplot))
            self.SubPlotTitle.append(title)
            self.SubPlotXLabel.append(Xlable)
            self.SubPlotYLabel.append(Ylabel)
            self.mNodeX.append(mnodeX)
            self.mNodeY.append(mnodeY)
            self.isSubPlotLege.append(isplotLegend)
            print("Plot " + str(title) + " created successfully.")
            self.ColorBar.append("")

            # add dummy stuff
            self.SubPlotYScale.append("")
            self.SubPlotYMarker.append("")

    def Update1DPlotData(self, iplot, dataX, dataY, label):
        """
        Update the data for a 1D plot/graph
        :param iplot: The graph number to be updated
        :param dataX: The data for the x-axis
        :param dataY: The data for the y-axis - if there is more than one must be of the form [[y1], [y2], [y3], etc]
        :param label: The label for the legend. If there are multiple plots, this must be of the form [["l1"],["l2"],["l3"]].
        :return: void
        """

        if not (iplot > 0 and iplot <= self.mPlot):
            print("Critical Error: " + str(iplot) + " does not exist.")
            exit(1)
        else:
            # Update the sub plot
            iplot = iplot - 1
            self.SubPlot[iplot].clear()
            self.SubPlot[iplot].ticklabel_format(style='sci', scilimits=(0, 0), axis='y')
            self.SubPlot[iplot].set_title(self.SubPlotTitle[iplot])
            self.SubPlot[iplot].set_xlabel(self.SubPlotXLabel[iplot])
            self.SubPlot[iplot].set_ylabel(self.SubPlotYLabel[iplot])
            if self.SubPlotYScale[iplot] == 'log':
                 self.SubPlot[iplot].set_yscale('log')


            # If the y data is just a single list then plot straight.
            subPlotLabel = []
            if len(label) <= 1:
                subPlotLabel.append(self.SubPlot[iplot].plot(dataX, dataY, "k" + str(self.SubPlotYMarker[0]), label=label))
                if self.isSubPlotLege[iplot]:
                    handles, labels = self.SubPlot[iplot].get_legend_handles_labels()
                    self.SubPlot[iplot].legend(handles[::-1], labels[::-1])
            else:
                for igraph in range(0, len(label)):
                    colours = ["k", "b", "r", "g", "c"]
                    subPlotLabel.append(self.SubPlot[iplot].plot(dataX, dataY[igraph], colours[igraph] + str(self.SubPlotYMarker[igraph]), label=label[igraph]))
                    if self.isSubPlotLege[iplot]:
                        handles, labels = self.SubPlot[iplot].get_legend_handles_labels()
                        self.SubPlot[iplot].legend(handles[::-1], labels[::-1])

            self.SubPlot[iplot].grid()

    def Update2DPlotData(self, iplot, phi, variableName):
        """
        Add a 2D colour contour plot to the window
        :param iplot: The graph number to be updated
        :param phi: The value of the variable. phi is assumed to be [phi(0,0), phi(1,0), .., phi(mnodeX - 1,0), phi(mnodeX,0), .. phi(2*mnodeX - 1,0), ...]
        :param variableName: The name of the variable you are plotting, will be used on the color bar.
        :return: void
        """
        if not (iplot > 0 and iplot <= self.mPlot):
            print("Critical Error: " + str(iplot) + " does not exist.")
            exit(1)
        else:
            iplot = iplot - 1
            coorX = np.linspace(0.0, 1.0, self.mNodeX[iplot])
            coorY = np.linspace(0.0, 1.0, self.mNodeY[iplot])
            phiNew = []

            # Create a 2D array for scalar field
            inode = 0
            for iy in range(self.mNodeY[iplot]):
                phiRow = []
                for ix in range(self.mNodeX[iplot]):
                    phiRow.append(phi[ix][iy][0])
                    inode = inode + 1
                phiNew.append(phiRow)

            # Set up points for plotting
            self.SubPlot[iplot].clear()
            for i in self.SubPlot[iplot].collections[:]:
                self.SubPlot[iplot].collections.remove(i)
            X, Y = np.meshgrid(coorX, coorY)

            self.SubPlot[iplot].pcolormesh(X, Y, phiNew, shading = 'gouraud')
            self.SubPlot[iplot].set_xlabel("x co-ordinate")
            self.SubPlot[iplot].set_ylabel("y co-ordinate")

            # On first visit set up the color bar, other wise just find new max and min.
            if self.ColorBar[iplot] == "":
                self.ColorBar[iplot] = self.GraphWind.colorbar((self.SubPlot[iplot].pcolormesh(X, Y, phiNew, shading = 'gouraud')), ax=self.SubPlot[iplot])
            else:
                self.ColorBar[iplot].set_clim(vmax=np.max(phi[:]), vmin=np.min(phi[:]))
                self.ColorBar[iplot].draw_all()
            self.ColorBar[iplot].set_label(variableName)
            self.SubPlot[iplot].set_title(self.SubPlotTitle[iplot] + '\n')

            # Add grid lines if requested
            self.SubPlot[iplot].grid(True, which='minor', axis='both', linestyle='-', color='k')
            self.SubPlot[iplot].set_xticks(coorX, minor=True)
            self.SubPlot[iplot].set_yticks(coorY, minor=True)
            self.SubPlot[iplot].set_xlim(coorX[0], coorX[len(coorX) - 1])
            self.SubPlot[iplot].set_ylim(coorY[0], coorY[len(coorY) - 1])

    def Plot(self, ainteractive):
        """
        Actually update the plotting window
        :param asleep: number of seconds to sleep for.
        :return: void
        """
        # if asleep != 0:
        #     plt.waitforbuttonpress(timeout = 0)

        self.GraphWind.canvas.draw()
        plt.show(block=ainteractive)

