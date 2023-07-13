import powerxrd as xrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_sch():

    data = xrd.Data('./sample1.xy').importfile()
    chart = xrd.Chart(*data)

    chart.backsub(tol=1.0,show=True)
    chart.SchPeak(xrange=[18,22],show=True)
    plt.xlabel('2 $\\theta$')
    plt.title('backsub and Scherrer width calculation')
    plt.show()

test_sch()