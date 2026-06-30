#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  16 09:21:12 2024

@author: farshad.toosi
"""


 

import pandas as pd
import numpy as np

def Q1():
    # he encoding="ISO-8859-1" (also known as Latin-1) is used in pandas.read_csv() when reading CSV files that contain characters encoded using this specific encoding.
    df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")
    locs = df['Location'].value_counts()
    print(type(locs))
    # Head will give a number of items from the top of the dataframe or Series.
    print(locs.head(1))
    
#Q1()
def Q2():
    df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")
    #Note any row is a type of shark attack.
    locs = df['Country'].value_counts()
    print(type(locs))
    print(locs.head(6))
#Q2()

def Q3():
    df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")
    
    print(pd.unique(df["Fatal"]))
    criteria1 = df["Fatal"]=='Y'
    countries_fatal= df[criteria1]
    locs = countries_fatal['Country'].value_counts()
    
    print(locs.head(6))    
#Q3()

def Q4():
    df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")
    boolSurfAttacks = df["Activity"] == "Surfing"
    boolScubaAttacks = df["Activity"] == "Scuba diving"    
    
    print ("Number of attacks when surfing ", len(  df [boolSurfAttacks] ))    
    print ("Number of attacks when Scuba Diving ", len(df[boolScubaAttacks]))
#Q4()
def Q5():
    df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")
    Fatals = df["Fatal"]=='Y'
    Fatal_Rows= df[Fatals]
    print(len(Fatal_Rows)*100/len(df))    
#Q5()
def Q6():
    df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")
    countries =  pd.unique(df["Country"])
    # Since the number of countries is limited (it wont increase the number of rows grow up..) therefore it is OK to use for loop
    for c in countries:
        country = df['Country'] == c
        fatal = df["Fatal"]=='Y'
        Non_Fatal = df["Fatal"]=='N'
        
        country_fatal = df[country & fatal]
        country_Non_Fatal = df[country & Non_Fatal]
        if len(country_fatal) > 0 and len(country_Non_Fatal) > 0  :
            print(f'The percentage of fatal attacks: ',c, len(country_fatal)*100/(len(country_fatal)+len(country_Non_Fatal)))  

#Q6()



def Q7(country):
    df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")
    
    countryBool = df['Country'] == country
    
    for yr in pd.unique(df['Year']):
        if yr>1924 and yr<2016:
            yeahBool = df['Year'] == yr
            countryYear = df[countryBool & yeahBool]
            print()
            print(country, yr, len(countryYear))
        
#Q7('AUSTRALIA')
    
def Q8():
    
    df = pd.read_csv("titanic.csv")
    # You can first see the unique values of Embarked column and then decide how to clean them...
    print(pd.unique(df['Embarked']))
    df['Embarked'][df['Embarked']=='C'] = 'Cherbourg'
    df['Embarked'][df['Embarked']=='Q'] = 'Cobh'
    df['Embarked'][df['Embarked']=='q1'] = 'Cobh'
    df['Embarked'][df['Embarked']=='q2'] = 'Cobh'
    
    df['Embarked'][df['Embarked']=='S'] = 'Southampton'
    
    #print(df)
    df.to_csv('titanic_new1.csv')
#Q8()
def Q9():
    
    df = pd.read_csv("titanic.csv")
    
    females = df[df['Sex']== "female"]
    
    females1 = females[females['Pclass']== 1]
    females2 = females[females['Pclass']== 2]
    females3 = females[females['Pclass']== 3]
    
    males = df[df['Sex']== "male"]
    
    males1 = males[males['Pclass']== 1]
    males2 = males[males['Pclass']== 2]
    males3 = males[males['Pclass']== 3]
    
    newDf = females3.sort_values(['Age'], ascending = [False])
    newDf = pd.concat([newDf, females2.sort_values(['Age'], ascending = [False])])
    newDf = pd.concat([newDf, females1.sort_values(['Age'], ascending = [False])])
    newDf = pd.concat([newDf, males3.sort_values(['Age'], ascending = [False])])
    newDf = pd.concat([newDf, males2.sort_values(['Age'], ascending = [False])])
    newDf = pd.concat([newDf, males1.sort_values(['Age'], ascending = [False])])
    newDf.to_csv('titanic_new.csv')
#Q9()
    
def Q10():
    # Part one 
    df = pd.read_csv("titanic.csv", index_col=1)

    print(np.mean(df['Age'][1]))
    print(np.mean(df['Age'][2]))
    print(np.mean(df['Age'][3]))
    
    # Part two
    df = pd.read_csv("titanic.csv")
    ClassGroups = df.groupby('Pclass')
    print(ClassGroups['Age'].mean())
Q10()
