# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:10:02 2023

@author: gobub
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
def fn1(c1, c2, c3):
     Function to plot a line plot using matplotlib.pyplot 
    plt.figure(figsize=[7.5, 3])
    plt.plot(c1, c2, label='Male', c='b')
    plt.plot(c1, c3, label='Female', c='g')
    plt.xticks(range(2000, 2020, 2))
    plt.xlim(2000, 2019)
    plt.ylim(0, 30)
    plt.xlabel("Year", fontweight='bold')
    plt.ylabel("Number of deaths \n per 100,000 population", fontweight='bold')
    plt.legend(loc='best')
    plt.title(" Suicide rate in india   ",
              color='black', fontsize=24,
              fontweight='bold', fontname="Times New Roman")
    plt.savefig("Assignment 1 figure 1.png")
    plt.show() 
    """
    
def fn2(x, c1, c2):
    """Function to make a bar graph with multiple bars"""
    xlen = len(df2.index)
    plt.bar(xlen, c1, label="Deaths", width=.05)
    #plt.bar(xlen+25, c2, label="Population")
    plt.xticks(x.tolist())
    plt.legend()
    plt.show()


"""
def fn3(v, l):
    Function to create Pie chart with 
    the values and labels as parameter
    
    
    plt.figure(figsize=[8,8])
    plt.pie(v, labels=l, autopct='%1.1f%%', textprops={'fontsize':18})
    plt.title("Percentage of adults \n who identify as LGBTQ",
              fontweight='bold', fontsize=30)
    
    plt.show()


df1 = pd.read_excel("Male and female suicide rates india.xlsx") 

fn1(df1['Year'], df1['Male'], df1['Female'])
"""

df2 = pd.read_excel("Covid death data of 10 countries.xlsx")
fn2(df2["Country"], df2["Deaths"], df2["Population"])

"""
df3 = pd.read_excel("LGBTQ percentages among generations.xlsx")
piex = df3["Generation"].tolist()
fn3(df3[2021], piex) """



