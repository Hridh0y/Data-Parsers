# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:56:52 2022

@author: hridhoy.datta
"""
import os
import pandas as pd
import re
import shutil

# path_certs = "/mnt/c/Users/hridhoy.datta/Desktop/Material Certs - Copy"
path_certs = "C:/Users/hridhoy.datta/Desktop/Material Certs - Copy - Copy"

path_powders = "C:/Users/hridhoy.datta/Desktop/Powders" 
path_placeholder ="C:/Users/hridhoy.datta/Desktop/Placeholder"

# path_powder_list = "/mnt/c/Users/hridhoy.datta/Desktop/BTI test/Metal Powder December 2021 Report.xlsx"
path_powder_list = "C:/Users/hridhoy.datta/Desktop/BTI test/Metal Powder December 2021 Report.xlsx"

df = pd.read_excel(path_powder_list)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
#------------------------------------------------------------------------------

b = []
powders = df['Batch'].tolist()
materials = df['Material'].tolist()
for i in powders:
    if type(i) == str:
        # b+=i.split(", /")
        b += re.split('; |, |\*|\n |/',i)
    else:
        b.append(str(i))
# print(b)
powders = b

#------------------------------------------------------------------------------


import os
import shutil

for doc_path in os.listdir(path_certs):
    if doc_path in powders:
        print(os.path.join(path_certs,doc_path))
        os.chdir(os.path.join(path_certs,doc_path))
        for root, dirs, files in os.walk(os.path.join(path_certs,doc_path), topdown=False):
            for file in files:
                try:
                    shutil.move(os.path.join(root, file), os.path.join(path_certs,doc_path))
                    # print()
                except:
                    pass
            for file in dirs:
                try:
                    os.rmdir(os.path.join(path_certs,doc_path,file))
                except:
                    pass
        # print('safe' + ' = ' + doc_path)
    else:
        shutil.rmtree(os.path.join(path_certs,doc_path))
        
