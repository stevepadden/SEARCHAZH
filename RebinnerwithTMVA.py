import ROOT as R

window200 = R.TFile('Window_200.root','read')
window130 = R.TFile('Window_130.root','read')
TMVANN = R.TFile('TMVANNMllbb.root','read')
TMVANNLL = R.TFile('TMVANNLOWLEVELMllbb.root','read')

global maxevbin
maxevbin = 30
global xmins
global xmaxs
xmins =[300]
xmaxs=[750]


eventmin = 2
#NewNbins = 20
components200 = [window200.TTbarANDZjet,window200.Data,window200.TT,window200.Zjet,window200.GGA_400,window200.GGA_500,window200.GGA_600,window200.GGA_700]
names200 = ['Background','Data','TT','Zjet','gga_mh200_400','gga_mh200_500','gga_mh200_600','gga_mh200_700']
components130 = [window130.TTbarANDZjet,window130.Data,window130.TT,window130.Zjet,window130.GGA_230,window130.GGA_250,window130.GGA_300,window130.GGA_400,window130.GGA_500,window130.GGA_600,window130.GGA_700,window130.GGA_800]
names130 = ('Background','Data','TT','Zjet','gga_mh130_230','gga_mh130_250','gga_mh130_300','gga_mh130_400','gga_mh130_500','gga_mh130_600','gga_mh130_700','gga_mh130_800')
tmvann = [TMVANN.Background,TMVANN.Signal_400,TMVANN.Signal_500,TMVANN.Signal_600,TMVANN.Signal_700,TMVANN.Data]
namestmva = ('Background','Signal400','Signal500','Signal600','Signal700','Data')
tmvannll = [TMVANNLL.Background,TMVANNLL.Signal_400,TMVANNLL.Signal_500,TMVANNLL.Signal_600,TMVANNLL.Signal_700,TMVANNLL.Data]


def Binner(array1,namearray,mass_higgs):
    Histowindow = R.TFile("Window_" + str(mass_higgs) + "REBIN.root", "recreate")
    for i in range(len(array1)):
        x = array1[i]
        name = namearray[i]
        x.Rebin(NewNbins)
        string =  name+"MH_"+str(mass_higgs)+'_Rebin'
        Canvas = R.TCanvas()
        NumBins = x.GetNbinsX()
        FirstBin = x.FindFirstBinAbove(eventmin)
        LastBin = x.FindLastBinAbove(eventmin)
        FirstCenter = x.GetBinCenter(FirstBin)
        LastCenter = x.GetBinCenter(LastBin)
        x.SetAxisRange(FirstCenter,LastCenter)
        x.Draw()
        Canvas.Print(string+'.png')
        x.Write(name)
    Histowindow.Close()

#def Binner2(array1,namearray,mass_higgs):
#    binmin = 10000000000
#    binmax = 0
#
#    for x in array1:
#            print(x)
#            FirstBin = x.FindFirstBinAbove(eventmin)
#            LastBin = x.FindLastBinAbove(eventmin)
#            FirstCenter = x.GetBinCenter(FirstBin)
#            LastCenter = x.GetBinCenter(LastBin)
#            if LastCenter > binmax:
#                binmax = LastCenter
#            if FirstCenter < binmin:
#                binmin = FirstCenter
#
#
#    print (binmin)
#    print (binmax)
#
def Binner2(array1, namearray, mass_higgs):
    binmin = 10000000000
    binmax = 0

    for x in array1:
            print(x)
            FirstBin = x.FindFirstBinAbove(eventmin)
            LastBin = x.FindLastBinAbove(eventmin)
            FirstCenter = x.GetBinCenter(FirstBin)
            LastCenter = x.GetBinCenter(LastBin)
            if LastCenter > binmax:
                binmax = LastCenter
            if FirstCenter < binmin:
                binmin = FirstCenter

    print (binmin)
    print (binmax)

    Histowindow = R.TFile("Window_" + str(mass_higgs) + "REBIN.root", "recreate")

    for i in range(len(array1)):
        x = array1[i]
        name = namearray[i]
        x.Rebin(NewNbins)
        string = name + "MH_" + str(mass_higgs) + '_Rebin'
        Canvas = R.TCanvas()
        NumBins = x.GetNbinsX()
        x.SetAxisRange(binmin, binmax)
        x.Draw()
        Canvas.Print(string+'.png')
        x.Write(name)
    Histowindow.Close()


def Binner3(array1,namearray,mass_higgs):

    Histowindow = R.TFile("Window_" + str(mass_higgs) + "REBIN.root", "recreate")
    maxy= None
    for i in range(len(array1)):
        x=array1[i]
        Canvas = R.TCanvas()
        name = namearray[i]
        string =  name+"MH_"+str(mass_higgs)+'_Rebin'
        #firstbin = x.FindFirstBinAbove(eventmin)
        #lastbin = x.FindLastBinAbove(eventmin)
        #FirstCenter = x.GetBinCenter(firstbin)
        #LastCenter = x.GetBinCenter(lastbin)
        #Final = x.FindFirstBinAbove(0)
        #FinalExtreme = x.GetBinCenter(Final)
        #Del = FinalExtreme/FirstCenter
        #print (Del)
        #CurrentBins = x.GetXaxis().GetNbins()
        #numbinsreq = CurrentBins/Del
        #print(numbinsreq)
        #var = round(CurrentBins/numbinsreq)
        if i == 0:
            ymax = x.GetBinContent(x.GetMaximumBin())
        if name == 'Data':
            print ('YEP')
            temp = x.GetBinContent(x.GetMaximumBin())
            scaler = ymax/temp
            x.Scale(scaler)


        x.Rebin(5)




        x.GetXaxis().SetRangeUser(xmins[0],xmaxs[0])
        #x.SetAxisRange(FirstCenter,LastCenter)
        x.Draw()
        Canvas.Print(string+'.png')
        x.Write(name)

    Histowindow.Close()
    print('File written' + "Window_" + str(mass_higgs) + "REBIN.root" )


masses = ['200','130','TMVA200','TMVALL200']
Binner3(components200,names200,masses[0])
Binner3(components130,names130,masses[1])
Binner3(tmvann,namestmva,masses[2])
Binner3(tmvannll,namestmva,masses[3])








