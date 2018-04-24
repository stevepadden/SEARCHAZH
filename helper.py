import ROOT as R
import numpy as np


# fill a histo from an array
def getHisto(hname, nbins, hmin, hmax, a):
    h = R.TH1F(hname,hname,nbins, hmin, hmax)
    for i in a:
        h.Fill(i)
    return h

# return the ROC curve
def roc(hs,hb):
    n = hs.GetNbinsX()
    g = R.TGraph()
    nsig = hs.Integral(0,n+1)
    nbkg = hb.Integral(0,n+1)
    for i in range(1,n):
        sigeff = hs.Integral(i,n+1)/nsig
        bkgeff = hb.Integral(i,n+1)/nbkg
        g.SetPoint(i-1,sigeff,1-bkgeff)
        if sigeff == 0:
            break
        #print 'DEBUG: ',i,sigeff, 1-bkgeff
    return g

# plot roc curves together
def rocPlot(vg, vstyle, vtitles,pname):
    c1 = R.TCanvas()
    g = vg[0]
    g.SetLineWidth(2)
    g.SetTitle("")
    g.GetXaxis().SetTitle("signal eff")
    g.GetYaxis().SetTitle("1- bkg eff")
    g.Draw("ALP")
    leg = R.TLegend(0.2,0.2,0.4,0.5)
    leg.AddEntry(g, vtitles[0],"l")
    for gi,i in zip(vg[1:],vstyle[1:]):
        gi.SetLineColor(i)
        gi.SetLineWidth(2)
        gi.Draw("L same")
    for gi,i in zip(vg[1:],vtitles[1:]):
        leg.AddEntry(gi, i,"l")
    leg.Draw("same")
    c1.Print(pname)


# plot 2 histos together
def plotter2(hsig,hbkg,xaxis,pname,yax=1.3, log=0):
    c = R.TCanvas()
    hsig.SetStats(0)
    hsig.SetTitle("")
    hsig.GetXaxis().SetTitle(xaxis)
    hsig.SetFillColor(2)
    theMax = max(hbkg.GetBinContent( hbkg.GetMaximumBin() ), hsig.GetBinContent( hsig.GetMaximumBin() ))
    if log>0:
        R.gPad.SetLogy()
    else:
        hsig.GetYaxis().SetRangeUser(0,theMax*yax)        
    leg = R.TLegend(0.5,0.7,0.9,0.9)
    leg.AddEntry(hsig,"Signal","f")
    leg.AddEntry(hbkg,"Background","l")
    hsig.Draw("HIST")
    hbkg.Draw("same")
    leg.Draw("same")
    c.Print(pname)


############################################
def plotInputVars(x_values, y_values,myvars, tag,log=0, w=[]):
    vh_min = []
    vh_max = []
    if len(w) == 0: # just put everything to 1
        w = [ 1 for i in range(len(x_values))  ]
    for v in myvars:
        vh_min.append(999999)
        vh_max.append(0)

    # find the min and max values
    for x0, y0 in zip(x_values, y_values):
        for i in range(0, len(x0)):
            if x0[i] > vh_max[i]:
                vh_max[i] = x0[i]
            if x0[i] < vh_min[i]:
                vh_min[i] = x0[i]
    #print vh_min, vh_max
    vh_hist_sig = []
    vh_hist_bkg = []
    for n, hmin, hmax in zip(myvars, vh_min, vh_max):
        hs = R.TH1F(n+"_sig", n+"_sig", 25, hmin*0.9, hmax*1.1)
        hb = R.TH1F(n+"_bkg", n+"_bkg", 25, hmin*0.9, hmax*1.1)
        vh_hist_sig.append(hs)
        vh_hist_bkg.append(hb)

    # fill them now
    i_sig, i_bkg = 0, 0
    #print y_values
    for x0, y0, w0 in zip(x_values, y_values, w):
        if y0[0] == 0:
            i_bkg += 1
            for i in range(0, len(vh_hist_bkg)):
                vh_hist_bkg[i].Fill(x0[i], w0)
        else:
            i_sig += 1
            for i in range(0, len(vh_hist_sig)):
                vh_hist_sig[i].Fill(x0[i], w0)

    print 'hists were filled; signal',i_sig,"bkg",i_bkg
    # now plot them
    print len(vh_hist_sig),len(vh_hist_bkg),len(myvars)        
    for hs, hb, n in zip(vh_hist_sig, vh_hist_bkg,myvars):
        hs.Scale(1./hs.Integral(0,999999))
        hb.Scale(1./hb.Integral(0,999999))
        print 'plotting histo ',n
        plotter2(hs,hb,n,"inputVar_"+tag+"_"+n, 1.5,log)
        
    return vh_min, vh_max


def scale_arrays(xin, v_min, v_max):
    i=0
    for xmin, xmax in zip(v_min,v_max):
        print 'scale var ',i,":",xmin," - ", xmax,"to 0 - 1"
        i += 1
        
    xout = []
    for x0 in xin:
        x0_norm = []
        for xx, xmin, xmax in zip(x0, v_min, v_max):
            x0_norm.append( (xx-xmin) / (xmax - xmin)  )
        xout.append(x0_norm)
    return np.array(xout)


    
