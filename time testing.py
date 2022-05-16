# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 10:24:40 2022

@author: hridh
"""

import pandas as pd
import matplotlib as mp

df = pd.read_csv("BTI-FRM-700 - Test Report Index - Rev B - Notes_Based.csv")
headers = df.iloc[0]
new_data = pd.DataFrame(df.values[1:], columns=headers)

df2 = pd.read_csv("BTI-FRM-700 - Test Report Index - Rev B - Test#_Based.csv")
headers2 = df2.iloc[0]
new2_data = pd.DataFrame(df2.values[1:], columns=headers2)

df3 = pd.read_csv("BTI-FRM-700 - Test Report Index - Rev B - Test#_Based - 2021.csv")
headers3 = df3.iloc[0]
new3_data = pd.DataFrame(df3.values[1:], columns=headers3)



data = new_data[['Date','Notes']]
data2 = new2_data[['Test#','Date','Notes']]
data3 = new3_data[['Test#','Date','Notes']]
# print(note_col.count())
# chosenwords = re.compile('Tensile ') 

# data = note_col.dropna(subset=['Notes'])
# print(data.count())

start_date = '01-01-2020'
end_date = '12-31-2020'

##############################################################################

#                       2020
#                       2020
#                       2020

##############################################################################

##############################################################################

#                       Notes Based

##############################################################################


Powder_tests = data.loc[data['Notes'].str.contains("Powder", case=False, na=False)]
Powder2020 = Powder_tests.count()[0]

mask = (data['Date'] > start_date) & (data['Date'] <= end_date)
# THIS WILL CATCH VALUES THAT HAVE POWDER CHEMISTRY AS WELL
# CREATE AN EXCEPTION

Chemistry_tests = data.loc[data['Notes'].str.contains("Chemistry", case=False, na=False)]
Chem2020 = Chemistry_tests.count()[0]


CT_tests = data.loc[data['Notes'].str.contains("CT", case=True, na=False)]
CT2020 = CT_tests.count()[0]


Microscopy_tests = data.loc[data['Notes'].str.contains("Microscopy", case=False, na=False)]
Micro2020 = Microscopy_tests.count()[0]

Hardness_tests = data.loc[data['Notes'].str.contains("Hardness", case=False, na=False)]
Hardness2020 = Hardness_tests.count()[0]

Density_Oil_tests = data.loc[data['Notes'].str.contains("Oil", case=False, na=False)]
D_oil2020 = Density_Oil_tests.count()[0]
oil_init = Density_Oil_tests.count()[0]

Density_B311_tests = data.loc[data['Notes'].str.contains("B311", case=False, na=False)]
D_b3112020 = Density_B311_tests.count()[0]
B311_init = Density_B311_tests.count()[0]

Tensile_tests = data.loc[data['Notes'].str.contains("Tensile", case=False, na=False)]
Tensile2020 = Tensile_tests.count()[0]

Fatigue_tests = data.loc[data['Notes'].str.contains("Fatigue", case=False, na=False)]
Fatigue2020 = Fatigue_tests.count()[0]



##############################################################################

#                       Test# Based

##############################################################################

Powder_tests2 = data2.loc[data2['Test#'].str.contains("P", case=False, na=False)]
Powder2020 = Powder2020 + Powder_tests2.count()[0]

Chemistry_tests2 = data2.loc[data2['Test#'].str.contains("C", case=False, na=False)]
Chem2020 = Chem2020 + Chemistry_tests2.count()[0]

CT_tests2 = data2.loc[data2['Test#'].str.contains("CT", case=True, na=False)]
CT2020 = CT2020 + CT_tests2.count()[0]
CT_removal = CT_tests2.count()[0]

Microscopy_tests2 = data2.loc[data2['Test#'].str.contains("M", case=False, na=False)]
Micro2020 = Micro2020 + Microscopy_tests2.count()[0]

Hardness_tests2 = data2.loc[data2['Test#'].str.contains("H", case=False, na=False)]
Hardness2020 = Hardness2020 + Hardness_tests2.count()[0]

Total_Density_TestBased = data2.loc[data2['Test#'].str.contains("D", case=False, na=False)]
Tot_Den_testbased = Total_Density_TestBased.count()[0]

Density_Oil_tests2 = data2.loc[data2['Notes'].str.contains("B962", case=False, na=False)]
D_oil2020 = D_oil2020 + Density_Oil_tests2.count()[0]

Density_B311_tests2 = data2.loc[data2['Notes'].str.contains("B311", case=False, na=False)]
D_b3112020 = D_b3112020 + Density_B311_tests2.count()[0]

Tensile_tests2 = data2.loc[data2['Test#'].str.contains("T", case=False, na=False)]
Tensile2020 = Tensile2020 + Tensile_tests2.count()[0]

Fatigue_tests2 = data2.loc[data2['Test#'].str.contains("F", case=False, na=False)]
Fatigue2020 = Fatigue2020 + Fatigue_tests2.count()[0]


##############################################################################

#                       2021
#                       2021
#                       2021

##############################################################################

#CT IMAGING REPORT: CT-21-003633 will catch P,C,M,T so minus CT from all these

Powder_tests2021 = data3.loc[data3['Test#'].str.contains("P", case=False, na=False)]
Powder2021 = Powder_tests2021.count()[0]
# THIS WILL CATCH VALUES THAT HAVE POWDER CHEMISTRY AS WELL
# CREATE AN EXCEPTION

Chemistry_tests2021 = data3.loc[data3['Test#'].str.contains("C", case=False, na=False)]
Chem2021 = Chemistry_tests2021.count()[0]

CT_tests2021 = data3.loc[data3['Test#'].str.contains("CT", case=True, na=False)]
CT2021 = CT_tests2021.count()[0]

Microscopy_tests2021 = data3.loc[data3['Test#'].str.contains("M", case=False, na=False)]
Micro2021 = Microscopy_tests2021.count()[0]

Hardness_tests2021 = data3.loc[data3['Test#'].str.contains("H", case=False, na=False)]
Hardness2021 = Hardness_tests2021.count()[0]

Total_Density_TestBased2 = data3.loc[data3['Test#'].str.contains("D", case=False, na=False)]
Tot_Den_testbased2 = Total_Density_TestBased2.count()[0]

denremoval = data3.loc[data3['Test#'].str.contains("IRD", case=False, na=False)]
removalden = denremoval.count()[0]
Tot_Den_testbased2 = Tot_Den_testbased2 - removalden

Density_Oil_tests2021 = data3.loc[data3['Notes'].str.contains("B962", case=False, na=False)]
D_oil2021 = Density_Oil_tests2021.count()[0]

Density_B311_tests2021 = data3.loc[data3['Notes'].str.contains("B311", case=False, na=False)]
D_b3112021 = Density_B311_tests2021.count()[0]

Tensile_tests2021 = data3.loc[data3['Test#'].str.contains("T", case=False, na=False)]
Tensile2021 = Tensile_tests2021.count()[0]

Fatigue_tests2021 = data3.loc[data3['Test#'].str.contains("F", case=False, na=False)]
Fatigue2021 = Fatigue_tests2021.count()[0]







