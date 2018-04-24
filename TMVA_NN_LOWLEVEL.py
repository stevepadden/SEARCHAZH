import sys
import ROOT as R

def TMVANN (filenameSTRING,outputDOTrootSTRING,sigtreeSTRING,bkgtreeSTRING,variablesSTRING):
    from ROOT import TMVA
    file = R.TFile(filenameSTRING)          #importing the lowlevel_dataset
    signaltree = file.Get(sigtreeSTRING)    #setting signaltree
    backgroundtree = file.Get(bkgtreeSTRING) #setting backgroundtree)
    TMVA.Tools.Instance()

    NNfile = R.TFile(outputDOTrootSTRING,"recreate")      #Writing the root file required for the TMVA factory

    TMVAfactory = TMVA.Factory("TMVANN",NNfile,"V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification")
    TMVAfactory.SetVerbose(False)  #Setting extra info (verbose) to false

    lowlevel_dataset = TMVA.DataLoader("lowlevel_dataset")     #Instantiating a lowlevel_dataset
    lowlevel_dataset.AddSignalTree(signaltree,1.)     #adding signal
    lowlevel_dataset.AddBackgroundTree(backgroundtree ,1.) #adding background
    lowlevel_dataset.AddBackgroundTree(backgroundtree ,1.) #adding background

    #lowlevel_dataset.SetSignalWeightExpression(weights)
    #lowlevel_dataset.SetBackgroundWeightExpression(weights)

    for i in variablesSTRING:                #adding our training variables to the TMVA
        lowlevel_dataset.AddVariable(i)

    signalcut = R.TCut("")  #Variables are already cut
    backgroundcut = R.TCut("")
    lowlevel_dataset.PrepareTrainingAndTestTree(signalcut,backgroundcut,"nTrain_Signal= 0:nTrain_Background=0:Splitmode=Random:NormMode=NumEvents:!V")
    #using all signal and background points to train, random selection, normalised to summed event weights = number of events for each tree, no verbose

    #Booking some methods

    TMVAfactory.BookMethod(lowlevel_dataset,TMVA.Types.kMLP,"LowLevelNN_3layer25,20,10_100Epoch_tanhNeuron","H:!V:NeuronType=tanh:VarTransform=N:NCycles=100:HiddenLayers=25,20,10:TestRate=5")
    TMVAfactory.BookMethod(lowlevel_dataset,TMVA.Types.kMLP,"LowLevelNN_1layer18nodes_100Epoch_tanhNeuron","H:!V:NeuronType=tanh:VarTransform=N:NCycles=100:HiddenLayers=18:TestRate=5")
    TMVAfactory.BookMethod(lowlevel_dataset,TMVA.Types.kMLP,"LowLevelNN_3layer20,20,20_100Epoch_tanhNeuron","H:!V:NeuronType=tanh:VarTransform=N:Ncycles=100:HiddenLayers=20,20,20:TestRate=5")
    TMVAfactory.BookMethod(lowlevel_dataset,TMVA.Types.kMLP,"LowLevelNN_1layer30nodes_100Epoch_tanhNeuron","H:!V:NeuronType=tanh:VarTransform=N:NCycles=100:HiddenLayers=30:TestRate=5")



    TMVAfactory.TrainAllMethods()
    TMVAfactory.TestAllMethods()
    TMVAfactory.EvaluateAllMethods()
    NNfile.Close()
    print ('TMVA Low Level ran & made root file ' + outputDOTrootSTRING)

def TMVAReader (filenameSTRING,sigtreeSTRING,bkgtreeSTRING,variablesSTRING,varnames,varweightfiles,xmins,xmaxs,signalmllbb,backgroundmllbb):
    inputfile = R.TFile(filenameSTRING,"read")
    reader = R.TMVA.Reader()
    signalhists = []
    backgroundhists= []
    signalmllbb = []
    backgroundmllbb = []
    for varname,xmin,xmax in zip(varnames,xmins,xmaxs):
        signalhist = R.TH1F("SignalHist" + varname,"Signal"+varname,60,xmin,xmax )
        backgroundhist =  R.TH1F("BackgroundHist Hist" + "Background"+ varname,varname,60,xmin,xmax)
        signalhists.append(signalhist)
        backgroundhists.append(backgroundhist)
        signalmllbb.append(signalhist)
        backgroundmllbb.append(backgroundhist)

    sigtree = inputfile.Get(sigtreeSTRING)
    bkgtree = inputfile.Get(bkgtreeSTRING)

    from array import array
    branchdict = {}
    for i in variablesSTRING:
        branchdict[i] = array('f',[0.])
        reader.AddVariable(i,branchdict[i])
        sigtree.SetBranchAddress(i,branchdict[i])
        bkgtree.SetBranchAddress(i,branchdict[i])

    for name,file in zip(varnames,varweightfiles):
        reader.BookMVA(name,file)

    i = 0
    while sigtree.GetEntry(i):
        i += 1
        for  name,histo in zip(varnames,signalhists):
            classify = reader.EvaluateMVA(name)
            histo.Fill(classify)
    i = 0
    while bkgtree.GetEntry(i):
        i +=1
        for  name,histo in zip(varnames,backgroundhists):
            classify = reader.EvaluateMVA(name)
            histo.Fill(classify)

    for histosig,histobkg,name in zip(signalhists,backgroundhists,varnames):
        canvas = R.TCanvas()
        histosig.SetStats(1)
        ymax = None
        if  histosig.GetBinContent(histosig.GetMaximumBin()) > histobkg.GetBinContent(histobkg.GetMaximumBin()):
            ymax = histosig.GetBinContent(histosig.GetMaximumBin())
        else:
            ymax = histobkg.GetBinContent(histobkg.GetMaximumBin())

        histosig.GetYaxis().SetRangeUser(0,ymax*1.5)
        histosig.SetLineColor(R.kSpring-4)
        histosig.SetFillColor(R.kSpring-4)
        histosig.Draw("HIST")
        histobkg.Draw("HIST,same")
        histosig.Draw("Hist,same")
        R.gPad.RedrawAxis()
        canvas.Print(name+".png")













signaltree = '400'
weights = 'Weight'
backgroundtree = 'Background'
TrainingVariables = ['lep0m','lep0pt','lep0phi','lep0eta','bjet0m','bjet0pt','bjet0phi','bjet0eta','lep1m','lep1pt','lep1phi','lep1eta','bjet1m','bjet1pt','bjet1phi','bjet1eta']
outputfilename = 'TMVANNLowLevel.root'
inputfilename = 'Window200NEW.root'
signalmllbbtree = 'signal_'+signaltree
backgroundmllbbtree = 'Background'
varnames = ['ArtificialNeuralNetwork_3Layer25,20,10_300Epoch_tanhNeuron','ArtificialNeuralNetwork_1layer18nodes_300Epoch_tanhNeuron','ArtificialNeuralNetwork_3Layer10nodes_300Epoch_tanhNeuron','ArtificialNeuralNetwork_1layer30nodes_300Epoch_tanhNeuron']
varlocation = 'lowlevel_dataset/weights/'
varweightfiles =   [varlocation+'TMVANN_LowLevelNN_3layer25,20,10_300Epoch_tanhNeuron.weights.xml',varlocation+'TMVANN_LowLevelNN_1layer18nodes_300Epoch_tanhNeuron.weights.xml',varlocation+'TMVANN_LowLevelNN_3layer10,10,10_300Epoch_reluNeuron.weights.xml',varlocation+'TMVANN_LowLevelNN_1layer30nodes_300Epoch_tanhNeuron.weights.xml']
xmins = [-0.3,-0.3,-0.3,-0.3,-0.3]
xmaxs = [0.3,0.3,0.3,0.3,0.3]

selector = input("Press 1 to run TMVA analysis, 2 to run the TMVA reader")
if selector == 1:

    TMVANN(inputfilename,outputfilename,signaltree,backgroundtree,TrainingVariables)

if selector == 2:

    TMVAReader(inputfilename,signaltree,backgroundtree,TrainingVariables,varnames,varweightfiles,xmins,xmaxs,signalmllbbtree,backgroundmllbbtree)
    