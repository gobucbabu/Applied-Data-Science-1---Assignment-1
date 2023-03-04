# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:10:02 2023

@author: gobub
"""

import pandas as pd
import matplotlib.pyplot as plt


def PlotLineGraph(df, c1, c2, c3):
    """Function plotting a line plot using matplotlib.pyplot. Arguments:
    The dataframe.
    The columns to be plotted in the line graph.
    """

    plt.figure(figsize=[14, 6])

    # plotting
    plt.plot(df[c1], df[c2], label='Male', c='b')
    plt.plot(df[c1], df[c3], label='Female', c='g')
    plt.xticks(range(2000, 2020, 2), fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlim(2000, 2019)
    plt.ylim(0, 30)

    # labelling
    plt.xlabel("Year", fontweight='bold', fontsize=20)
    plt.ylabel("Number of deaths \n per 100,000 population",
               fontweight='bold', fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.title(" Suicide rate in india  ",
              color='black', fontsize=40,
              fontweight='bold', fontname="Times New Roman")
    plt.grid(zorder=0)

    # save as png
    plt.savefig("Assignment 1 figure 1.png")

    plt.show()

    return


def PlotBarGraph(x, c1):
    """Function to make a bar graph with multiple bars. Arguments:
    A dataframe with the bar plot categories as its index
    The column plotting the bars with.
    """

    plt.figure(figsize=[19, 7])

    # plotting
    plt.bar(x.index, x[c1], label="Deaths", width=.69, zorder=2)

    # labelling
    plt.title("Percentage of covid deaths by country",
              fontsize=38, fontname="Times New Roman",
              fontweight='bold')
    plt.xlabel("Country", fontsize=25)
    plt.ylabel("Percentage of death", fontsize=25)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)

    # save as png
    plt.savefig("Assignment 1 figure 2.png")

    plt.show()

    return


def PlotPieChart(v, lst):
    """Function to create Pie chart with the values and labels as parameter.
    Arguments:
    The dataframe column with which the pie chart is to be plotted.
    The list containing the labels.
    """

    plt.figure(figsize=[12, 10])

    # plotting
    plt.pie(v, labels=lst, autopct='%1.1f%%', textprops={'fontsize': 25})

    # labeling
    plt.title("Share of adults \n who identify as LGBTQ",
              fontweight='bold', fontsize=40, fontname="Times New Roman")

    # save as png
    plt.savefig("Assignment 1 figure 3")

    plt.show()

    return


# creating the dataframes with pandas
df1 = pd.read_excel("Male and female suicide rates india.xlsx")
df2 = pd.read_excel("Covid stat of 10 countries.xlsx", index_col="Country")
df3 = pd.read_excel("LGBTQ percentages among generations.xlsx")

# calling the functions
PlotLineGraph(df1, 'Year', 'Male', 'Female')

PlotBarGraph(df2, "Percentages")

piex = df3["Generation"].tolist()
PlotPieChart(df3[2021], piex)
