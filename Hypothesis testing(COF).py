# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 00:38:10 2020

@author: Wellson
"""

import pandas as pd
import scipy
from scipy import stats
import statsmodels.api as sm

COF=pd.read_csv("C:/Users/Wellson/Documents/R/360/Hypothesis testing/CustomerOrderform.csv")
COF
COF.dtypes

obj_COF=COF.select_dtypes(include=['object']).copy()
obj_COF.head()

obj_COF[obj_COF.isnull().any(axis=1)]

obj_COF['Phillippines'].value_counts()
scipy.stats.binom_test(x=29,n=271)

obj_COF['Indonesia'].value_counts()
scipy.stats.binom_test(x=33,n=267,p=0.5)

obj_COF['Malta'].value_counts()
scipy.stats.binom_test(x=31,n=269,p=0.5)

obj_COF['India'].value_counts()
scipy.stats.binom_test(x=20,n=280,p=0.5)

