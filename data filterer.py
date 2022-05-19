# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:27:32 2022

@author: jonat
"""

import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/jonat/Documents/universiteit/master vo/introduction into engineering research/Data filtered2.csv")


na_free = df.dropna(subset = ['ipaqtot1',	'stap_om_1_aantal', 'stap_om_2_aantal', 'stap_om_3_aantal', 'stap_om_4_aantal', 'stap_om_5_aantal', 	'stap_om_6_aantal',	'stap_om_7_aantal'
])

only_na = df[~df.index.isin(na_free.index)]

na_free.to_csv("C:/Users/jonat/Documents/universiteit/master vo/introduction into engineering research/Filtered data3.csv")
only_na.to_csv("C:/Users/jonat/Documents/universiteit/master vo/introduction into engineering research/NanData.csv")