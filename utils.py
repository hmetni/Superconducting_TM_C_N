## Useful Python functions

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import pchip_interpolate
import seaborn as sns


def plot_series(df, series, left=None, right=None, label=None, color=None, marker=None):
    series_df = df[df['elements']==series]
    composition = series_df['perc_1_in_2'].tolist()
    Tc = series_df['Tc'].tolist()
    if left is not None:
        composition.insert(0,0)
        Tc.insert(0,left)
    if right is not None:
        composition.insert(len(composition),1)
        Tc.insert(len(Tc),right)
    sns.scatterplot(x=composition, y=Tc, color=color, marker=marker,label=label, s=75)
    xnew = np.linspace(min(composition), max(composition), 50)
    #f = make_interp_spline(np.array(composition), Tc, k=2)  # type: BSpline
    #f = CubicHermiteSpline(np.array(composition), Tc, dydx=)
    smooth = pchip_interpolate(np.array(composition),Tc, xnew)
    #power_smooth = f(xnew)
    plt.plot(xnew, smooth, color=color, alpha=0.15)

