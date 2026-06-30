#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:21:12 2028

@author: farshad.toosi
"""


 
import numpy as np
 
import random as rnd

   
 
def Q1():
    
    holiday = 1
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')

    subset = data[data[:, 7] == holiday]

    print ("Number of entries Holiday:\t", len(subset))

    print ("Mean", np.mean(subset[:, 15]))
    
    holiday = 0
    subset = data[data[:, 7] == holiday]

    print ("Number of entries Non-Holiday:\t ", len(subset))

    print ("Mean", np.mean(subset[:, 15]))
    



def Q2():
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')

    result = data[:, 13]>data[:, 14]
    
    result = data[result] # a new array that only contains the rows where casual users are greater than registered ones.
    percentage =  (len(result))/len(data)
    print ("Percentage of time where causal users > registered", percentage )


def Q3():
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')

    conditions = {1:"Clear", 2:"Misty", 3:"Light Rain", 4:"Heavy Rain"}

    for key in conditions:

         subsetData = data[data[:,8]==key]

         print (conditions[key],np.mean(subsetData[:, 15]))




def Q4():
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')
    for temp in range(1, 40, 5):

           # the temperature values stored in the array are multiplied by 41
          minValue = temp
          maxValue = temp+4
          
          higherTempCondition = (data[:,9]*41)>=minValue
    
          lowerTempCondition = (data[:,9]*41)<=maxValue
    
          subset = data[higherTempCondition & lowerTempCondition]
    
          meanValue = np.mean(subset[:, 13])
    
          print ("For temp in range ", minValue, "to", maxValue, " , mean  casual  is ", "{:.2f}".format(meanValue))


import pandas as pd


def Q5():
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')
    
    # Note, np.arange() by default generates inter values, but values type can be changed to string as below syntax.
    
    ind = np.array(np.arange(len(data)),str)
    
    
    d = pd.Series(data[:,13], index = ind)
    # Testing it below
    print(d['1030'])


def Q6():
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')
    
   
    # In this example you can see the benefit of duplicated labled indexes in pandas.
    
    d = pd.Series(data[:,9], index = data[:,1])
   
    print(np.mean(d[1]), np.mean(d[2]), np.mean(d[3]), np.mean(d[4]))
  

def Q7():
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')
    
   
    # In this example you can see the benefit of duplicated labled indexes in pandas.
    
    d = pd.Series(data[:,11], index = data[:,3])
   
    for i in range(12):
        print(np.mean(d[i+1]))
        



