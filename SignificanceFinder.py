import ROOT as R
from math import sqrt as sqrt
inputfile = R.TFile('Window_200.root','read') #just change this
signals = ['400','500','600','700']             #this
BackgroundAZH = inputfile.Get('TTbarANDZjet')         #and this
sigfiles = []
sigprefix = 'GGA_'                         #and maybe this if you have a suffix before the signal name
for i in signals:                                                                    #everything else is handeled in code
    sigfiles.append(inputfile.Get(sigprefix+i))
print sigfiles


def roccurve (signal,background,signals):
    from ROOT import TGraph as graph
    from ROOT import TCanvas
    from ROOT import TLegend
    canvas = TCanvas()
    numbins = signal.GetNbinsX()
    Graph = graph()
    totalsig = signal.Integral(0,numbins+1)
    totalbkg = background.Integral(0,numbins+1)
    Significancecounter = 0
    cutval = 0
    temparray = []
    summer = 0

    for i in range (1,numbins):

        signalefficiency = signal.Integral(i,numbins+1)/totalsig
        backgroundefficiency = background.Integral(i,numbins+1)/totalbkg

        #temp = signalefficiency * (1-backgroundefficiency)
        #print temp
        #summer += temp
        Graph.SetPoint(i-1,signalefficiency,1-backgroundefficiency)
        significance = signal.Integral(i,numbins+1)/sqrt((signal.Integral(i,numbins+1))+(background.Integral(i,numbins+1)))
        if signalefficiency == 0:
            break
        if backgroundefficiency == 0:
            break
        if significance > Significancecounter:
            Significancecounter = significance
            cutval = i
            temparray.append(significance)
    Graph.SetTitle("")
    Graph.GetXaxis().SetTitle("Signal Efficiency")
    Graph.GetYaxis().SetTitle("1-Background Efficiency")
    Graph.Draw()#("ALC") # Setting to draw axis around the curve in a smooth curve
    canvas.Print('rocurve'+name+'.png')
    print(summer)
    cutvalGEV = (background.GetBinCenter(cutval))
    print Significancecounter
    print (background.GetBinCenter(cutval))
    print ('Optimum significance for ' + name + 'GeV window found at cut value ' + str(cutvalGEV) +' Giving value ' + str(Significancecounter) + '(classifier cut at bin ' + str(cutval) + ')' )
    return Graph

for signal,name in zip(sigfiles,signals):
    roccurve(signal,BackgroundAZH,name)