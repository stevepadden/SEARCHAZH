import sys
import ROOT as R

def TMVANN (filenameSTRING,outputDOTrootSTRING,sigtreeSTRINGS,bkgtreeSTRING,variablesSTRING):
    NNfile = R.TFile(outputDOTrootSTRING, "recreate")
    NNfile.Close()
    for sigtreeSTRING in sigtreeSTRINGS:
        from ROOT import TMVA
        file = R.TFile(filenameSTRING)          #importing the datasetsignals
        signaltree = file.Get(sigtreeSTRING)    #setting signaltree
        backgroundtree = file.Get(bkgtreeSTRING) #setting backgroundtree)
        sigweights = file.Get(sigtreeSTRING+weights)
        bkgweights = file.Get(bkgtreeSTRING+weights)
        TMVA.Tools.Instance()

        NNfile = R.TFile(outputDOTrootSTRING,"update")      #Writing the root file required for the TMVA factory

        TMVAfactory = TMVA.Factory("TMVANN",NNfile,"V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification")
        TMVAfactory.SetVerbose(False)  #Setting extra info (verbose) to false

        datasetsignals = TMVA.DataLoader("datasetsignals")     #Instantiating a datasetsignals
        datasetsignals.AddSignalTree(signaltree,1.)     #adding signal
        datasetsignals.AddBackgroundTree(backgroundtree ,1.) #adding background
        print(sigweights)
        datasetsignals.SetSignalWeightExpression(weights)
        datasetsignals.SetBackgroundWeightExpression(weights)

        for i in variablesSTRING:                #adding our training variables to the TMVA
            datasetsignals.AddVariable(i)

        signalcut = R.TCut("")  #Variables are already cut
        backgroundcut = R.TCut("")
        datasetsignals.PrepareTrainingAndTestTree(signalcut,backgroundcut,"nTrain_Signal= 0:nTrain_Background=0:Splitmode=Random:NormMode=NumEvents:!V")
        TMVAfactory.BookMethod(datasetsignals,TMVA.Types.kMLP,"ArtificialNeuralNetwork_4Layer8Node_500Epoch_tanhNeuron"+sigtreeSTRING,"H:!V:NeuronType=tanh:VarTransform=N:NCycles=500:HiddenLayers=8,8,8,8:TestRate=5")         #Artifical Neural Network 8 layers 500 epoch




        TMVAfactory.TrainAllMethods()
        TMVAfactory.TestAllMethods()
        TMVAfactory.EvaluateAllMethods()
        NNfile.Close()
    NNfile = R.TFile(outputDOTrootSTRING, "update")

def TMVAReader (filenameSTRING,sigtreeSTRINGS,bkgtreeSTRING,variablesSTRING,varnames,varweightfiles,xmins,xmaxs):
    for sigtreeSTRING in sigtreeSTRINGS:
        inputfile = R.TFile(filenameSTRING,"read")
        reader = R.TMVA.Reader()
        signalhists = []
        backgroundhists= []
        for varname,xmin,xmax in zip(varnames,xmins,xmaxs):
            signalhist = R.TH1F("SignalHist" + varname+sigtreeSTRING,"Signal"+varname+sigtreeSTRING,60,xmin,xmax )
            backgroundhist =  R.TH1F("BackgroundHist Hist" + "Background"+ varname,varname,60,xmin,xmax)
            signalhists.append(signalhist)
            backgroundhists.append(backgroundhist)

        sigtree = inputfile.Get(sigtreeSTRING)
        bkgtree = inputfile.Get(bkgtreeSTRING)

        from array import array       #ADD NAME STRINGS!!
        branchdict = {}
        for i in variablesSTRING:
            branchdict[i+sigtreeSTRING] = array('f',[0.])
            reader.AddVariable(i+sigtreeSTRING,branchdict[i+sigtreeSTRING])
            sigtree.SetBranchAddress(i+sigtreeSTRING,branchdict[i+sigtreeSTRING])
            bkgtree.SetBranchAddress(i+sigtreeSTRING,branchdict[i+sigtreeSTRING])

        for name,file in zip(varnames,varweightfiles):
            reader.BookMVA(name+sigtreeSTRING,file)

        i = 0

        while sigtree.GetEntry(i):
            i += 1
            for  name,histo in zip(varnames,signalhists):
                classify = reader.EvaluateMVA(name+sigtreeSTRING)
                if i == 1:
                    print(str(classify) + ' <<---Signal for ' + name+sigtreeSTRING)

                histo.Fill(classify)
        i = 0

        while bkgtree.GetEntry(i):
            i +=1
            for  name,histo in zip(varnames,backgroundhists):
                classify = reader.EvaluateMVA(name+sigtreeSTRING)
                if i == 1:
                    print(str(classify) + ' <<-- Background for ' + name+sigtreeSTRING)
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
            canvas.Print(name+"_"+sigtreeSTRING+".png")

signaltree = ['400','500','600','700']
weights = 'Weight'
backgroundtree = 'Background'
TrainingVariables = ['Mbb','Zpt','Jvar']
outputfilename = 'TMVANNSIGNALS.root'
inputfilename = 'Window200NEW.root'
varnames = ['ArtificialNeuralNetwork_4Layer8Node_500Epoch_tanhNeuron']
varlocation = 'datasetsignals/weights/'
varweightfiles =   [varlocation+'TMVANN_ArtificialNeuralNetwork_4Layer8Node_500Epoch_tanhNeuron.weights.xml',
 
                    ]
xmins = [-0.3]
xmaxs = [0.3]
    
selector = 2            #input("Press 1 to run TMVA analysis, 2 to run the TMVA reader")
if selector == 1:

    TMVANN(inputfilename,outputfilename,signaltree,backgroundtree,TrainingVariables)

if selector == 2:
                                                                                                                                                                                    
    TMVAReader(inputfilename,signaltree,backgroundtree,TrainingVariables,varnames,varweightfiles,xmins,xmaxs)
