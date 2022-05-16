
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:56:52 2022

@author: hridhoy.datta
"""



# import cv2
# import pdftotext
import os
import pandas as pd
import re
import shutil

sorted_count = 0


# path_certs = "/mnt/c/Users/hridhoy.datta/Desktop/Material Certs - Copy - Copy"
path_certs = "C:/Users/hridhoy.datta/Desktop/Material Certs - Copy - Copy"

path_powders = "C:/Users/hridhoy.datta/Desktop/Powders" 
path_placeholder ="C:/Users/hridhoy.datta/Desktop/Placeholder"

# path_powder_list = "/mnt/c/Users/hridhoy.datta/Desktop/BTI test/Metal Powder December 2021 Report.xlsx"
path_powder_list = "C:/Users/hridhoy.datta/Desktop/BTI test/Metal Powder December 2021 Report.xlsx"

BTI_count = 0
IMR_count = 0
IMR_P_count = 0
SUPPLIER_count = 0

suppliers = ['TEKNA','AP&C','METALPINE','EOS','CARPENTER','LPW','NSL','TLS','CONSTELLIUM','PRAXAIR']

df = pd.read_excel(path_powder_list)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
noprinted = True

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

########################################################################################################################

#------------------------------------------------------------------------------------------------------------------------------------------------------------

########################################################################################################################


# os.chdir(path_certs)

# for root, dirs, files in os.walk('.', topdown=False):
#     # while pog:
            

#     dir_list = os.listdir()
#     for name in dir_list:
        
#         BTI_count = 0
#         IMR_count = 0
#         SUPPLIER_count = 0
        
#         if name in powders:
#             print()
#             print()
#             os.chdir(os.path.join(path_certs, name))
            
#             i = 1
            
#             if not os.path.exists('BTI'):
#                 os.makedirs('BTI')
#             if not os.path.exists('IMR'):
#                 os.makedirs('IMR')
#             if not os.path.exists('SUPPLIER'):
#                 os.makedirs('SUPPLIER')
#             for f in os.listdir(os.getcwd()):
                
#                 try:
#                     if os.path.isfile(f):
                    
#                         if any(supp in f for supp in suppliers):
#                             print(f)
#                             shutil.move(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), 'SUPPLIER'))
                    
#                         #   BTI POWDER REPORTS
                        
#                         elif ("BTI-P-21-Lot#" in f) or ("BTI-P-20-Lot#" in f):
                            
#                             BTI_count += 1
#                             print(f)
#                             shutil.move(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), 'BTI'))
                            
                            
#                         #   IMR POWDER REPORTS
                            
#                         elif "IMR-S-Lot#" in f or "IMR-P-Lot#":
                            
#                             IMR_count += 1
#                             print(f)
#                             shutil.move(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), 'IMR'))
                            

#                         #   SUPPLIER POWDER REPORTS
                            
#                         elif "SUPPLIER-Lot#" in f:
    
#                             SUPPLIER_count += 1
#                             print(f)
#                             shutil.move(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), 'SUPPLIER'))
                            
# #-----------------------------------------------------------------------------------------------------------------------
                        
#                         #   BTI POWDER REPORTS
                        
#                         elif ('P-20' in f) and (BTI_count == 0):
                            
#                             BTI_count += 1
#                             recycle = ''
                            
#                             for letter in range(len(f)):
#                                 k = 1
#                                 if f[letter] == 'R':
                                    
#                                     recycle += f[letter+1]
#                                     if f[letter+2].isdigit():
#                                         recycle += f[letter+2]
#                                     recycle += '-'
#                             # print(os.path.join(os.getcwd(), name))
#                             oldext = os.path.splitext(f)[1]
#                             strname = 'BTI-P-21-Lot#' + name + '-R' + recycle + 'x'
#                             print(strname+oldext)
#                             os.rename(f,strname+oldext)
#                             shutil.move(os.path.join(os.getcwd(), strname+oldext), os.path.join(os.getcwd(), 'BTI'))
                         
#                         elif ('P-21' in f) and (BTI_count):
                            
#                             BTI_count += 1
#                             recycle = ''
                            
#                             for letter in range(len(f)):
#                                 k = 1
#                                 if f[letter] == 'R':
                                    
#                                     recycle += f[letter+1]
#                                     if f[letter+2].isdigit():
#                                         recycle += f[letter+2]
#                                     recycle += '-'

#                             oldext = os.path.splitext(f)[1]
#                             strname = 'BTI-P-21-Lot#' + name + '-R' + recycle + 'x' + '-' + str(BTI_count)
#                             print(strname+oldext)
#                             os.rename(f,strname+oldext)
#                             shutil.move(os.path.join(os.getcwd(), strname+oldext), os.path.join(os.getcwd(), 'BTI'))
                            
                            
#                         elif ('P-20' in f) and (BTI_count):
                            
#                             BTI_count += 1
#                             recycle = ''
                            
#                             for letter in range(len(f)):
#                                 k = 1
#                                 if f[letter] == 'R':
                                    
#                                     recycle += f[letter+1]
#                                     if f[letter+2].isdigit():
#                                         recycle += f[letter+2]
#                                     recycle += '-'

#                             oldext = os.path.splitext(f)[1]
#                             strname = 'BTI-P-20-Lot#' + name + '-R' + recycle + 'x' + '-' + str(BTI_count)
#                             print(strname+oldext)
#                             os.rename(f,strname+oldext)
#                             shutil.move(os.path.join(os.getcwd(), strname+oldext), os.path.join(os.getcwd(), 'BTI'))
#                         #   IMR POWDER REPORTS
                        
#                         elif ('IMR' in f or 'REC' in f) and (IMR_count == 0):
                            
#                             IMR_count += 1
#                             recycle = '0'
#                             for letter in range(len(f)):
#                                 k = 1
#                                 if f[letter] == 'R':
                                    
#                                     recycle += f[letter+1]
#                                     if f[letter+2].isdigit():
#                                         recycle += f[letter+2]
#                                     recycle += '-'

#                             oldext = os.path.splitext(f)[1]
#                             strname = 'IMR-S-Lot#' + name + '-R' + recycle + 'x' 
#                             print(strname+oldext)
#                             os.rename(f,strname+oldext)
#                             shutil.move(os.path.join(os.getcwd(), strname+oldext), os.path.join(os.getcwd(), 'IMR'))
                            
#                         elif ('IMR' in f or 'REC' in f) and (IMR_count):
                                
#                             IMR_count += 1
#                             recycle = '0'
#                             for letter in range(len(f)):
#                                 k = 1
#                                 if f[letter] == 'R':
                                    
#                                     recycle += f[letter+1]
#                                     if f[letter+2].isdigit():
#                                         recycle += f[letter+2]
#                                     recycle += '-'

#                             oldext = os.path.splitext(f)[1]
#                             strname = 'IMR-S-Lot#' + name + '-R' + recycle + 'x' + '-' + str(IMR_count)
#                             print(strname+oldext)
#                             os.rename(f,strname+oldext)
#                             shutil.move(os.path.join(os.getcwd(), strname+oldext), os.path.join(os.getcwd(), 'IMR'))
                                
                        
                                
                                
#                         #   SUPPLIER POWDER REPORTS
                        
#                         elif SUPPLIER_count:
                            
#                             SUPPLIER_count += 1
#                             oldext = os.path.splitext(f)[1]
#                             strname = 'SUPPLIER-Lot#' + name + '-' + str(SUPPLIER_count)

#                             os.rename(f,strname+oldext)
#                             shutil.move(os.path.join(os.getcwd(), strname+oldext), os.path.join(os.getcwd(), 'SUPPLIER'))

#                         elif SUPPLIER_count == 0:

#                             SUPPLIER_count += 1
#                             oldext = os.path.splitext(f)[1]
#                             strname = 'SUPPLIER-Lot#' + name 

#                             os.rename(f,strname+oldext)
#                             shutil.move(os.path.join(os.getcwd(), strname+oldext), os.path.join(os.getcwd(), 'SUPPLIER'))
                
#                 except:
#                     try:
#                         os.rename(os.path.join(os.getcwd(),f),strname+'-dup'+oldext)
#                         shutil.move(os.path.join(os.getcwd(), strname+'-dup'+oldext), os.path.join(os.getcwd(), 'SUPPLIER'))
#                     except:
#                         strname = os.path.splitext(f)[0]
#                         oldext = os.path.splitext(f)[1]
#                         print(strname+'-dup'+oldext)
#                         os.rename(os.path.join(os.getcwd(),f),strname+'-dup'+oldext)
#                         shutil.move(os.path.join(os.getcwd(), strname+'-dup'+oldext), os.path.join(os.getcwd(), 'SUPPLIER'))

                            
                
#         if BTI_count:
#             print("\t BTI - " + str(BTI_count))
#         if IMR_count:
#             print("\t IMR - " + str(IMR_count))
#         if SUPPLIER_count:
#             print("\t SUPPLIER - " + str(SUPPLIER_count))


########################################################################################################################

#--------------------------------FIXER-----------------------------------------------------------------------------------------

########################################################################################################################

# os.chdir(path_certs)

# for root, dirs, files in os.walk('.', topdown=False):
#     # while pog:
            

#     dir_list = os.listdir()
#     for name in dir_list:
        
#         BTI_count = 0
#         IMR_count = 0
#         SUPPLIER_count = 0
#         IMR_P_count = 0
        
#         if name in powders:
#             print()
#             print()
#             os.chdir(os.path.join(path_certs, name))
            
#             i = 1
            
#             for f in os.listdir(os.getcwd()):
                

#                 if os.path.isfile(f) and os.path.splitext(f)[1] == '.pdf':
#                     if ('SUPPLIER-' in f) or ('IMR-S-' in f) or ('BTI-' in f):
                    
#                         with open(f,'rb') as path:
#                             pdf = pdftotext.PDF(path)

#                         #BTI REPORT CHECKER
                        
#                         if 'BTI-FRM' in pdf[0] and '2020' in pdf[0]:
#                             print(f)
                            
#                             if BTI_count == 0:
                                
#                                 BTI_count += 1
#                                 oldext = os.path.splitext(f)[1]
#                                 strname = 'BTI-P-20-Lot#' + name 
#                                 print(strname+oldext)
#                                 os.rename(f,strname+oldext)
#                                 sorted_count += 1
                                
#                             elif BTI_count != 0:
                                
#                                 BTI_count += 1
#                                 oldext = os.path.splitext(f)[1]
#                                 strname = 'BTI-P-20-Lot#' + name + '-' + str(BTI_count) 
#                                 print(strname+oldext)
#                                 os.rename(f,strname+oldext)  
#                                 sorted_count += 1
                                
#                         elif 'BTI-FRM' in pdf[0] and '2021' in pdf[0]:
#                             print(f)
                            
#                             if BTI_count == 0:
                                
#                                 BTI_count += 1
#                                 oldext = os.path.splitext(f)[1]
#                                 strname = 'BTI-P-21-Lot#' + name 
#                                 print(strname+oldext)
#                                 os.rename(f,strname+oldext)    
#                                 sorted_count += 1
                                
#                             elif BTI_count != 0:
                                
#                                 BTI_count += 1
#                                 oldext = os.path.splitext(f)[1]
#                                 strname = 'BTI-P-21-Lot#' + name + '-' + str(BTI_count) 
#                                 print(strname+oldext)
#                                 os.rename(f,strname+oldext)
#                                 sorted_count += 1



#                         #IMR REPORT CHECKER
                        
#                         if 'IMR Report Number' in pdf[0]:
#                             print(f)
                            
#                             if IMR_P_count == 0:
                                
#                                 IMR_P_count += 1
#                                 oldext = os.path.splitext(f)[1]
#                                 strname = 'IMR-P-Lot#' + name 
#                                 print(strname+oldext)
#                                 os.rename(f,strname+oldext)
#                                 sorted_count += 1
                                
#                             elif IMR_P_count != 0:
                                    
#                                 IMR_P_count += 1
#                                 oldext = os.path.splitext(f)[1]
#                                 strname = 'IMR-P-Lot#' + name + '-' + str(IMR_P_count)
#                                 print(strname+oldext)
#                                 os.rename(f,strname+oldext)
#                                 sorted_count += 1
                                
# print(sorted_count)
                        
                            



########################################################################################################################

#------------------------------------------------------------------------------------------------------------------------------------------------------------

########################################################################################################################


#------------------------------------------------------------------------------

# os.chdir(path_certs)

# for root, dirs, files in os.walk('.', topdown=False):
#     # while pog:
            

#     dir_list = os.listdir()
#     for name in dir_list:
        
#         BTI_count = 0
#         IMR_count = 0
#         SUPPLIER_count = 0
        
#         if name in powders:
#             print()
#             print()
#             os.chdir(os.path.join(path_certs, name))
            
#             i = 1
            
#             if not os.path.exists('BTI'):
#                 os.makedirs('BTI')
#             if not os.path.exists('IMR'):
#                 os.makedirs('IMR')
#             if not os.path.exists('SUPPLIER'):
#                 os.makedirs('SUPPLIER')
#             for f in os.listdir(os.getcwd()):
                

#                 if os.path.isfile(f) and os.path.splitext(f)[1] == '.pdf':
#                     if 'SUPPLIER-' in f:
                    
#                         with open(f,'rb') as path:
#                             pdf = pdftotext.PDF(path)
                        
#                         if 'IMR Report Number' in pdf[0]:
#                             print(f)


########################################################################################################################

#-------------sORTER----------------------------------------------------------------------------------------------------------------------------

########################################################################################################################


#------------------------------------------------------------------------------
os.chdir(path_certs)

for root, dirs, files in os.walk('.', topdown=False):
    # while pog:
            

    dir_list = os.listdir()
    for name in dir_list:
        
        BTI_count = 0
        IMR_count = 0
        SUPPLIER_count = 0
        
        if name in powders:
            print()
            print()
            os.chdir(os.path.join(path_certs, name))
            
            i = 1
            
            if not os.path.exists('BTI'):
                os.makedirs('BTI')
            # if not os.path.exists('IMR'):
            #     os.makedirs('IMR')
            # if not os.path.exists('SUPPLIER'):
            #     os.makedirs('SUPPLIER')
            for f in os.listdir(os.getcwd()):
                
                try:
                    if os.path.isfile(f):
                    
                        #   BTI POWDER REPORTS
                        
                        if ("BTI" in f):
                            
                            # with open(f,'rb') as path:
                            #     pdf = pdftotext.PDF(path)
                            # # print(f)
                            
                            # page = pdf[0]
                            # pattern = r"(?:Test \#\:).+\b"
                            # # temp = re.findall(pattern,page)[0] 
                            # # temp = temp.split()
                            # reportno = re.findall(pattern,page)[0].split()[-1].split('-')
                            # # print(reportno)
                            # # print(f.split('-'))
                            # temp = f.split('Lot')
                            # try:    
                            #     print(temp[0] + reportno[2] + '-' + reportno[3] + '-Lot' + temp[1])
                            #     newname = temp[0] + reportno[2] + '-' + reportno[3] + '-Lot' + temp[1]
                            # except:
                            #     print(temp[0] + reportno[-1] + '-Lot' + temp[1])
                            #     newname = temp[0] + reportno[-1] + '-Lot' + temp[1]
                            
                            # print()
                            
                            BTI_count += 1
                            print(f)
                            shutil.move(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), 'BTI'))
                            # os.rename(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), newname))
                            
                            
                            
                        #   IMR POWDER REPORTS
                            
                        # if "IMR" in f:
                            
                        #     IMR_count += 1
                        #     print(f)
                        #     shutil.move(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), 'IMR'))
                            

                        # #   SUPPLIER POWDER REPORTS
                            
                        # else:
    
                        #     SUPPLIER_count += 1
                        #     print(f)
                        #     shutil.move(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), 'SUPPLIER'))
                            
#-----------------------------------------------------------------------------------------------------------------------
                        
                                        
                except:
                    pass
                            
                
        # if BTI_count:
        #     print("\t BTI - " + str(BTI_count))
        # if IMR_count:
        #     print("\t IMR - " + str(IMR_count))
        # if SUPPLIER_count:
        #     print("\t SUPPLIER - " + str(SUPPLIER_count))
