
selector = input("Welcome! Please use the below instructions, \n 1 Generates root files, \n 2 reuturns the optimum cut and significances, \n 3 makes new root files for TMVA,\n"
                 " 4 runs generic TMVA analysis on High level variables, \n 5 Runs generic TMVA analysis on Low Level variables,\n 6 Runs TMVA High Level analysis for the mH = 200 geV across signal regions for mA"
                 "\n 7 runs TMVA Low Level analysis for mH = 200 across signal regions for mA, \n 8 Takes optimum significance cuts (found in the Mllbbplotterfiles) and returns Mllbb plots from TMVA \n "
                 "9 Rebins the files making them ready for Poisson Likelihood calculatons,\n 10 returns the limit plots from Poisson Likelihood for all 3 methods\n 100 performs all of the above")
initialnumberbins = 100
BinCollapse = 10
masses = [200,130]
rootnames = ["Window_130.root","Window200.root"]

if selector == 1 or selector == 100:
    from RootHistoMaker import *
    for i in range(len(masses)):
        print ("Working in Higgs Mass window " + str(masses[i]) + ' GeV')
        Maker(masses[i],selector,rootnames[i],initialnumberbins)

if selector == 2 or selector == 100:
    import SignificanceFinder
    SignificanceFinder
if selector == 3 or selector ==100:
    import RootFileMaker
    RootFileMaker

if selector == 4 or selector == 100:
    import TMVA_NN
    TMVA_NN
if selector == 5 or selector == 100:
    import TMVA_NN_LOWLEVEL
    TMVA_NN_LOWLEVEL
if selector == 6 or selector == 100:
    import TMVA_SIGNALS
    TMVA_SIGNALS
if selector == 7 or selector == 100:
    import TMVA_SIGNALS_LOWLEVEL
    TMVA_SIGNALS_LOWLEVEL
if selector == 8 or selector == 100:
    import MllbbPlotter
    import MllbbPlotterLOWLEVEL
    MllbbPlotter
    MllbbPlotterLOWLEVEL
if selector == 9 or selector == 100:
    from Rebinner import *
    Binner3(components200,names200,masses[0],BinCollapse)
    Binner3(components130,names130,masses[1],BinCollapse)
if selector == 10 or selector ==100:
    import TgraphLimits
    TgraphLimits


