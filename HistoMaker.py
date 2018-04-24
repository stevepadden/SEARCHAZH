import ROOT as R
def Histogrammaker(x1, NameQUOTES, TitleQUOTES, Bins, LowerRange,UpperRange,inputdata,inputweight):  # A method that fills generic histograms when arguments passed properly
    x1 = R.TH1F(NameQUOTES, TitleQUOTES, Bins, LowerRange, UpperRange)  # x1 is the object name, all others are obvious arguments
    for i in range(len(inputdata)):
        (x1.Fill(inputdata[i],inputweight[i]))
    return x1  # we need to return from the method

def Draw (CanvasName,ObjectToBeDrawn,PointArgumentsQUOTES,LineArgumentsRdotkColour,ImageSaveNameQUOTES):
    x = PointArgumentsQUOTES
    y = LineArgumentsRdotkColour
    CanvasName = R.TCanvas()  # Making our hard work pay off! Set a new canvas
    ObjectToBeDrawn.Draw(x)  # "PE" Adds error bars
    ObjectToBeDrawn.SetLineColor(y)
    CanvasName.Print(ImageSaveNameQUOTES)
