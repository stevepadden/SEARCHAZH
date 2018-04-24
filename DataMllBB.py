import ROOT as R
import numpy
from FileGetter import *
from array import array
Background = []
Backgroundweight = []
BackgroundJvar = []
BackgroundMBB = []
BackgroundZPT = []
Backgroundptll = []
BackgroundNBjets = []
Backgroundlep0pt = []
Backgroundlep0eta = []
Backgroundlep0m = []
Backgroundlep0phi = []
Backgroundbjet0pt = []
Backgroundbjet0eta= []
Backgroundbjet0m = []
Backgroundbjet0phi = []
Backgroundlep1pt = []
Backgroundlep1eta = []
Backgroundlep1m = []
Backgroundlep1phi = []
Backgroundbjet1pt = []
Backgroundbjet1eta= []
Backgroundbjet1m = []
Backgroundbjet1phi = []
Backgroundnumelecs = []
Datamllbb = []
Dataweight = []
DataJvar = []
DataMBB = []
DataZPT = []
Dataptll = []
DataNBjets = []
Datalep0pt = []
Datalep0eta = []
Datalep0m = []
Datalep0phi = []
Databjet0pt = []
Databjet0eta= []
Databjet0m = []
Databjet0phi = []
Datalep1pt = []
Datalep1eta = []
Datalep1m = []
Datalep1phi = []
Databjet1pt = []
Databjet1eta= []
Databjet1m = []
Databjet1phi = []
Datanumelecs = []






def TTSignals(x1):
    for t in x1:
        Vecl0 = R.TLorentzVector()
        Vecl1 = R.TLorentzVector()
        Vecl0.SetPtEtaPhiM(x1.lep0_pt, x1.lep0_eta, x1.lep0_phi, x1.lep0_m)
        Vecl1.SetPtEtaPhiM(x1.lep1_pt, x1.lep1_eta, x1.lep1_phi, x1.lep1_m)
        Vecb0 = R.TLorentzVector()
        Vecb1 = R.TLorentzVector()
        Vecb0.SetPtEtaPhiM(x1.bjet0_pt, x1.bjet0_eta, x1.bjet0_phi, x1.bjet0_m)
        Vecb1.SetPtEtaPhiM(x1.bjet1_pt, x1.bjet1_eta, x1.bjet1_phi, x1.bjet1_m)
        y = (Vecl0 + Vecl1 + Vecb0 + Vecb1).Mag()
        Background.append(y)
        Backgroundweight.append(x1.weight)
        BackgroundJvar.append(x1.Jvar)
        BackgroundMBB.append(x1.mass_mbb)
        BackgroundZPT.append(x1.ptll)
        BackgroundNBjets.append(x1.NBjets)
        Backgroundlep0pt.append(x1.lep0_pt)
        Backgroundlep0eta.append(x1.lep0_eta)
        Backgroundlep0m.append(x1.lep0_m)
        Backgroundlep0phi.append(x1.lep0_phi)
        Backgroundlep1pt.append(x1.lep1_pt)
        Backgroundlep1eta.append(x1.lep1_eta)
        Backgroundlep1m.append(x1.lep1_m)
        Backgroundlep1phi.append(x1.lep1_phi)
        Backgroundbjet0m.append(x1.bjet0_m)
        Backgroundbjet0pt.append(x1.bjet0_pt)
        Backgroundbjet0phi.append(x1.bjet0_phi)
        Backgroundbjet0eta.append(x1.bjet0_eta)
        Backgroundbjet1m.append(x1.bjet1_m)
        Backgroundbjet1pt.append(x1.bjet1_pt)
        Backgroundbjet1phi.append(x1.bjet1_phi)
        Backgroundbjet1eta.append(x1.bjet1_eta)

def ZJetSignals(x1):
    for t in x1:
        Vecl0 = R.TLorentzVector()
        Vecl1 = R.TLorentzVector()
        Vecl0.SetPtEtaPhiM(x1.lep0_pt, x1.lep0_eta, x1.lep0_phi, x1.lep0_m)
        Vecl1.SetPtEtaPhiM(x1.lep1_pt, x1.lep1_eta, x1.lep1_phi, x1.lep1_m)
        Vecb0 = R.TLorentzVector()
        Vecb1 = R.TLorentzVector()
        Vecb0.SetPtEtaPhiM(x1.bjet0_pt, x1.bjet0_eta, x1.bjet0_phi, x1.bjet0_m)
        Vecb1.SetPtEtaPhiM(x1.bjet1_pt, x1.bjet1_eta, x1.bjet1_phi, x1.bjet1_m)
        y = (Vecl0 + Vecl1 + Vecb0 + Vecb1).Mag()
        Background.append(y)
        Backgroundweight.append(x1.weight)
        BackgroundJvar.append(x1.Jvar)
        BackgroundMBB.append(x1.mass_mbb)
        BackgroundZPT.append(x1.ptll)
        BackgroundNBjets.append(x1.NBjets)
        Backgroundlep0pt.append(x1.lep0_pt)
        Backgroundlep0eta.append(x1.lep0_eta)
        Backgroundlep0m.append(x1.lep0_m)
        Backgroundlep0phi.append(x1.lep0_phi)
        Backgroundlep1pt.append(x1.lep1_pt)
        Backgroundlep1eta.append(x1.lep1_eta)
        Backgroundlep1m.append(x1.lep1_m)
        Backgroundlep1phi.append(x1.lep1_phi)
        Backgroundbjet0m.append(x1.bjet0_m)
        Backgroundbjet0pt.append(x1.bjet0_pt)
        Backgroundbjet0phi.append(x1.bjet0_phi)
        Backgroundbjet0eta.append(x1.bjet0_eta)
        Backgroundbjet1m.append(x1.bjet1_m)
        Backgroundbjet1pt.append(x1.bjet1_pt)
        Backgroundbjet1phi.append(x1.bjet1_phi)
        Backgroundbjet1eta.append(x1.bjet1_eta)

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
        Datamllbb.append(y)
        Dataweight.append(x1.weight)
        DataJvar.append(x1.Jvar)
        DataMBB.append(x1.mass_mbb)
        DataZPT.append(x1.ptll)
        DataNBjets.append(x1.NBjets)
        Datalep0pt.append(x1.lep0_pt)
        Datalep0eta.append(x1.lep0_eta)
        Datalep0m.append(x1.lep0_m)
        Datalep0phi.append(x1.lep0_phi)
        Datalep1pt.append(x1.lep1_pt)
        Datalep1eta.append(x1.lep1_eta)
        Datalep1m.append(x1.lep1_m)
        Datalep1phi.append(x1.lep1_phi)
        Databjet0m.append(x1.bjet0_m)
        Databjet0pt.append(x1.bjet0_pt)
        Databjet0phi.append(x1.bjet0_phi)
        Databjet0eta.append(x1.bjet0_eta)
        Databjet1m.append(x1.bjet1_m)
        Databjet1pt.append(x1.bjet1_pt)
        Databjet1phi.append(x1.bjet1_phi)
        Databjet1eta.append(x1.bjet1_eta)

Datatimer = 0.0
Datatimeleft = (len(datas))
for i in range (len(datas)):
    x = datas[i]
    Data(x)
    percent = (Datatimer/Datatimeleft)*100
    print (str(int(percent)) + '% of Data completed')
    Datatimer = Datatimer + 1
print len(Datamllbb)
print(len(Dataweight))

TTtimer = 0.0
TTtimeleft = (len(TTbars))
for i in range(len(TTbars)):
    x = TTbars[i]
    TTSignals(x)
    # Below is just the timer
    percent = (TTtimer / TTtimeleft) * 100
    print (str(int(percent)) + '% of TT completed')
    TTtimer = TTtimer + 1

Zjettimer = 0.0
Zjettimeleft = (len(Zjets))
for i in range(len(Zjets)):
    x = Zjets[i]
    ZJetSignals(x)
    # Below is just the timer
    percent = (Zjettimer / Zjettimeleft) * 100
    print (str(int(percent)) + '% of Zjet completed')
    Zjettimer = Zjettimer + 1

print(Background)






File = R.TFile("Data200.root","recreate")
Tree = R.TTree("background","tree title")



# create 1 dimensional float arrays (python's float datatype corresponds to c++ doubles)
# as fill variables
n = array('f',[0.])   #Declaring the arrayhs to be written
mbb = array('f',[0.])
jvar = array('f',[0.])
zpt = array('f',[0.])
weight = array('f',[0.])
numjets = array('f',[0.])
lep0pt = array('f',[0.])
lep0m = array('f',[0.])
lep0phi = array('f',[0.])
lep0eta = array('f',[0.])
bjet0m = array('f',[0.])
bjet0pt = array('f',[0.])
bjet0phi = array('f',[0.])
bjet0eta = array('f',[0.])
lep1pt = array('f',[0.])
lep1m = array('f',[0.])
lep1phi = array('f',[0.])
lep1eta = array('f',[0.])
bjet1m = array('f',[0.])
bjet1pt = array('f',[0.])
bjet1phi = array('f',[0.])
bjet1eta = array('f',[0.])
numelecs = array('f',[0.])




# create the branches and assign the fill-variables to them
Tree.Branch('Mllbb', n, 'Mllbb/F')    #fill the branch with the array in /F (float) style
Tree.Branch('Mbb',mbb,'Mbb/F')
Tree.Branch('Jvar',jvar,'Jvar/F')
Tree.Branch('Zpt',zpt,'Zpt/F')
Tree.Branch('Weight',weight,'Weight/F')
Tree.Branch('NumJets',numjets,'NumJets/F')
Tree.Branch('lep0m',lep0m,'lep0m/F')
Tree.Branch('lep0pt',lep0pt,'lep0pt/F')
Tree.Branch('lep0phi',lep0phi,'lep0phi/F')
Tree.Branch('lep0eta',lep0eta,'lep0eta/F')
Tree.Branch('bjet0m',bjet0m,'bjet0m/F')
Tree.Branch('bjet0pt',bjet0pt,'bjet0pt/F')
Tree.Branch('bjet0phi',bjet0phi,'bjet0phi/F')
Tree.Branch('bjet0eta',bjet0eta,'bjet0eta/F')
Tree.Branch('lep1m',lep1m,'lep1m/F')
Tree.Branch('lep1pt',lep1pt,'lep1pt/F')
Tree.Branch('lep1phi',lep1phi,'lep1phi/F')
Tree.Branch('lep1eta',lep1eta,'lep1eta/F')
Tree.Branch('bjet1m',bjet1m,'bjet1m/F')
Tree.Branch('bjet1pt',bjet1pt,'bjet1pt/F')
Tree.Branch('bjet1phi',bjet1phi,'bjet1phi/F')
Tree.Branch('bjet1eta',bjet1eta,'bjet1eta/F')
Tree.Branch('NumElecs',numelecs,'NumElecs/F')


#t.Branch('uniform', u, 'uniform/D')
for i in range(len(Background)):
    n[0] = Background[i]                               			#Fill the actual arrays
    mbb[0] = BackgroundMBB[i]
    jvar[0] = BackgroundJvar[i]
    zpt[0] = BackgroundZPT[i]
    weight[0] = Backgroundweight[i]
    lep0m[0]=Backgroundlep0m[i]
    lep0eta[0] = Backgroundlep0eta[i]
    lep0phi [0] = Backgroundlep0phi[i]
    lep0pt[0] = Backgroundlep0pt[i]
    bjet0m[0]=Backgroundbjet0m[i]
    bjet0eta[0] = Backgroundbjet0eta[i]
    bjet0phi [0] = Backgroundbjet0phi[i]
    bjet0pt[0] = Backgroundbjet0pt[i]
    lep1m[0]=Backgroundlep1m[i]
    lep1eta[0] = Backgroundlep1eta[i]
    lep1phi [0] = Backgroundlep1phi[i]
    lep1pt[0] = Backgroundlep1pt[i]
    bjet1m[0]=Backgroundbjet1m[i]
    bjet1eta[0] = Backgroundbjet1eta[i]
    bjet1phi [0] = Backgroundbjet1phi[i]
    bjet1pt[0] = Backgroundbjet1pt[i]
    #numelecs[0] = Backgroundnumelecs[i]
    Tree.Fill()
File.Write()
File.Close()

def Signalwriter(SignalVARIABLE,nameSTRING):
    sig_Mllbb = []
    sig_weight = []
    sig_Jvar = []
    sig_MBB = []
    sig_ZPT = []
    sig_NBjets = []
    sig_lep0pt = []
    sig_lep0eta = []
    sig_lep0m = []
    sig_lep0phi = []
    sig_bjet0pt = []
    sig_bjet0eta = []
    sig_bjet0m = []
    sig_bjet0phi = []
    sig_lep1pt = []
    sig_lep1eta = []
    sig_lep1m = []
    sig_lep1phi = []
    sig_bjet1pt = []
    sig_bjet1eta = []
    sig_bjet1m = []
    sig_bjet1phi = []
    sig_numelecs = []



    File= R.TFile('Data200.root','update')
    sigarray = array('f',[0.])
    mbb = array('f', [0.])
    jvar = array('f', [0.])
    zpt = array('f', [0.])
    weight = array('f', [0.])
    numjets = array('f', [0.])
    lep0pt = array('f', [0.])
    lep0m = array('f', [0.])
    lep0phi = array('f', [0.])
    lep0eta = array('f', [0.])
    bjet0m = array('f', [0.])
    bjet0pt = array('f', [0.])
    bjet0phi = array('f', [0.])
    bjet0eta = array('f', [0.])
    lep1pt = array('f', [0.])
    lep1m = array('f', [0.])
    lep1phi = array('f', [0.])
    lep1eta = array('f', [0.])
    bjet1m = array('f', [0.])
    bjet1pt = array('f', [0.])
    bjet1phi = array('f', [0.])
    bjet1eta = array('f', [0.])
    numelecs = array('f', [0.])

    Tree = R.TTree("signal","tree title")
    Tree.Branch('Mllbb',sigarray,'Mllbb/F')
    Tree.Branch('Mbb', mbb, 'Mbb/F')
    Tree.Branch('Jvar', jvar, 'Jvar/F')
    Tree.Branch('Zpt', zpt, 'Zpt/F')
    Tree.Branch('Weight', weight, 'Weight/F')
    Tree.Branch('NumJets', numjets, 'NumJets/F')
    Tree.Branch('lep0m', lep0m, 'lep0m/F')
    Tree.Branch('lep0pt', lep0pt, 'lep0pt/F')
    Tree.Branch('lep0phi', lep0phi, 'lep0phi/F')
    Tree.Branch('lep0eta', lep0eta, 'lep0eta/F')
    Tree.Branch('bjet0m', bjet0m, 'bjet0m/F')
    Tree.Branch('bjet0pt', bjet0pt, 'bjet0pt/F')
    Tree.Branch('bjet0phi', bjet0phi, 'bjet0phi/F')
    Tree.Branch('bjet0eta', bjet0eta, 'bjet0eta/F')
    Tree.Branch('lep1m', lep1m, 'lep1m/F')
    Tree.Branch('lep1pt', lep1pt, 'lep1pt/F')
    Tree.Branch('lep1phi', lep1phi, 'lep1phi/F')
    Tree.Branch('lep1eta', lep1eta, 'lep1eta/F')
    Tree.Branch('bjet1m', bjet1m, 'bjet1m/F')
    Tree.Branch('bjet1pt', bjet1pt, 'bjet1pt/F')
    Tree.Branch('bjet1phi', bjet1phi, 'bjet1phi/F')
    Tree.Branch('bjet1eta', bjet1eta, 'bjet1eta/F')
    Tree.Branch('numelecs',numelecs,'numelecs/F')


    for i in SignalVARIABLE:
        Vecl0 = R.TLorentzVector()
        Vecl1 = R.TLorentzVector()
        Vecl0.SetPtEtaPhiM(i.lep0_pt, i.lep0_eta, i.lep0_phi, i.lep0_m)
        Vecl1.SetPtEtaPhiM(i.lep1_pt, i.lep1_eta, i.lep1_phi, i.lep1_m)
        Vecb0 = R.TLorentzVector()
        Vecb1 = R.TLorentzVector()
        Vecb0.SetPtEtaPhiM(i.bjet0_pt, i.bjet0_eta, i.bjet0_phi, i.bjet0_m)
        Vecb1.SetPtEtaPhiM(i.bjet1_pt, i.bjet1_eta, i.bjet1_phi, i.bjet1_m)
        y = (Vecl0 + Vecl1 + Vecb0 + Vecb1).Mag()
        sig_Mllbb.append(y)
        sig_weight.append(i.weight)
        sig_Jvar.append(i.Jvar)
        sig_MBB.append(i.mass_mbb)
        sig_ZPT.append(i.ptll)
        sig_NBjets.append(i.NBjets)
        sig_lep0pt.append(i.lep0_pt)
        sig_lep0eta.append(i.lep0_eta)
        sig_lep0m.append(i.lep0_m)
        sig_lep0phi.append(i.lep0_phi)
        sig_lep1pt.append(i.lep1_pt)
        sig_lep1eta.append(i.lep1_eta)
        sig_lep1m.append(i.lep1_m)
        sig_lep1phi.append(i.lep1_phi)
        sig_bjet0m.append(i.bjet0_m)
        sig_bjet0pt.append(i.bjet0_pt)
        sig_bjet0phi.append(i.bjet0_phi)
        sig_bjet0eta.append(i.bjet0_eta)
        sig_bjet1m.append(i.bjet1_m)
        sig_bjet1pt.append(i.bjet1_pt)
        sig_bjet1phi.append(i.bjet1_phi)
        sig_bjet1eta.append(i.bjet1_eta)
        sig_numelecs.append(i.nElecs)

    for i in range(len(sig_Mllbb)):
        sigarray[0] = sig_Mllbb[i]
        mbb[0] = sig_MBB[i]
        jvar[0] = sig_Jvar[i]
        zpt[0] = sig_ZPT[i]
        weight[0] = sig_weight[i]
        weight[0] = sig_weight[i]
        lep0m[0] = sig_lep0m[i]
        lep0eta[0] = sig_lep0eta[i]
        lep0phi[0] = sig_lep0phi[i]
        lep0pt[0] = sig_lep0pt[i]
        bjet0m[0] = sig_bjet0m[i]
        bjet0eta[0] = sig_bjet0eta[i]
        bjet0phi[0] = sig_bjet0phi[i]
        bjet0pt[0] = sig_bjet0pt[i]
        lep1m[0] = sig_lep1m[i]
        lep1eta[0] = sig_lep1eta[i]
        lep1phi[0] = sig_lep1phi[i]
        lep1pt[0] = sig_lep1pt[i]
        bjet1m[0] = sig_bjet1m[i]
        bjet1eta[0] = sig_bjet1eta[i]
        bjet1phi[0] = sig_bjet1phi[i]
        bjet1pt[0] = sig_bjet1pt[i]
        #numelecs[0] = sig_numelecs[i]
        Tree.Fill()
    File.Write()
    File.Close()


File= R.TFile('Data200.root','update')
Tree = R.TTree("Data","tree title")

datamllbb = array('f',[0.])
dataweight = array('f',[0.])
datambb = array('f',[0.])
datajvar = array('f',[0.])
datazpt = array('f',[0.])
datanumjets = array('f',[0.])
datalep0m = array('f',[0.])
datalep0pt = array('f',[0.])
datalep0phi = array('f',[0.])
datalep0eta = array('f',[0.])
datalep1m = array('f',[0.])
datalep1pt = array('f',[0.])
datalep1phi = array('f',[0.])
datalep1eta = array('f',[0.])
databjet0m = array('f',[0.])
databjet0pt = array('f',[0.])
databjet0phi = array('f',[0.])
databjet0eta = array('f',[0.])
databjet1m = array('f',[0.])
databjet1pt = array('f',[0.])
databjet1phi = array('f',[0.])
databjet1eta = array('f',[0.])
datanumelecs = array('f',[0.])


Tree.Branch('Mllbb', datamllbb, 'Mllbb/F')    #fill the branch with the array in /F (float) style
Tree.Branch('Weight',dataweight,'Weight/F')
Tree.Branch('Mbb', datambb, 'Mbb/F')
Tree.Branch('Jvar', datajvar, 'Jvar/F')
Tree.Branch('Zpt', datazpt, 'Zpt/F')
Tree.Branch('NumJets', datanumjets, 'NumJets/F')
Tree.Branch('lep0m', datalep0m, 'lep0m/F')
Tree.Branch('lep0pt', datalep0pt, 'lep0pt/F')
Tree.Branch('lep0phi', datalep0phi, 'lep0phi/F')
Tree.Branch('lep0eta', datalep0eta, 'lep0eta/F')
Tree.Branch('bjet0m', databjet0m, 'bjet0m/F')
Tree.Branch('bjet0pt', databjet0pt, 'bjet0pt/F')
Tree.Branch('bjet0phi', databjet0phi, 'bjet0phi/F')
Tree.Branch('bjet0eta', databjet0eta, 'bjet0eta/F')
Tree.Branch('lep1m', datalep1m, 'lep1m/F')
Tree.Branch('lep1pt', datalep1pt, 'lep1pt/F')
Tree.Branch('lep1phi', datalep1phi, 'lep1phi/F')
Tree.Branch('lep1eta', datalep1eta, 'lep1eta/F')
Tree.Branch('bjet1m', databjet1m, 'bjet1m/F')
Tree.Branch('bjet1pt', databjet1pt, 'bjet1pt/F')
Tree.Branch('bjet1phi', databjet1phi, 'bjet1phi/F')
Tree.Branch('bjet1eta', databjet1eta, 'bjet1eta/F')
Tree.Branch('numelecs', datanumelecs, 'numelecs/F')

for i in range(len(Datamllbb)):
    datamllbb[0] = Datamllbb[i]                               			#Fill the actual arrays
    dataweight[0] = Dataweight[i]
    datambb[0] = DataMBB[i]
    datajvar[0] = DataJvar[i]
    datazpt[0] = DataZPT[i]
    datanumjets[0] = DataNBjets[i]
    datalep0m[0]=Datalep0m[i]
    datalep0pt[0] = Datalep0pt[i]
    datalep0eta[0] = Datalep0eta[i]
    datalep0phi[0]=Datalep0phi[i]
    datalep1m[0]=Datalep1m[i]
    datalep1pt[0] = Datalep1pt[i]
    datalep1eta[0] = Datalep1eta[i]
    datalep1phi[0]=Datalep1phi[i]
    databjet0m[0]=Databjet0m[i]
    databjet0pt[0] = Databjet0pt[i]
    databjet0eta[0] = Databjet0eta[i]
    databjet0phi[0]=Databjet0phi[i]
    databjet1m[0]=Databjet1m[i]
    databjet1pt[0] = Databjet1pt[i]
    databjet1eta[0] = Databjet1eta[i]
    databjet1phi[0]=Databjet1phi[i]

    Tree.Fill()
File.Write()
File.Close()





ggtimer = 0.0  # Has to be non integer
ggtimeleft = (len(GGA_MH200))


x = GGA_MH200[0]
Signalwriter(x, names200[0])

# Below is just the timer
percent = (ggtimer / ggtimeleft) * 100
print (str(int(percent)) + '% of GG completed')
ggtimer = ggtimer + 1



