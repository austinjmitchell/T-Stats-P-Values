#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:48:39 2023

@author: austinmitchell
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
#import seaborn as sns
from scipy import stats
import statistics as stat

data = pd.read_csv("FEV.csv")

d = pd.DataFrame(data)

male = d[d["Sex"] == 1]
girls = d[d["Sex"] == 0]

bins = [5, 9, 14, 19]
labels = ['5-9', '10-14', '15-19']

d['Age_Group'] = pd.cut(d['Age'], bins=bins, labels=labels, right=False)

for age_group in labels:
    male_data = d[(d['Sex'] == 1) & (d['Age_Group'] == age_group)]['FEV']
    female_data = d[(d['Sex'] == 0) & (d['Age_Group'] == age_group)]['FEV']

    t_stat, p_value = stats.ttest_ind(male_data, female_data, equal_var=False) 

    print(f"\nResults for Age Group {age_group}:")
    print(f"Mean FEV (Male): {male_data.mean()}")
    print(f"Mean FEV (Female): {female_data.mean()}")
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
    
bins = [10, 14, 19]
labels = ['10-14', '15-19']

d['Age_Group'] = pd.cut(d['Age'], bins=bins, labels=labels, right=False)
male = d[d["Sex"] == 1]
female = d[d["Sex"] == 0]
for age_group in labels:
    for gender in [0,1]:
        for smoker_status in [0, 1]:
            subgroup_data = d[(d['Age_Group'] == age_group) & (d['Sex'] == gender) & (d['Smoke'] == smoker_status)]['FEV']

            t_stat, p_value = stats.ttest_1samp(subgroup_data, d['FEV'].mean())

            print(f"\nResults for {age_group}-year-old {'male' if gender == 1 else 'female'} {'Smokers' if smoker_status == 1 else 'Nonsmokers'}:")
            print(f"Mean FEV: {subgroup_data.mean()}")
            print(f"T-statistic: {t_stat}")
            print(f"P-value: {p_value}")
