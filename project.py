import plotly.express as px
import numpy as np 
import csv 
import pandas as pd
def plotfigure(datapath):
    #with open(datapath) as f:
        #df = csv.DictReader(f)
    df = pd.read_csv(datapath)
    fig = px.scatter(df,x = "Days Present", y = "Marks In Percentage")
    fig.show()
def getdatasource(datapath):
    temperature=[]
    icecreamsales=[]
    with open(datapath) as f:
        df = csv.DictReader(f)
        for i in df:
            temperature.append(float(i["Marks In Percentage"]))
            icecreamsales.append(float(i["Days Present"]))
    return {"x":temperature,"y":icecreamsales}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datapath='marks.csv'
    datasource=getdatasource(datapath)
    findcorrelation(datasource)
    plotfigure(datapath)(datapath)

setup()