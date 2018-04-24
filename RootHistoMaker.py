import sys
import ROOT as R
from FileGetter import *
import HistoMaker as Histo
from numpy import mean as mean

def Maker(Mass,selector,rootname,numbins):
    cuts = [357.253, 439.75, 522.25, 610.25]
    print len(cuts)
    mass_higgs = Mass #Energy in GeV
    M2G = 1000

    window_low = (0.85*mass_higgs)-20
    window_high =mass_higgs+20
    midwind = (window_high+window_low)/2
    if Mass == 130:
        hmin = 200            #0.001 for full range
        hmax = 800           #set to 800 (upper limit on mA) or 1000 for full range
    if Mass == 200:
        hmin = 250
        hmax = 800
    nbins =numbins


    Data_sig_Mllbb = []
    Data_sig_mbb = []
    Data_sig_weight = []
    TT_sig_Mllbb = []
    TT_sig_weight = []
    TT_sig_mbb = []
    Zjet_sig_Mllbb = []
    Zjet_sig_weight = []
    Zjet_sig_mbb = []
    GGhists = []


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
                mbb = ev.mass_mbb

                if ev.NBjets != 2:
                    continue
                if ev.Jvar < 0.4:
                    continue
                if mbb >window_low and mbb <window_high:

                    if (80 *M2G)<mll<(100*M2G):
                        Data_sig_mbb.append(mbb/M2G)
                        Data_sig_Mllbb.append(y/M2G)
                        Data_sig_weight.append((x1.weight)) #/M2G)
            print ('looking at ' + str(ev))


    def TTSignals(x1):
        for t in x1:
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

            if x1.Jvar > 0.4 and (x1.bjet0_pt > 45 * M2G or x1.bjet1_pt > 45 * M2G) and x1.NBjets >= 2 and ( window_low < x1.mass_mbb < window_high):  # applying cuts before filling the Loretnz Vectors

                if (80 * M2G) < mll < (100 * M2G):

                    TT_sig_Mllbb.append(y/M2G)
                    TT_sig_weight.append((x1.weight))   #/M2G)
    def ZJetSignals(x1):
        for t in x1:
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

            if x1.Jvar > 0.4 and (x1.bjet0_pt > 45 * M2G or x1.bjet1_pt > 45 * M2G) and x1.NBjets >= 2 and ( window_low < x1.mass_mbb < window_high):  # applying cuts before filling the Loretnz Vectors

                if (80 * M2G) < mll < (100 * M2G):

                    Zjet_sig_Mllbb.append(y/M2G)
                    Zjet_sig_weight.append((x1.weight))#  /M2G)



    Datatimer = 0.0
    Datatimeleft = (len(datas))
    for i in range(len(datas)):
        x = datas[i]
        Data(x)
        percent = (Datatimer / Datatimeleft) * 100
        print (str(int(percent)) + '% of Data completed')
        Datatimer = Datatimer + 1

    TTtimer = 0.0
    TTtimeleft = (len(TTbars))
    for i in  range(len(TTbars)):
        x = TTbars[i]
        TTSignals(x)
        # Below is just the timer
        percent = (TTtimer / TTtimeleft) * 100
        print (str(int(percent)) + '% of TT completed')
        TTtimer = TTtimer + 1
    print TT_sig_Mllbb

    Zjettimer = 0.0
    Zjettimeleft = (len(Zjets))
    for i in range (len(Zjets)):
        x = Zjets[i]
        ZJetSignals(x)
        # Below is just the timer
        percent = (Zjettimer / Zjettimeleft) * 100
        print (str(int(percent)) + '% of Zjet completed')
        Zjettimer = Zjettimer + 1


    DataSignalHist = None
    DataSignalHist = Histo.Histogrammaker(DataSignalHist, "", "", nbins, hmin, hmax, Data_sig_Mllbb,Data_sig_weight)       #Needs decleration of 1'st variable prior to calling

    TTsignalhist = None
    TTsignalhist = Histo.Histogrammaker(TTsignalhist,"","",nbins,hmin,hmax,TT_sig_Mllbb,TT_sig_weight)

    Zjetsignalhist = None
    Zjetsignalhist = Histo.Histogrammaker(Zjetsignalhist,"","",nbins,hmin,hmax,Zjet_sig_Mllbb,Zjet_sig_weight)
    comb = Zjetsignalhist+TTsignalhist

    datasignalcanvas = None
    databgcanvas = None
    TTsignalcanvas = None
    TTbackgroundcanvas = None
    Zjetsignalcanvas = None
    Zjetbackgroundcanvas = None
    combcanvas = None


    Histo.Draw(datasignalcanvas,DataSignalHist,"L",R.kRed,"Data_Signal_Canvas_" + str(mass_higgs)+'.png')
    Histo.Draw(TTsignalcanvas,TTsignalhist,"PE",R.kBlue,"TT_Signal_Canvas_" + str(mass_higgs)+'.png')
    Histo.Draw(Zjetsignalcanvas,Zjetsignalhist,"PE",R.kMagenta,"Zjet_Signal_Canvas_" + str(mass_higgs)+'.png')
    Histo.Draw(combcanvas,comb,"PE",R.kBlack,"TT_+_Zjets_" + str(mass_higgs)+'.png')

    print('The Integral of the Signal Data Histogram is ' + str(DataSignalHist.Integral(0,101)))
    print('The Integral of the Signal TT bar histogram is ' + str(TTsignalhist.Integral(0,101)))
    print('The Integral of the Signal Zjet Histogram is' + str(Zjetsignalhist.Integral(0,101)))
    print('The intergal of the combined canvas is ' + str(comb.Integral(0,101)))

    Histowindow = R.TFile("Window_" + str(mass_higgs)+".root", "recreate")

    DataSignalHist.Write("Data")
    TTsignalhist.Write("TT")
    Zjetsignalhist.Write("Zjet")
    comb.Write("TTbarANDZjet")


    # ZjetbgHist.Write("Zjet_Background")

    def compile(GGA,name,colour):
        print(GGA)
        GG_sig_Mllbb = []
        GG_sig_Mllbb = []
        GG_sig_weight = []
        GGsignalhist = None

        for t in GGA:
                Vecl0 = R.TLorentzVector()
                Vecl1 = R.TLorentzVector()
                Vecl0.SetPtEtaPhiM(GGA.lep0_pt, GGA.lep0_eta, GGA.lep0_phi, GGA.lep0_m)
                Vecl1.SetPtEtaPhiM(GGA.lep1_pt, GGA.lep1_eta, GGA.lep1_phi, GGA.lep1_m)
                mll = (Vecl0 + Vecl1).Mag()
                Vecb0 = R.TLorentzVector()
                Vecb1 = R.TLorentzVector()
                Vecb0.SetPtEtaPhiM(GGA.bjet0_pt, GGA.bjet0_eta, GGA.bjet0_phi, GGA.bjet0_m)
                Vecb1.SetPtEtaPhiM(GGA.bjet1_pt, GGA.bjet1_eta, GGA.bjet1_phi, GGA.bjet1_m)
                y = (Vecl0 + Vecl1 + Vecb0 + Vecb1).Mag()  # SCALE THIS SO 4 VECTOR GIVES MASS OF CENTRE OF WINDOW

                if GGA.Jvar > 0.4 and (GGA.bjet0_pt > 45 * M2G or GGA.bjet1_pt > 45 * M2G) and GGA.NBjets >= 2 and (
                        window_low < GGA.mass_mbb < window_high):  # applying cuts before filling the Loretnz Vectors

                    if (80 * M2G) < mll < (100 * M2G):
                        GG_sig_Mllbb.append(y/M2G)
                        GG_sig_weight.append((GGA.weight))              #/M2G)

        #        GGsignalhist = Histo.Histogrammaker(GGsignalhist, "", "GG signal Histogram", nbins,hmin*M2G,hmax*M2G, GG_sig_Mllbb,   # +delta scales the signal
        #                                    GG_sig_weight)
        GGsignalhist = Histo.Histogrammaker(GGsignalhist, "", "Signal for m_{A} =" + name, nbins,hmin,hmax, GG_sig_Mllbb,   # +delta scales the signal
                                            GG_sig_weight)
        GGsignalhist.Write("GGA_" + name)
        print (GGsignalhist)
        GGhists.append(GGsignalhist)
        #GGsignalhist.Draw("same")
        #GGsignalhist.SetLineColor(colour)
        #print('The Integral of the Signal Histogram is ' + str(GGsignalhist.Integral(0, 101)))


    if mass_higgs == (200):
        ggtimer = 0.0                #Has to be non integer
        ggtimeleft = (len(GGA_MH200))

        for i in range(len(GGA_MH200)):
            x = GGA_MH200[i]
            compile(x, names200[i],colours200[i])

            # Below is just the timer
            percent = (ggtimer / ggtimeleft) * 100
            print (str(int(percent)) + '% of GG completed')
            ggtimer = ggtimer + 1

    if mass_higgs == (130):
        ggtimer = 0.0  # Has to be non integer
        ggtimeleft = (len(GGA_MH130))

        for i in range(len(GGA_MH130)):
            x = GGA_MH130[i]
            compile(x, names130[i], colours130[i])

            # Below is just the timer
            percent = (ggtimer / ggtimeleft) * 100
            print (str(int(percent)) + '% of GG completed')
            ggtimer = ggtimer + 1



    print (GGhists)

    FullCanvas = R.TCanvas()
    DataSignalHist.Draw()
    DataSignalHist.SetLineColor(R.kRed)
    Zjetsignalhist.Draw("same")
    Zjetsignalhist.SetLineColor(R.kBlue)
    TTsignalhist.Draw("same")
    TTsignalhist.SetLineColor(R.kOrange)
    comb.Draw("Same")
    if mass_higgs == 200:
        for i in range(len(GGhists)):
            GGhists[i].Draw("same")
            GGhists[i].SetLineColor(R.kSpring-4)#colours200[i])
            GGhists[i].SetFillColor(R.kSpring-4)

    if mass_higgs == 130:
        for i in range(len(GGhists)):
            GGhists[i].SetLineColor(R.kSpring-4)#colours200[i])
            GGhists[i].SetFillColor(R.kSpring-4)



    concatname = str("Window_"+str(mass_higgs)+"_signal.png")
    FullCanvas.Print(concatname)

    if mass_higgs == 200:
        for i in range(len(GGhists)):

            FullCanvas = R.TCanvas()

            DataSignalHist.Draw("PE")
            DataSignalHist.SetLineColor(R.kRed)

            #GGhists[i].SetFillColor(R.kSpring - 4)
            GGhists[i].SetLineColor(R.kBlack)#colours200[i])
            GGhists[i].SetFillColor(R.kSpring-4)
            GGhists[i].Draw("HIST,same")
            Zjetsignalhist.Draw("HIST,same")
            Zjetsignalhist.SetLineColor(R.kCyan)
            TTsignalhist.Draw("HIST,same")
            TTsignalhist.SetLineColor(R.kOrange)
            comb.Draw("HIST,same")
            comb.SetLineColor(R.kBlue)
            #GGhists[i].SetLineColor(colours200[i])
            concatname = str("Window_" + str(mass_higgs) + "_signal"+names200[i]+'.png')

            legend = R.TLegend(0.7, 0.7, 0.9,
                               0.9)  # Creating the legend with location and size arguments - not sure which - just played around
            legend.SetHeader("Components Of Histogram", "C")  # Setting the legend with a central title ( ,C )
            legend.AddEntry(Zjetsignalhist, "ZZ",
                            "l")  # it is possible to replace the "lep" with for example "l" to represent just a straight line - worth playing with
            legend.AddEntry(GGhists[i], "mA ="+names200[i], "f")  # Sets a line in the legend box
            legend.AddEntry(TTsignalhist, "TT", "fl")  # Sets a fill in legend
            legend.AddEntry(DataSignalHist, "Data", "lep")  # Sets error bar in legend
            legend.AddEntry(comb,"Background","l")
            legend.Draw()

            # Setting the axis and titles - I had to set these on the leading Histogram (DataHist in my case) not the canvas.

            DataSignalHist.GetXaxis().SetTitle("m_{llbb} [GeV]")
            DataSignalHist.GetYaxis().SetTitle("Events")
            DataSignalHist.SetStats(False)
            #DataSignalHist.SetStats(0)
            Zjetsignalhist.SetStats(False)
            TTsignalhist.SetStats(False)
            comb.SetStats(False)
            GGhists[i].SetStats(False)

            # DataHist.GetXaxis().SetRangeUser(400 * M2G, 1000 * M2G)
            # DataHist.GetYaxis().SetRangeUser(0, 100)
            FullCanvas.Print(concatname)


    if mass_higgs == 130:
        for i in range(len(GGhists)):
            DataSignalHist.SetStats(False)
            FullCanvas = R.TCanvas()
            DataSignalHist.Draw("PE")
            DataSignalHist.SetLineColor(R.kRed)
            GGhists[i].SetLineColor(R.kBlack)#colours200[i])
            GGhists[i].SetFillColor(R.kSpring-4)
            GGhists[i].Draw("HIST,same")
            Zjetsignalhist.Draw("HIST,same")
            Zjetsignalhist.SetLineColor(R.kCyan)
            TTsignalhist.Draw("HIST,same")
            TTsignalhist.SetLineColor(R.kOrange)
            comb.Draw("HIST,same")
            comb.SetLineColor(R.kBlue)
            concatname = str("Window_" + str(mass_higgs) + "_signal"+names130[i]+'.png')


            legend = R.TLegend(0.7, 0.7, 0.9,
                   0.9)
# Creating the legend with location and size arguments - not sure which - just played around
            legend.SetHeader("Components Of Histogram", "C")  # Setting the legend with a central title ( ,C )
            legend.AddEntry(Zjetsignalhist, "ZZ",
                            "l")  # it is possible to replace the "lep" with for example "l" to represent just a straight line - worth playing with
            legend.AddEntry(GGhists[i], "mA ="+names130[i], "f")  # Sets a line in the legend box
            legend.AddEntry(TTsignalhist, "TT", "fl")  # Sets a fill in legend
            legend.AddEntry(DataSignalHist, "Data", "lep")  # Sets error bar in legend
            legend.Draw()

            # Setting the axis and titles - I had to set these on the leading Histogram (DataHist in my case) not the canvas.

            DataSignalHist.GetXaxis().SetTitle("m_{llbb} [GeV]")
            DataSignalHist.GetYaxis().SetTitle("Events")
            DataSignalHist.SetStats(False)
            DataSignalHist.SetStats(0)
            Zjetsignalhist.SetStats(False)
            TTsignalhist.SetStats(False)
            comb.SetStats(False)
            GGhists[i].SetStats(False)
            FullCanvas.Print(concatname)


    Histowindow.Close()

    cuts = [357.253,439.75,522.25,610.25]
    if len(cuts) == 4 and mass_higgs == 200:
        iii=0
        for z in range(len(cuts)):
            combihist = None
            signalmllbbcut = []
            signalmllbbweight = []
            signalmllbbhisto = None
            combimllbbcut = []
            combimllbbweight = []
            for i in range(len(TT_sig_Mllbb)):
                if TT_sig_Mllbb[i]> cuts[iii]:
                    combimllbbcut.append(TT_sig_Mllbb[i])
                    combimllbbweight.append(TT_sig_weight[i])
            for i in range(len(Zjet_sig_Mllbb)):
                if Zjet_sig_Mllbb[i]> cuts[iii]:
                    combimllbbcut.append(Zjet_sig_Mllbb[i])
                    combimllbbweight.append(Zjet_sig_weight[i])
            for GGA in GGA_MH200[iii]:
                    Vecl0 = R.TLorentzVector()
                    Vecl1 = R.TLorentzVector()
                    Vecl0.SetPtEtaPhiM(GGA.lep0_pt, GGA.lep0_eta, GGA.lep0_phi, GGA.lep0_m)
                    Vecl1.SetPtEtaPhiM(GGA.lep1_pt, GGA.lep1_eta, GGA.lep1_phi, GGA.lep1_m)
                    mll = (Vecl0 + Vecl1).Mag()
                    Vecb0 = R.TLorentzVector()
                    Vecb1 = R.TLorentzVector()
                    Vecb0.SetPtEtaPhiM(GGA.bjet0_pt, GGA.bjet0_eta, GGA.bjet0_phi, GGA.bjet0_m)
                    Vecb1.SetPtEtaPhiM(GGA.bjet1_pt, GGA.bjet1_eta, GGA.bjet1_phi, GGA.bjet1_m)
                    y = (Vecl0 + Vecl1 + Vecb0 + Vecb1).Mag()  # SCALE THIS SO 4 VECTOR GIVES MASS OF CENTRE OF WINDOW

                    if GGA.Jvar > 0.4 and (GGA.bjet0_pt > 45 * M2G or GGA.bjet1_pt > 45 * M2G) and GGA.NBjets >= 2 and (
                            window_low < GGA.mass_mbb < window_high):  # applying cuts before filling the Loretnz Vectors

                        if (80 * M2G) < mll < (100 * M2G):
                            if (y/M2G) > cuts[iii]:
                                signalmllbbcut.append(y/M2G)
                                signalmllbbweight.append(GGA.weight)
            signalmllbbhisto = Histo.Histogrammaker(signalmllbbhisto, "", "", nbins, hmin, hmax, signalmllbbcut,
                                                        signalmllbbweight)  # Needs decleration of 1'st variable prior to calling
            combihist = Histo.Histogrammaker(combihist, "", "", nbins, hmin, hmax, combimllbbcut, combimllbbweight)
            if signalmllbbhisto.GetMinimumBin() < combihist.GetMinimumBin():
                xmin = signalmllbbhisto.GetBinContent(signalmllbbhisto.GetMinimumBin())
            else:
                xmin = combihist.GetBinContent(combihist.GetMinimumBin())

            signalmllbbhisto.GetXaxis().SetRangeUser(cuts[iii],800)
            ymax = None
            if signalmllbbhisto.GetBinContent(signalmllbbhisto.GetMaximumBin()) > combihist.GetBinContent(combihist.GetMaximumBin()):
                ymax = signalmllbbhisto.GetBinContent(signalmllbbhisto.GetMaximumBin())
            else:
                ymax = combihist.GetBinContent(combihist.GetMaximumBin())
            cutCanvas = R.TCanvas()
            signalmllbbhisto.GetYaxis().SetRangeUser(0,ymax*1.2)


            signalmllbbhisto.Draw("HIST")
            signalmllbbhisto.SetLineColor(R.kBlack)
            signalmllbbhisto.SetFillColor(R.kSpring-4)
            combihist.Draw("HIST,same")
            cutconcatname = str("cut_mllbb_mA_" + names200[iii] +'.png')

            legend = R.TLegend(0.7, 0.7, 0.9,
                               0.9)  # Creating the legend with location and size arguments - not sure which - just played around
            legend.SetHeader("Components Of Histogram", "C")  # Setting the legend with a central title ( ,C )
            legend.AddEntry(combihist, "Background",
                            "l")  # it is possible to replace the "lep" with for example "l" to represent just a straight line - worth playing with
            legend.AddEntry(signalmllbbhisto, "mA ="+names200[iii], "f")  # Sets a line in the legend box
            legend.Draw()

            # Setting the axis and titles - I had to set these on the leading Histogram (DataHist in my case) not the canvas.

            signalmllbbhisto.GetXaxis().SetTitle("m_{llbb} [GeV]")
            signalmllbbhisto.GetYaxis().SetTitle("Events")
            signalmllbbhisto.SetStats(False)
            combihist.SetStats(False)
            cutCanvas.Print(cutconcatname)
            iii += 1


