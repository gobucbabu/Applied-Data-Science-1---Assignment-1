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
    plt.figure(figsize=[4.3, 2.5])
    plt.plot(a, b, label='Male', c='b')
    plt.plot(a, c, label='Female', c='g')
    plt.xlim(2000, 2019)
    plt.ylim(0, 30)
    plt.xlabel("Year", fontweight='bold')
    plt.ylabel("Number of deaths", fontweight='bold')
    plt.legend(loc='best')
    plt.title("Suicide rate in india  ",
              fontstyle='italic', color='red', fontsize=15,
              fontweight='bold')
    plt.savefig("Assignment 1 figure 1.png")
    plt.show()
    
#Age standardized suicide rates \n (per 100,000 population)

df1 = pd.read_excel("Male and female suicide rates india.xlsx") 

p = df1['Year']
q = df1['Male']
r = df1['Female']

fn1(p, q, r)
