# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:10:02 2023

@author: gobub
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fn1(c1, c2, c3):
    """Function to plot a line plot using matplotlib.pyplot"""
    plt.figure(figsize=[14, 6])
    plt.plot(c1, c2, label='Male', c='b')
    plt.plot(c1, c3, label='Female', c='g')
    plt.xticks(range(2000, 2020, 2), fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlim(2000, 2019)
    plt.ylim(0, 30)
    plt.xlabel("Year", fontweight='bold', fontsize=20)
    plt.ylabel("Number of deaths \n per 100,000 population",
               fontweight='bold', fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.title(" Suicide rate in india  ",
              color='black', fontsize=40,
              fontweight='bold', fontname="Times New Roman")
    plt.grid(zorder=0)
    plt.savefig("Assignment 1 figure 1.png")
    plt.show() 
    

def fn2(x, c1):
    """Function to make a bar graph with multiple bars.
    Arguments: A dataframe with the bar plot categories as its index 
    and the column to plot the bars"""
    plt.figure(figsize=[19,7])
    plt.bar(x.index, x[c1], label="Deaths", width=.69, zorder=2)
    
    #labelling
    plt.title("Percentage of covid deaths by country",
              fontsize=38)
    plt.xlabel("Country", fontsize=25)
    plt.ylabel("Percentage of death", fontsize=25)
    plt.xticks( fontsize=18)
    plt.yticks( fontsize=18)
    
    
    # save the figure
    plt.savefig("Assignment 1 figure 2.png")
    plt.show()


def fn3(v, l):
    """Function to create Pie chart with 
    the values and labels as parameter"""
    
    
    plt.figure(figsize=[12, 10])
    plt.pie(v, labels=l, autopct='%1.1f%%', textprops={'fontsize':25})
    plt.title("Percentage of adults \n who identify as LGBTQ",
              fontweight='bold', fontsize=40)
    plt.savefig("Assignment 1 figure 3")
    plt.show()


df1 = pd.read_excel("Male and female suicide rates india.xlsx") 
fn1(df1['Year'], df1['Male'], df1['Female'])

df2 = pd.read_excel("Covid stat of 10 countries.xlsx", index_col="Country")
fn2(df2, "Percentages")

df3 = pd.read_excel("LGBTQ percentages among generations.xlsx")
piex = df3["Generation"].tolist()
fn3(df3[2021], piex) 
