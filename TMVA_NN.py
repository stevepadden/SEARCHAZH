import sys
import ROOT as R

def TMVANN (filenameSTRING,outputDOTrootSTRING,sigtreeSTRINGS,bkgtreeSTRING,variablesSTRING):
    for sigtreeSTRING in sigtreeSTRINGS:
        from ROOT import TMVA
        file = R.TFile(filenameSTRING)          #importing the dataset
        signaltree = file.Get(sigtreeSTRING)    #setting signaltree
        backgroundtree = file.Get(bkgtreeSTRING) #setting backgroundtree)
        sigweights = file.Get(sigtreeSTRING+weights)
        bkgweights = file.Get(bkgtreeSTRING+weights)
        TMVA.Tools.Instance()

        NNfile = R.TFile(outputDOTrootSTRING,"recreate")      #Writing the root file required for the TMVA factory

        TMVAfactory = TMVA.Factory("TMVANN",NNfile,"V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification")
        TMVAfactory.SetVerbose(False)  #Setting extra info (verbose) to false

        dataset = TMVA.DataLoader("dataset")     #Instantiating a dataset
        dataset.AddSignalTree(signaltree,1.)     #adding signal
        dataset.AddBackgroundTree(backgroundtree ,1.) #adding background
        print(sigweights)
        #dataset.SetSignalWeightExpression(weights)
        #dataset.SetBackgroundWeightExpression(weights)

        for i in variablesSTRING:                #adding our training variables to the TMVA
            dataset.AddVariable(i)

        signalcut = R.TCut("")  #Variables are already cut
        backgroundcut = R.TCut("")
        dataset.PrepareTrainingAndTestTree(signalcut,backgroundcut,"nTrain_Signal= 0:nTrain_Background=0:Splitmode=Random:NormMode=NumEvents:!V")
        #using all signal and background points to train, random selection, normalised to summed event weights = number of events for each tree, no verbose

        #Booking some methods
        #TMVAfactory.BookMethod(dataset,TMVA.Types.kMLP,"ArtificialNeuralNetwork_1Layer_500Epoch_tanhNeuron","H:!V:NeuronType=tanh:VarTransform=N:NCycles=500:HiddenLayers=8:TestRate=5")         #Artifical Neural Network 1 layers 500 epoch

        TMVAfactory.BookMethod(dataset,TMVA.Types.kFisher, "FisherMethod","H:!V:Fisher:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=60:NsmoothMVAPdf=10")    #Fisher Method
        TMVAfactory.BookMethod(dataset,TMVA.Types.kLikelihood, "BayesLikelihood","H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=60")    #Bayes likleihood
        TMVAfactory.BookMethod(dataset,TMVA.Types.kMLP,"ArtificialNeuralNetwork_4Layer8Node_500Epoch_tanhNeuron","H:!V:NeuronType=tanh:VarTransform=N:NCycles=500:HiddenLayers=8,8,8,8:TestRate=5")         #Artifical Neural Network 8 layers 500 epoch
        TMVAfactory.BookMethod(dataset,TMVA.Types.kMLP,"ArtificialNeuralNetwork_1Layer6Node_500Epoch_reluNeuron","H:!V:NeuronType=tanh:VarTransform=N:NCycles=500:HiddenLayers=6:TestRate=5")         #Artifical Neural Network 8 layers 500 epoch
        TMVAfactory.BookMethod(dataset,TMVA.Types.kMLP,"ArtificialNeuralNetwork_1Layer3Node_100Epoch_reluNeuron","H:!V:NeuronType=tanh:VarTransform=N:NCycles=100:HiddenLayers=3:TestRate=5")         #Artifical Neural Network 8 layers 500 epoch
        TMVAfactory.BookMethod(dataset,TMVA.Types.kMLP,"ArtificialNeuralNetwork_2Layer5Node_500Epoch_tanhNeuron","H:!V:NeuronType=tanh:VarTransform=N:NCycles=500:HiddenLayers=5,5:TestRate=5")         #Artifical Neural Network 8 layers 500 epoch





        TMVAfactory.TrainAllMethods()
        TMVAfactory.TestAllMethods()
        TMVAfactory.EvaluateAllMethods()
        NNfile.Close()
        print ('TMVANN Ran & made ROOT file ' + outputDOTrootSTRING+sigtreeSTRING)

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
                if i == 1:
                    print(str(classify) + ' <<---Signal for ' + name)

                histo.Fill(classify)
        i = 0

        while bkgtree.GetEntry(i):
            i +=1
            for  name,histo in zip(varnames,backgroundhists):
                classify = reader.EvaluateMVA(name)
                if i == 1:
                    print(str(classify) + ' <<-- Background for ' + name)
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













signaltree = ['400']
weights = 'Weight'
backgroundtree = 'Background'
TrainingVariables = ['Mbb','Zpt','Jvar']
outputfilename = 'TMVANN.root'
inputfilename = 'Window200NEW.root'
varnames = ['FisherMethod','BayesLikelihood','ArtificialNeuralNetwork_4Layer8Node_50Epoch_tanhNeuron','ArtificialNeuralNetwork_1Layer6Node_500Epoch_reluNeuron','ArtificialNeuralNetwork_1Layer3Node_1000Epoch_reluNeuron','ArtificialNeuralNetwork_1Layer10Node_100Epoch_reluNeuron','ArtificialNeuralNetwork_2Layer5Node_500Epoch_tanhNeuron']
varlocation = 'dataset/weights/'
varweightfiles =   [varlocation+'TMVANN_FisherMethod.weights.xml',varlocation+'TMVANN_BayesLikelihood.weights.xml',varlocation+'TMVANN_ArtificialNeuralNetwork_4Layer8Node_500Epoch_tanhNeuron.weights.xml',
                    varlocation+'TMVANN_ArtificialNeuralNetwork_1Layer6Node_500Epoch_reluNeuron.weights.xml',varlocation+'TMVANN_ArtificialNeuralNetwork_1Layer3Node_500Epoch_reluNeuron.weights.xml',
                    varlocation+'TMVANN_ArtificialNeuralNetwork_2Layer5Node_500Epoch_tanhNeuron.weights.xml'
                    ]
xmins = [-0.3,-0.3,0,0,0,0,0]
xmaxs = [0.3,0.3,0.1,0.1,0.1,0.1,0.1]

selector = 2#input("Press 1 to run TMVA analysis, 2 to run the TMVA reader")
if selector == 1:

    TMVANN(inputfilename,outputfilename,signaltree,backgroundtree,TrainingVariables)

if selector == 2:
                                                                                                                                                                                    
    TMVAReader(inputfilename,signaltree,backgroundtree,TrainingVariables,varnames,varweightfiles,xmins,xmaxs)
