import ROOT  as R

extension = '/home/steve/PycharmProjects/AZH/RootHistos/limitplots/' ##CHANGE THIS TO CHANGE WHERE PLOTS SAVE!


masses200 = [400.,500.,600.,700.]

#CUT BASED LIMITS
mediancut=[0.224147,0.0886944,0.0473405,0.0269906]
cutexl2 = [0.120306,0.0476046,0.0254089,0.0144865]
cutexl1 = [0.161511,0.0639092,0.0341114,0.0194482]
cutexh1 = [0.312597,0.124471,0.0670678,0.0388026]
cutexh2 = [0.421683,0.169708,0.0928832,0.0551002]
zeros = [0.0,0.0,0.0,0.0]
#TMVA LIMITS
mediantmva = [0.0773712,0.0351421,0.0190845,0.0167283]
tmvaexl2 = [0.0415271,0.01888616,0.0102431,0.00897852]
tmvaexl1 = [0.0557502,0.0253218,0.0137514,0.0120537]
tmvaexh1 = [0.107765,0.0489744,0.0266178,0.0232874]
tmvaevh2 = [0.144963,0.0659551,0.0359038,0.0313087]

#LOW LEVEL TMVA LIMITS

mediantmvaLL = [0.0826337,0.0477397,0.0340525,0.0273244]
tmvaLLexl2 = [0.0443517,0.0256231,0.0182768,0.0146657]
tmvaLLexl1 = [0.0595422,0.0343991,0.0245367,0.0196888]
tmvaLLexh1 = [0.115104,0.0665071,0.0474728,0.038123]
tmvaLLexh2 = [0.15486,0.0895756,0.0640033,0.0514282]

tmvaERRORUP = []
tmvaERRORDOWN = []
tmvaLLERRORUP = []
tmvaLLERRORDOWN = []
cutERRORUP = []
cutERRORDOWN = []

def error (median,errorup,errordown,ERRORUP,ERRORDOWN):
    for i in range(len(median)):
        ERRORUP.append(errorup[i]-median[i])
        ERRORDOWN.append(errordown[i])# + median[i])
error(mediancut,cutexh2,cutexl2,cutERRORUP,cutERRORDOWN)
error(mediantmva,tmvaevh2,tmvaexl2,tmvaERRORUP,tmvaERRORDOWN)
error(mediantmvaLL,tmvaLLexh2,tmvaLLexl2,tmvaLLERRORUP,tmvaLLERRORDOWN)



from ROOT import TGraphAsymmErrors as Graph
from ROOT import TCanvas as Canvas
from ROOT import TLegend as Legend
from ROOT import gStyle
import numpy as np

#x = np.array(masses200)#SETTING UP ARRAYS SO THEY ARE CONTIGUOUS
#xes = np.array(zeros)
#
#y = np.array(mediancut)
#yues = np.array(cutexh2)
#ydes = np.array(cutexl2)
#
#y1 = np.array(mediantmva)
#y1ues = np.array(tmvaevh2)
#y1des = np.array(tmvaexl2)
#
#y2 = np.array(mediantmvaLL)
#y2ues = np.array(tmvaLLexh2)
#y2des = np.array(tmvaLLexl2)

x = np.array(masses200)      #SETTING UP ARRAYS SO THEY ARE CONTIGUOUS
xes = np.array(zeros)

y = np.array(mediancut)
yues = np.array(cutERRORUP)
ydes = np.array(cutERRORDOWN)

y1 = np.array(mediantmva)
y1ues = np.array(tmvaERRORUP)
y1des = np.array(tmvaERRORDOWN)
y2 = np.array(mediantmvaLL)
y2ues = np.array(tmvaLLERRORUP)
y2des = np.array(tmvaLLERRORDOWN)




numbins = 4
canvas = Canvas()
graph = Graph(numbins,x,y,xes,xes,ydes,yues)      #CALLING AN OBJECT OF TYPE TGraphAsymmErrors
#graph = Graph(numbins,np.array(masses200),np.array(mediantmva),np.array(zeros),np.array(zeros),np.array(cutexl2),np.array(cutexh2))
graph.SetTitle("")
graph.GetXaxis().SetTitle("m_{llbb} GeV")
graph.GetYaxis().SetTitle("Limits")
graph.SetLineColor(R.kBlack)
gStyle.SetEndErrorSize(10)

graph.Draw("ALP*1")
legend = Legend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(graph,"Cut Based Limits","l")
legend.Draw("same")
canvas.Print(extension+'Tgraphlimits.png')

canvas = Canvas()
graph = Graph(numbins,x,y,xes,xes,ydes,yues)
graph1 = Graph(numbins,x,y1,xes,xes,y1des,y1ues)
#graph = Graph(numbins,np.array(masses200),np.array(mediantmva),np.array(zeros),np.array(zeros),np.array(cutexl2),np.array(cutexh2))
graph.SetTitle("")
graph.GetXaxis().SetTitle("m_{llbb} GeV")
graph.GetYaxis().SetTitle("Limits")
graph.SetLineColor(R.kBlack)
graph1.SetLineColor(R.kBlue)
graph.Draw("ALP*")
graph1.Draw("same,LP*")
legend = Legend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(graph,"Cut Based Limits", "l")
legend.AddEntry(graph1,"High Level Limits","l")
legend.Draw("same")
canvas.Print(extension+'TgraphLimitsCUTVTMVA.png')

canvas = Canvas()
graph = Graph(numbins,x,y,xes,xes,ydes,yues)
graph2 = Graph(numbins,x,y2,xes,xes,y2des,y2ues)
#graph = Graph(numbins,np.array(masses200),np.array(mediantmva),np.array(zeros),np.array(zeros),np.array(cutexl2),np.array(cutexh2))
graph.SetTitle("")
graph.GetXaxis().SetTitle("m_{llbb} GeV")
graph.GetYaxis().SetTitle("Limits")
graph.SetLineColor(R.kBlack)
graph2.SetLineColor(R.kRed)
graph.Draw("ALP*")
graph2.Draw("same,LP*")
legend = Legend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(graph,"Cut Based Limits", "l")
legend.AddEntry(graph2,"Low Level Limits","l")
legend.Draw("same")
canvas.Print(extension+'TgraphLimitsCUTVTMVALL.png')

canvas = Canvas()
graph = Graph(numbins,x,y,xes,xes,ydes,yues)
graph2 = Graph(numbins,x,y2,xes,xes,y2des,y2ues)
graph1 = Graph(numbins,x,y1,xes,xes,y1des,y1ues)
#graph = Graph(numbins,np.array(masses200),np.array(mediantmva),np.array(zeros),np.array(zeros),np.array(cutexl2),np.array(cutexh2))
graph.SetTitle("")
graph.GetXaxis().SetTitle("m_{llbb} GeV")
graph.GetYaxis().SetTitle("Limits")
graph.SetLineColor(R.kBlack)
graph1.SetLineColor(R.kBlue)
graph2.SetLineColor(R.kRed)
graph.Draw("ALP*")
graph1.Draw("same,LP*")
graph2.Draw("same,LP*")
legend = Legend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(graph,"Cut Based Limits","l")     #object, name printed, fill style
legend.AddEntry(graph1,"High Level Limits","l")     #object, name printed, fill style
legend.AddEntry(graph2,"Low Level Limits","l")     #object, name printed, fill style

legend.Draw("same")
canvas.Print(extension+'TotalLimits.png')

canvas = Canvas()
graph = Graph(numbins,x,y,xes,xes,ydes,yues)
graph1 = Graph(numbins,x,y1,xes,xes,y1des,y1ues)
#graph = Graph(numbins,np.array(masses200),np.array(mediantmva),np.array(zeros),np.array(zeros),np.array(cutexl2),np.array(cutexh2))
graph1.SetTitle("")
graph1.GetXaxis().SetTitle("m_{llbb} GeV")
graph1.GetYaxis().SetTitle("Limits")
graph1.SetLineColor(R.kBlack)
graph1.SetLineColor(R.kBlue)
graph1.Draw("ALP*")
legend = Legend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(graph1,"High Level Limits","l")
legend.Draw("same")
canvas.Print(extension+'HighLevelLimitsTGRAPH.png')

canvas = Canvas()
graph2 = Graph(numbins,x,y2,xes,xes,y2des,y2ues)
#graph = Graph(numbins,np.array(masses200),np.array(mediantmva),np.array(zeros),np.array(zeros),np.array(cutexl2),np.array(cutexh2))
graph2.SetTitle("")
graph2.GetXaxis().SetTitle("m_{llbb} GeV")
graph2.GetYaxis().SetTitle("Limits")
graph2.SetLineColor(R.kBlack)
graph2.SetLineColor(R.kRed)
graph2.Draw("ALP*")
legend = Legend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(graph2,"Low Level Limits","l")
legend.Draw("same")
canvas.Print(extension+'LowLevelLimitsTGRAPH.png')

canvas = Canvas()
graph2 = Graph(numbins,x,y2,xes,xes,y2des,y2ues)
graph1 = Graph(numbins,x,y1,xes,xes,y1des,y1ues)
#graph = Graph(numbins,np.array(masses200),np.array(mediantmva),np.array(zeros),np.array(zeros),np.array(cutexl2),np.array(cutexh2))
graph2.SetTitle("")
graph2.GetXaxis().SetTitle("m_{llbb} GeV")
graph2.GetYaxis().SetTitle("Limits")
graph1.SetLineColor(R.kBlue)
graph2.SetLineColor(R.kRed)
graph2.Draw("ALP*")
graph1.Draw("same,LP*")
legend = Legend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(graph1,"High Level Limits","l")     #object, name printed, fill style
legend.AddEntry(graph2,"Low Level Limits","l")     #object, name printed, fill style

legend.Draw("same")
canvas.Print(extension+'HighVSLowLimitsTGRAPH.png')















