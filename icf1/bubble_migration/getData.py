# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import casefoam
import seaborn as sns
import numpy as np

def getMinMax(caseComb, time, currentDataFrame, axis=0):
    """Return the max, min and mean of the given axis.

    Axis argument can be given as keyword argument in posField_to_timeSeries
    .e.g (axis=1).

    """

    data = {"t":   [time],
            "min": [currentDataFrame.iloc[:, axis].min()],
            "max": [currentDataFrame.iloc[:, axis].max()]}
    df = pd.DataFrame(data)
    df = df.set_index('t')
    return df


cases = [['interFoam','interIsoFoam','interFlow']]

baseCase = 'Cases'
solutionDir = 'surfaceData'
file = 'p_freeSurf.raw'

# get the freesurface at 0.5 seconds
freeSurf = casefoam.positional_field(solutionDir, file,0.5,cases, baseCase)


# get min and max of the freesurface
freeSurf_min_max = casefoam.posField_to_timeSeries(solutionDir,file,getMinMax,cases,baseCase,axis=2)
freeSurf_min_max = freeSurf_min_max.reset_index("t")
freeSurf_min_max.columns = ["t","min","max","solver"]
freeSurf_min_max = freeSurf_min_max.sort_values("t")
freeSurf_min_max.to_csv("results/freeSurf_min_max.csv",index=False)


maxU = casefoam.time_series("maxU/0","volFieldValue.dat",cases,baseCase)
maxU = maxU.reset_index("t")
maxU.columns = ["t","U_x","U_y","U_z","solver"]
maxU["dt"] = maxU.groupby("solver")["t"].transform(lambda x: x.diff())
maxU = maxU.dropna(axis=0)
maxU.to_csv("results/maxU.csv",index=False)
