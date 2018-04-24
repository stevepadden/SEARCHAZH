import matplotlib.pyplot as plt
#window = [-2sig,-1sig,median,+1sig,+2sig]


mh200_400 = [0.120306,0.161511,0.224147,0.312597,0.421683]
mh200_500 = [0.0476046,0.0639092,0.0886944,0.124471,0.169708]
mh200_600 = [0.0254089,0.0341114,0.0473405,0.0670678,0.0928832]
mh200_700 = [0.0144865,0.0194482,0.0269906,0.0388026,0.0551002]

masses200 = [400,500,600,700]

TMVA200_400 = [0.0415271,0.0557502,0.0773712,0.107765,0.144963]
TMVA200_500 = [0.01888616,0.0253218,0.0351421,0.0489744,0.0659551]
TMVA200_600 = [0.0102431,0.0137514,0.0190845,0.0266178,0.0359038]
TMVA200_700 = [0.00897852,0.0120537,0.0167283,0.0232874,0.0313087]


TMVALL200_400 = [0.0443517,0.0595422,0.0826337,0.115104,0.15486]
TMVALL200_500 = [0.0256231,0.0343991,0.0477397,0.0665071,0.0895756]
TMVALL200_600 = [0.0182768,0.0245367,0.0340525,0.0474728,0.0640033]
TMVALL200_700 = [0.0146657,0.0196888,0.0273244,0.038123,0.0514282]



window200 = [mh200_400,mh200_500,mh200_600,mh200_700]
windowTMVA = [TMVA200_400,TMVA200_500,TMVA200_600,TMVA200_700]
windowTMVALL = [TMVALL200_400,TMVALL200_500,TMVALL200_600,TMVALL200_700]
sig130_2min = []
sig130_1min = []
median130 = []
sig130_1plus = []
sig130_2plus = []







sig200_2min = []
sig200_1min = []
median200 = []
sig200_1plus = []
sig200_2plus = []

TMVA200_2min = []
TMVA200_1min = []
medianTMVA = []
TMVA200_1plus = []
TMVA200_2plus = []

TMVALL200_2min = []
TMVALL200_1min = []
medianTMVALL = []
TMVALL200_1plus = []
TMVALL200_2plus = []


for i,ii,iii in zip(window200,windowTMVA,windowTMVALL):
    sig200_2min.append(i[0])
    sig200_1min.append(i[1])
    median200.append(i[2])
    sig200_1plus.append(i[3])
    sig200_2plus.append(i[4])
    TMVA200_2min.append(ii[0])
    TMVA200_1min.append(ii[1])
    medianTMVA.append(ii[2])
    TMVA200_1plus.append(ii[3])
    TMVA200_2plus.append(ii[4])
    TMVALL200_2min.append(iii[0])
    TMVALL200_1min.append(iii[1])
    medianTMVALL.append(iii[2])
    TMVALL200_1plus.append(iii[3])
    TMVALL200_2plus.append(iii[4])

#plt.plot(masses200, sig200_2min, masses200, sig200_1min, masses200, median200, masses200, sig200_1plus, masses200,
#             sig200_2plus,linestyle = 'dashed',label = 'Cut Based') #colour = 'tab:red')
#plt.plot(masses200, TMVA200_2min, masses200, TMVA200_1min, masses200, median200, masses200, TMVA200_1plus, masses200,
#             TMVA200_2plus,linestyle = 'solid',label = 'TMVA')#color = 'tab:blue')
#plt.plot(masses200,TMVALL200_2min,masses200,TMVALL200_1min,masses200,medianTMVALL,masses200,TMVA200_1plus,masses200,TMVA200_2plus,linestyle = 'solid',label ='TMVALL')
plt.plot(masses200,sig200_2min,label = '2 min', linestyle = 'dotted')#, color = 'tab:')
plt.plot(masses200,sig200_1min,label = '1 min', linestyle = 'dashed')#, color = 'tab:red')
plt.plot(masses200,median200,label = 'median', linestyle = 'solid')#color = 'tab:red')
plt.plot(masses200,sig200_1plus,label = '1 plus', linestyle = 'dashed')#, color = 'tab:red')
plt.plot(masses200,sig200_2plus,label = '2 plus', linestyle = 'dotted')#, color = 'tab:red')



plt.legend()
plt.xlabel('Signal Mass $m_{A}$ GeV')
plt.title("Window 200")
plt.ylabel('Likelihood')
plt.savefig('MH200_Likelihood.png')
plt.show()
plt.show()

plt.close()

plt.plot(masses200,TMVA200_2min,label = '2 min', linestyle = 'dotted')#, color = 'tab:')
plt.plot(masses200,TMVA200_1min,label = '1 min', linestyle = 'dashed')#, color = 'tab:red')
plt.plot(masses200,medianTMVA,label = 'median', linestyle = 'solid')#color = 'tab:red')
plt.plot(masses200,TMVA200_1plus,label = '1 plus', linestyle = 'dashed')#, color = 'tab:red')
plt.plot(masses200,TMVA200_2plus,label = '2 plus', linestyle = 'dotted')#, color = 'tab:red')



plt.legend()
plt.xlabel('Signal Mass $m_A$ GeV')
plt.title("TMVA Window 200")
plt.ylabel('Likelihood')
plt.savefig('TMVA_Likelihood.png')
plt.show()
plt.show()

plt.close()

plt.plot(masses200,TMVALL200_2min,label = '2 min', linestyle = 'dotted')#, color = 'tab:')
plt.plot(masses200,TMVALL200_1min,label = '1 min', linestyle = 'dashed')#, color = 'tab:red')
plt.plot(masses200,medianTMVALL,label = 'median', linestyle = 'solid')#color = 'tab:red')
plt.plot(masses200,TMVALL200_1plus,label = '1 plus', linestyle = 'dashed')#, color = 'tab:red')
plt.plot(masses200,TMVALL200_2plus,label = '2 plus', linestyle = 'dotted')#, color = 'tab:red')



plt.legend()
plt.xlabel('Signal Mass $m_{A}$ GeV')
plt.title("TMVA Low Level Window 200")
plt.ylabel('Likelihood')
plt.savefig('TMVALL_Likelihood.png')
plt.show()
plt.show()

plt.close()


plt.plot(masses200,TMVA200_2min, linestyle = 'dotted' ,color = 'tab:blue')
plt.plot(masses200,TMVA200_1min, linestyle = 'dashed', color = 'tab:blue')
plt.plot(masses200,medianTMVA,label = 'High Level', linestyle = 'solid',color = 'tab:blue')
plt.plot(masses200,TMVA200_1plus, linestyle = 'dashed',color = 'tab:blue')
plt.plot(masses200,TMVA200_2plus,linestyle = 'dotted',color = 'tab:blue')

# plt.plot(masses200,TMVALL200_2min, linestyle = 'dotted' ,color = 'tab:green')
# plt.plot(masses200,TMVALL200_1min, linestyle = 'dashed', color = 'tab:green')
# plt.plot(masses200,medianTMVALL,label = 'Low Level', linestyle = 'solid',color = 'tab:green')
# plt.plot(masses200,TMVALL200_1plus, linestyle = 'dashed',color = 'tab:green')
# plt.plot(masses200,TMVALL200_2plus,linestyle = 'dotted',color = 'tab:green')


plt.plot(masses200,sig200_2min, linestyle = 'dotted' ,color = 'tab:red')
plt.plot(masses200,sig200_1min, linestyle = 'dashed', color = 'tab:red')
plt.plot(masses200,median200,label = 'Cut Based', linestyle = 'solid',color = 'tab:red')
plt.plot(masses200,sig200_1plus, linestyle = 'dashed',color = 'tab:red')
plt.plot(masses200,sig200_2plus,linestyle = 'dotted',color = 'tab:red')


plt.legend()
plt.xlabel('Signal Mass $m_{A}$ GeV')
plt.title("TMVA vs Cut Based Analysis Window 200")
plt.ylabel('Likelihood')
plt.savefig('TMVA_V_CUT_LIKELIHOOD.png')
plt.show()
plt.show()

plt.close()


plt.plot(masses200,TMVA200_2min, linestyle = 'dotted' ,color = 'tab:blue')
plt.plot(masses200,TMVA200_1min, linestyle = 'dashed', color = 'tab:blue')
plt.plot(masses200,medianTMVA,label = 'High Level', linestyle = 'solid',color = 'tab:blue')
plt.plot(masses200,TMVA200_1plus, linestyle = 'dashed',color = 'tab:blue')
plt.plot(masses200,TMVA200_2plus,linestyle = 'dotted',color = 'tab:blue')

plt.plot(masses200,TMVALL200_2min, linestyle = 'dotted' ,color = 'tab:green')
plt.plot(masses200,TMVALL200_1min, linestyle = 'dashed', color = 'tab:green')
plt.plot(masses200,medianTMVALL,label = 'Low Level', linestyle = 'solid',color = 'tab:green')
plt.plot(masses200,TMVALL200_1plus, linestyle = 'dashed',color = 'tab:green')
plt.plot(masses200,TMVALL200_2plus,linestyle = 'dotted',color = 'tab:green')


# plt.plot(masses200,sig200_2min, linestyle = 'dotted' ,color = 'tab:red')
# plt.plot(masses200,sig200_1min, linestyle = 'dashed', color = 'tab:red')
# plt.plot(masses200,median200,label = 'Low Level', linestyle = 'solid',color = 'tab:red')
# plt.plot(masses200,sig200_1plus, linestyle = 'dashed',color = 'tab:red')
# plt.plot(masses200,sig200_2plus,linestyle = 'dotted',color = 'tab:red')


plt.legend()
plt.xlabel('Signal Mass $m_{A}$ GeV')
plt.title("TMVA Low Level vs TMVA High Level Window 200")
plt.ylabel('Likelihood')
plt.savefig('Low_V_High_comparisson.png')
plt.show()
plt.show()

plt.close()



plt.plot(masses200,TMVA200_2min, linestyle = 'dotted' ,color = 'tab:blue')
plt.plot(masses200,TMVA200_1min, linestyle = 'dashed', color = 'tab:blue')
plt.plot(masses200,medianTMVA,label = 'High Level', linestyle = 'solid',color = 'tab:blue')
plt.plot(masses200,TMVA200_1plus, linestyle = 'dashed',color = 'tab:blue')
plt.plot(masses200,TMVA200_2plus,linestyle = 'dotted',color = 'tab:blue')

plt.plot(masses200,TMVALL200_2min, linestyle = 'dotted' ,color = 'tab:green')
plt.plot(masses200,TMVALL200_1min, linestyle = 'dashed', color = 'tab:green')
plt.plot(masses200,medianTMVALL,label = 'Low Level', linestyle = 'solid',color = 'tab:green')
plt.plot(masses200,TMVALL200_1plus, linestyle = 'dashed',color = 'tab:green')
plt.plot(masses200,TMVALL200_2plus,linestyle = 'dotted',color = 'tab:green')


plt.plot(masses200,sig200_2min, linestyle = 'dotted' ,color = 'tab:red')
plt.plot(masses200,sig200_1min, linestyle = 'dashed', color = 'tab:red')
plt.plot(masses200,median200,label = 'Low Level', linestyle = 'solid',color = 'tab:red')
plt.plot(masses200,sig200_1plus, linestyle = 'dashed',color = 'tab:red')
plt.plot(masses200,sig200_2plus,linestyle = 'dotted',color = 'tab:red')


plt.legend()
plt.xlabel('Signal Mass $m_{A}$ GeV')
plt.title("TMVA Low Level vs TMVA High Level Window 200")
plt.ylabel('Likelihood')
plt.savefig('FullLikleihood.png')
plt.show()
plt.show()

plt.close()










