import ROOT as R
location ='/home/steve/AZH_Files/AZH_master_student/'      #This object can be changed to alter the location the files are in
desire = 'NtupleMPhys/massMPhys'            #This object can also be changed, to change what file is referenced within the .root file
print ('Files should be in relative path: '+ location )
print ('From within the ROOT file, looking for tree in location: ' +desire)

GGA_MA230_MH130 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA230_mH130_llbb.a766.0.root','read')
ggA_MA230_MH130 = GGA_MA230_MH130.Get(desire)

GGA_MA250_MH130 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA250_mH130_llbb.a766.0.root','read')
ggA_MA250_MH130 = GGA_MA250_MH130.Get(desire)

GGA_MA250_MH150 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA250_mH150_llbb.a766.0.root','read')
ggA_MA250_MH150 = GGA_MA250_MH150.Get(desire)

GGA_MA300_MH130 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA300_mH130_llbb.a766.0.root','read')
ggA_MA300_MH130 = GGA_MA300_MH130.Get(desire)

GGA_MA300_MH150 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA300_mH150_llbb.a766.0.root','read')
ggA_MA300_MH150 = GGA_MA300_MH150.Get(desire)

GGA_MA300_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA300_mH200_llbb.a766.0.root','read')
ggA_MA300_MH200 = GGA_MA300_MH200.Get(desire)

GGA_MA350_MH250 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA350_mH250_llbb.a766.0.root','read')
ggA_MA350_MH250 = GGA_MA350_MH250.Get(desire)

GGA_MA400_MH130 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA400_mH130_llbb.a766.0.root','read')
ggA_MA400_MH130 = GGA_MA400_MH130.Get(desire)

GGA_MA400_MH150 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA400_mH150_llbb.a766.0.root','read')
ggA_MA400_MH150 = GGA_MA400_MH150.Get(desire)

GGA_MA400_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA400_mH200_llbb.a766.0.root','read')
ggA_MA400_MH200 = GGA_MA400_MH200.Get(desire)

GGA_MA400_MH250 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA400_mH250_llbb.a766.0.root','read')
ggA_MA400_MH250 = GGA_MA400_MH250.Get(desire)

GGA_MA400_MH300 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA400_mH300_llbb.a766.0.root','read')
ggA_MA400_MH300 = GGA_MA400_MH300.Get(desire)

GGA_MA430_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA430_mH200_llbb.a766.0.root','read')
ggA_MA430_MH200 = GGA_MA430_MH200.Get(desire)

GGA_MA460_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA460_mH200_llbb.a766.0.root','read')
ggA_MA460_MH200 = GGA_MA460_MH200.Get(desire)

GGA_MA500_MH130 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH130_llbb.a766.0.root','read')
ggA_MA500_MH130 = GGA_MA500_MH130.Get(desire)

#### WHAT ARE THESE? ###

GGA_MA500_MH150_1 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH150_llbb_LW05.a766.0.root')
ggA_MA500_MH150_1 = GGA_MA500_MH150_1.Get(desire)
GGA_MA500_MH150_2 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH150_llbb_LW10.a766.0.root')
ggA_MA500_MH150_2 = GGA_MA500_MH150_2.Get(desire)
GGA_MA500_MH150_3 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH150_llbb_LW20.a766.0.root')
ggA_MA500_MH150_3 = GGA_MA500_MH150_3.Get(desire)

#####???####

GGA_MA500_MH175 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH175_llbb.a766.0.root','read')
ggA_MA500_MH175 = GGA_MA500_MH175.Get(desire)

GGA_MA500_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH200_llbb.a766.0.root','read')
ggA_MA500_MH200 = GGA_MA500_MH200.Get(desire)

GGA_MA500_MH225 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH225_llbb.a766.0.root','read')
ggA_MA500_MH225 = GGA_MA500_MH225.Get(desire)

GGA_MA500_MH250 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH250_llbb.a766.0.root','read')
ggA_MA500_MH250 = GGA_MA500_MH250.Get(desire)

GGA_MA500_MH300 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH300_llbb.a766.0.root','read')
ggA_MA500_MH300 = GGA_MA500_MH300.Get(desire)

GGA_MA500_MH350 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH350_llbb.0.root','read')
ggA_MA500_MH350 = GGA_MA500_MH350.Get(desire)

GGA_MA500_MH400 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA500_mH400_llbb.a766.0.root','read')
ggA_MA500_MH400 = GGA_MA500_MH400.Get(desire)

GGA_MA530_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA530_mH200_llbb.a766.0.root','read')
ggA_MA530_MH200 = GGA_MA530_MH200.Get(desire)

GGA_MA560_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA560_mH200_llbb.a766.0.root','read')
ggA_MA560_MH200 = GGA_MA560_MH200.Get(desire)

GGA_MA600_MH130 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA600_mH130_llbb.a766.0.root','read')
ggA_MA600_MH130 = GGA_MA600_MH130.Get(desire)

GGA_MA600_MH150 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA600_mH150_llbb.a766.0.root','read')
ggA_MA600_MH150 = GGA_MA600_MH150.Get(desire)

GGA_MA600_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA600_mH200_llbb.a766.0.root','read')
ggA_MA600_MH200 = GGA_MA600_MH200.Get(desire)

GGA_MA600_MH250 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA600_mH250_llbb.a766.0.root','read')
ggA_MA600_MH250 = GGA_MA600_MH250.Get(desire)

GGA_MA600_MH300 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA600_mH300_llbb.a766.0.root','read')
ggA_MA600_MH300 = GGA_MA600_MH300.Get(desire)

GGA_MA600_MH400 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA600_mH400_llbb.a766.0.root','read')
ggA_MA600_MH400 = GGA_MA600_MH400.Get(desire)

GGA_MA600_MH450 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA600_mH450_llbb.0.root','read')
ggA_MA600_MH450 = GGA_MA600_MH450.Get(desire)

GGA_MA600_MH500 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA600_mH500_llbb.a766.0.root','read')
ggA_MA600_MH500 = GGA_MA600_MH500.Get(desire)

GGA_MA700_MH130 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA700_mH130_llbb.a766.0.root','read')
ggA_MA700_MH130 = GGA_MA700_MH130.Get(desire)

GGA_MA700_MH150 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA700_mH150_llbb.a766.0.root','read')
ggA_MA700_MH150 = GGA_MA700_MH150.Get(desire)

GGA_MA700_MH200 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA700_mH200_llbb.a766.0.root','read')
ggA_MA700_MH200 = GGA_MA700_MH200.Get(desire)

GGA_MA700_MH250 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA700_mH250_llbb.a766.0.root','read')
ggA_MA700_MH250 = GGA_MA700_MH250.Get(desire)

GGA_MA700_MH300 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA700_mH300_llbb.a766.0.root','read')
ggA_MA700_MH300 = GGA_MA700_MH300.Get(desire)

GGA_MA700_MH400 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA700_mH400_llbb.a766.0.root','read')
ggA_MA700_MH400 = GGA_MA700_MH400.Get(desire)

GGA_MA700_MH500 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA700_mH500_llbb.a766.0.root','read')
ggA_MA700_MH500 = GGA_MA700_MH500.Get(desire)

GGA_MA700_MH600 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA700_mH600_llbb.0.root','read')
ggA_MA700_MH600 = GGA_MA700_MH600.Get(desire)

GGA_MA800_MH130 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA800_mH130_llbb.0.root','read')
ggA_MA800_MH130 = GGA_MA800_MH130.Get(desire)

GGA_MA800_MH300 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA800_mH300_llbb.0.root','read')
ggA_MA800_MH300 = GGA_MA800_MH300.Get(desire)

GGA_MA800_MH500 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA800_mH500_llbb.a766.0.root','read')
ggA_MA800_MH500 = GGA_MA800_MH500.Get(desire)

GGA_MA800_MH700 = R.TFile(location+'FinalPlots.Z.ggA_AZH.ggA_mA800_mH700_llbb.0.root', 'read')
gga_MA800_MH700 = GGA_MA800_MH700.Get(desire)





ZZEEB_70 = R.TFile(location+'FinalPlots.Z.ZeeB_v221.MAXHTPTV0_70_BFilter.0.root', 'read')       #Next 8 lines fill for z->eeB
zzeeb_70 = ZZEEB_70.Get(desire)
ZZEEB_140 = R.TFile(location+'FinalPlots.Z.ZeeB_v221.MAXHTPTV70_140_BFilter.0.root', 'read')
zzeeb_140= ZZEEB_140.Get(desire)
ZZEEB_280= R.TFile(location+'FinalPlots.Z.ZeeB_v221.MAXHTPTV140_280_BFilter.0.root', 'read')
zzeeb_280= ZZEEB_280.Get(desire)
ZZEEB_500 = R.TFile(location+'FinalPlots.Z.ZeeC_v221.MAXHTPTV280_500_CFilterBVeto.0.root', 'read')
zzeeb_500= ZZEEB_500.Get(desire)

ZZEEC_70 = R.TFile(location+'FinalPlots.Z.ZeeC_v221.MAXHTPTV0_70_CFilterBVeto.0.root', 'read')      #Next 8 lines looking for Z -> eeC
zzeec_70= ZZEEC_70.Get(desire)
ZZEEC_140 = R.TFile(location+'FinalPlots.Z.ZeeC_v221.MAXHTPTV70_140_CFilterBVeto.0.root', 'read')
zzeec_140= ZZEEC_140.Get(desire)
ZZEEC_280 = R.TFile(location+'FinalPlots.Z.ZeeC_v221.MAXHTPTV140_280_CFilterBVeto.0.root', 'read')
zzeec_280= ZZEEC_280.Get(desire)
ZZEEC_500 = R.TFile(location+'FinalPlots.Z.ZeeC_v221.MAXHTPTV280_500_CFilterBVeto.0.root', 'read')
zzeec_500= ZZEEC_500.Get(desire)

ZZEE_HPT_500 = R.TFile(location+'FinalPlots.Z.ZeeHPT_v221.MAXHTPTV500_1000.0.root','read')
zzee_hpt_500 = ZZEE_HPT_500.Get(desire)
ZZEE_HPT_1000 = R.TFile(location+'FinalPlots.Z.ZeeHPT_v221.MAXHTPTV1000_E_CMS.0.root','read')
zzee_hpt_1000 = ZZEE_HPT_1000.Get(desire)

ZZEEL_70 = R.TFile(location+'FinalPlots.Z.ZeeL_v221.MAXHTPTV0_70_CVetoBVeto.0.root','read')
zzeel_70 = ZZEEL_70.Get(desire)
ZZEEL_140 = R.TFile(location+'FinalPlots.Z.ZeeL_v221.MAXHTPTV70_140_CVetoBVeto.0.root','read')
zzeel_140 = ZZEEL_140.Get(desire)
ZZEEL_280 = R.TFile(location+'FinalPlots.Z.ZeeL_v221.MAXHTPTV140_280_CVetoBVeto.0.root','read')
zzeel_280 = ZZEEL_280.Get(desire)
ZZEEL_500 = R.TFile(location+'FinalPlots.Z.ZeeL_v221.MAXHTPTV280_500_CVetoBVeto.0.root','read')
zzeel_500 = ZZEEL_500.Get(desire)

ZZMUMUB_70 = R.TFile(location+'FinalPlots.Z.ZmumuB_v221.MAXHTPTV0_70_BFilter.0.root','read')
zzmumub_70 = ZZMUMUB_70.Get(desire)
ZZMUMUB_140 = R.TFile(location+'FinalPlots.Z.ZmumuB_v221.MAXHTPTV70_140_BFilter.0.root','read')
zzmumub_140 = ZZMUMUB_140.Get(desire)
ZZMUMUB_280 = R.TFile(location+'FinalPlots.Z.ZmumuB_v221.MAXHTPTV140_280_BFilter.0.root','read')
zzmumub_280 = ZZMUMUB_280.Get(desire)
ZZMUMUB_500 = R.TFile(location+'FinalPlots.Z.ZmumuB_v221.MAXHTPTV280_500_BFilter.0.root','read')
zzmumub_500 = ZZMUMUB_500.Get(desire)

ZZMUMUC_70 = R.TFile(location+'FinalPlots.Z.ZmumuC_v221.MAXHTPTV0_70_CFilterBVeto.0.root','read')
zzmumuc_70 = ZZMUMUC_70.Get(desire)
ZZMUMUC_140 = R.TFile(location+'FinalPlots.Z.ZmumuC_v221.MAXHTPTV70_140_CFilterBVeto.0.root','read')
zzmumuc_140 = ZZMUMUC_140.Get(desire)
ZZMUMUC_280 = R.TFile(location+'FinalPlots.Z.ZmumuC_v221.MAXHTPTV140_280_CFilterBVeto.0.root','read')
zzmumuc_280 = ZZMUMUC_280.Get(desire)
ZZMUMUC_500 = R.TFile(location+'FinalPlots.Z.ZmumuC_v221.MAXHTPTV280_500_CFilterBVeto.0.root','read')
zzmumuc_500 = ZZMUMUC_500.Get(desire)

ZZMUMUHPT_500 = R.TFile(location+'FinalPlots.Z.ZmumuHPT_v221.MAXHTPTV500_1000.0.root','read')
zzmumuhpt_500 = ZZMUMUHPT_500.Get(desire)
ZZMUMUHPT_1000 = R.TFile(location+'FinalPlots.Z.ZmumuHPT_v221.MAXHTPTV1000_E_CMS.0.root','read')
zzmumuhpt_1000 = ZZMUMUHPT_1000.Get(desire)

ZZMUMUL_70 = R.TFile(location+'FinalPlots.Z.ZmumuL_v221.MAXHTPTV0_70_CVetoBVeto.0.root','read')
zzmumul_70 = ZZMUMUL_70.Get(desire)
ZZMUMUL_140 = R.TFile(location+'FinalPlots.Z.ZmumuL_v221.MAXHTPTV70_140_CVetoBVeto.0.root','read')
zzmumul_140 = ZZMUMUL_140.Get(desire)
ZZMUMUL_280 = R.TFile(location+'FinalPlots.Z.ZmumuL_v221.MAXHTPTV140_280_CVetoBVeto.0.root','read')
zzmumul_280 = ZZMUMUL_280.Get(desire)
ZZMUMUL_500 = R.TFile(location+'FinalPlots.Z.ZmumuL_v221.MAXHTPTV280_500_CVetoBVeto.0.root','read')
zzmumul_500 = ZZMUMUL_500.Get(desire)

ZZTAUTAUB = R.TFile(location+'FinalPlots.Z.ZtautauB_v221.0.root','read')
zztautaub = ZZTAUTAUB.Get(desire)
ZZTAUTAUC = R.TFile(location+'FinalPlots.Z.ZtautauC_v221.0.root','read')
zztautauc = ZZTAUTAUC.Get(desire)
ZZTAUTAUL = R.TFile(location+'FinalPlots.Z.ZtautauL_v221.0.root','read')
zztautaul = ZZTAUTAUL.Get(desire)

TTbar1 = R.TFile(location+'FinalPlots.Z.ttbar.410000.PwPyEG_P2012_ttbar.0.root', 'read')        #Getting TT bar files
ttbar1 = TTbar1.Get(desire)
DATA1 = R.TFile(location+'FinalPlots.Z.data15.0.root','read')
Data1 = DATA1.Get(desire)
DATA2 = R.TFile(location+'FinalPlots.Z.data16.0.root','read')
Data2 = DATA2.Get(desire)



Zjets = [zzee_hpt_500,zzee_hpt_1000,zzeeb_70,zzeeb_140,zzeeb_280,zzeeb_500,zzeec_70,zzeec_140,zzeec_280,zzeec_500,zzeel_70,zzeel_140,zzeel_280,zzeel_500,zzmumub_70,zzmumub_140,zzmumub_280,zzmumub_500,zzmumuc_70,zzmumuc_140,zzmumuc_280,zzmumuc_500,zzmumuhpt_500,zzmumuhpt_1000,zzmumul_70,zzmumul_140,zzmumul_280,zzmumul_500,zztautaub,]
TTbars = [ttbar1]
ggas = [ggA_MA230_MH130,ggA_MA250_MH130,ggA_MA250_MH150,ggA_MA300_MH130,ggA_MA300_MH150,ggA_MA300_MH200,ggA_MA300_MH200,ggA_MA350_MH250,ggA_MA400_MH130,ggA_MA400_MH150,ggA_MA400_MH200,ggA_MA400_MH250,ggA_MA400_MH300,ggA_MA430_MH200,ggA_MA460_MH200,ggA_MA500_MH130,ggA_MA500_MH175,ggA_MA500_MH200,ggA_MA500_MH225,ggA_MA500_MH250,ggA_MA500_MH300,ggA_MA500_MH350,ggA_MA530_MH200,ggA_MA560_MH200,ggA_MA600_MH130,ggA_MA600_MH150,ggA_MA600_MH200,ggA_MA600_MH250,ggA_MA600_MH300,ggA_MA600_MH200,ggA_MA600_MH450,ggA_MA600_MH500,ggA_MA700_MH130,ggA_MA700_MH150,ggA_MA700_MH200,ggA_MA700_MH250,ggA_MA700_MH300,ggA_MA700_MH200,ggA_MA700_MH500,ggA_MA700_MH600,ggA_MA800_MH130,ggA_MA800_MH300,ggA_MA800_MH500,gga_MA800_MH700]
gga400 =  ggA_MA400_MH200
gga500 =  ggA_MA500_MH200
gga600 =  ggA_MA600_MH200
gga700 =  ggA_MA700_MH200




GGA_MH200 = [gga400,gga500,gga600,gga700]
names200 = ['400','500','600','700']
colours200 = [R.kGreen, R.kGreen -3 , R.kGreen -6 , R.kGreen -9]
GGA_MH130 = [ggA_MA230_MH130,ggA_MA250_MH130,ggA_MA300_MH130,ggA_MA400_MH130,ggA_MA500_MH130,ggA_MA600_MH130,ggA_MA700_MH130,ggA_MA800_MH130]
names130 = ['230','250','300','400','500','600','700','800']
colours130 = [R.kGreen - 0 ,R.kGreen -1, R.kGreen -2,R.kGreen -3,R.kGreen-4,R.kGreen-5,R.kGreen-6,R.kGreen-7]




datas = [Data1,Data2]

