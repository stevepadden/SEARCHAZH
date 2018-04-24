import ROOT as R
from FileGetter import datas
def TMVAReader (filenameSTRING,sigtreeSTRINGS,bkgtreeSTRING,variablesSTRING,varnames,varweightfiles,xmins,xmaxs,cuts):
    Datamllbb = []
    Datahist = R.TH1F("Datahist", "Datahist", numbins, xmins[0], xmaxs[0])

    def Data(x1):
        for ev in x1:
            Vecl0 = R.TLorentzVector()
            Vecl1 = R.TLorentzVector()
            Vecl0.SetPtEtaPhiM(x1.lep0_pt, x1.lep0_eta, x1.lep0_phi, x1.lep0_m)
            Vecl1.SetPtEtaPhiM(x1.lep1_pt, x1.lep1_eta, x1.lep1_phi, x1.lep1_m)
            mll = (Vecl0 + Vecl1).Mag()
            Vecb0 = R.TLorentzVector()
            Vecb1 = R.TLorentzVector()
            Vecb0.SetPtEtaPhiM(x1.bjet0_pt, x1.bjet0_eta, x1.bjet0_phi, x1.bjet0_m)
            Vecb1.SetPtEtaPhiM(x1.bjet1_pt, x1.bjet1_eta, x1.bjet1_phi, x1.bjet1_m)
            y = (Vecl0 + Vecl1 + Vecb0 + Vecb1).Mag()
            Datahist.Fill(y/1000) #

    for i in range(len(datas)):
        x = datas[i]
        Data(x)
    RootFile = R.TFile("DataMllbb.root", "recreate")


    #from array import array



    #datamllbb = array('f', [0.])
    #Tree.Branch('Mllbb', datamllbb, 'Mllbb/F')  # fill the branch with the array in /F (float) style
    #for i in range(len(Datamllbb)):
    #    datamllbb[0] = Datamllbb[i]  # Fill the actual arrays
    #    Tree.Fill()
    canvas = R.TCanvas()
    #Datahist.Scale(10)
    Datahist.SetStats(1)
    ymax = Datahist.GetBinContent(Datahist.GetMaximumBin())

    Datahist.GetYaxis().SetRangeUser(0, ymax * 1.5)
    Datahist.SetLineColor(R.kRed)
    Datahist.Draw("HIST")
    R.gPad.RedrawAxis()
    canvas.Print("DataTMVA.png")

    Datahist.Write('Data')
    RootFile.Close()
    ii = 0
    for sigtreeSTRING in sigtreeSTRINGS:
        inputfile = R.TFile(filenameSTRING,"read")
        reader = R.TMVA.Reader()
        signalhists = []
        backgroundhists= []
        for varname,xmin,xmax in zip(varnames,xmins,xmaxs):
            signalhist = R.TH1F("SignalHist" + varname,"",numbins,xmin,xmax )
            backgroundhist =  R.TH1F("BackgroundHist" + varname,"",numbins,xmin,xmax)
            signalhists.append(signalhist)
            backgroundhists.append(backgroundhist)

        sigtree = inputfile.Get(sigtreeSTRING)
        bkgtree = inputfile.Get(bkgtreeSTRING)

        print ('array reached')
        from array import array
        branchdict = {}
        for i in variablesSTRING:
            branchdict[i] = array('f',[0.])
            print ('Branch Okay')
            reader.AddVariable(i,branchdict[i])
            sigtree.SetBranchAddress(i,branchdict[i])

        for name,file in zip(varnames,varweightfiles):
            reader.BookMVA(name+sigtreeSTRING,file)

        i = 0

        while sigtree.GetEntry(i):
            i += 1
            for  name,histo in zip(varnames,signalhists):
                classify = reader.EvaluateMVA(name+sigtreeSTRING)
                if classify>cuts[ii]:
                    histo.Fill(sigtree.Mllbb/1000)

        i = 0



        for histosig,histobkg,name in zip(signalhists,backgroundhists,varnames):
            canvas = R.TCanvas()
            histosig.SetStats(1)
            ymax = None
            ymax = Datahist.GetBinContent(histosig.GetMaximumBin())
            RootFile = R.TFile("DataMllbb.root", "update")

            histosig.GetYaxis().SetRangeUser(0,ymax*1.5)
            histosig.SetLineColor(R.kBlack)
            histosig.GetXaxis().SetRangeUser(xmins[0],xmaxs[0])
            histosig.GetXaxis().SetTitle("m_{llbb} [GeV]")
            histosig.GetYaxis().SetTitle("Events")
            histosig.SetFillColor(R.kSpring-4)
            histosig.SetStats(0)
            histosig.Draw("HIST")
            Datahist.Draw("HIST,same")
            legend = R.TLegend(0.7, 0.7, 0.9,
                               0.9)  # Creating the legend with location and size arguments - not sure which - just played around
            legend.SetHeader("Components Of Histogram", "C")  # Setting the legend with a central title ( ,C )
            legend.AddEntry(histosig, "Classifier response for m_A = " + macuts[ii],
                            "f")  # it is possible to replace the "lep" with for example "l" to represent just a straight line - worth playing with
            legend.AddEntry(Datahist, "Taken Data", "l")  # Sets a line in the legend box
            legend.Draw()
            #Adding the data histogram & scaling to background levels
            temp = Datahist.GetBinContent(Datahist.GetMaximumBin())
            #scaler = ymax/temp
            #Datahist.Scale(scaler)
            #Datahist.Draw("HIST,same")
            

            R.gPad.RedrawAxis()
            canvas.Print('Data'+macuts[ii]+".png")
            histosig.Write("Signal_"+sigtreeSTRING)
            histobkg.Write("Background")
            RootFile.Close()
            ii+=1













signaltree = ['Data','Data','Data','Data']
macuts = ['400','500','600','700']
weights = 'Weight'  
backgroundtree = 'Background'
TrainingVariables = ['Mbb','Zpt','Jvar']
outputfilename = 'TMVANN.root'
inputfilename = 'Data200.root'
varnames = ['ArtificialNeuralNetwork_4Layer8Node_50Epoch_tanhNeuron']
varlocation = 'datasetsignals/weights/'
varweightfiles =   [varlocation+'TMVANN_ArtificialNeuralNetwork_4Layer8Node_500Epoch_tanhNeuron.weights.xml'
                    ]
global numbins
numbins = 300
xmins = [0]
xmaxs = [800]
cuts = [0.01,0.01618,0.01,0.016]

TMVAReader(inputfilename, signaltree, backgroundtree, TrainingVariables, varnames, varweightfiles, xmins, xmaxs,cuts)