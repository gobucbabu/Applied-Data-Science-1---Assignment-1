# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:10:02 2023

@author: gobub
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fn1(a, b, c):
    """ Function to plot a line plot using matplotlib.pyplot """
    plt.plot(a, b, label='Male', c='b')
    plt.plot(a, c, label='Female', c='g')
    plt.xlim(2000, 2019)
    plt.ylim(0, 30)
    plt.xlabel("Year")
    plt.ylabel("Number of deaths")
    plt.legend(loc='best')
    plt.show()


df1 = pd.read_excel("Male and female suicide rates india.xlsx") 

p = df1['Year']
q = df1['Male']
r = df1['Female']

fn1(p, q, r)
