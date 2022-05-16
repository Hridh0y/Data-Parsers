# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:13:41 2021

@author: hridh
"""


import pdftotext
import re 
import pandas as pd
import os

def PDFREADERIMR_BTI_SINGLE(path):
    
    
    # Burloak_Report_number = '*'
    # Lot_number = '*'
    # Recycle_count = '*'
    WorkOrder = '*'
    BTI = '*'
    PartNumber = '*'
    SerialNumber = '*'
    Material = '*'
    # Machine = '*'
    # Sieve = 0.0
    # IMR_Report_number = '*'
    Aluminumwt = '*'
    Vanadiumwt = '*'
    Ironwt = '*'
    Chromiumwt = '*'
    Siliconwt = '*'
    Yttriumwt = '*'
    Carbonwt = '*'
    Copperwt = '*'
    Sulphurwt = '*'
    Nitrogenwt = '*'
    Oxygenwt = '*'
    Hydrogenwt = '*'
    Zirconiumwt = '*'
    Nickelwt = '*'
    Manganesewt = '*'
    Titaniumwt = '*'
    Cobaltwt = '*'
    Phosphoruswt = '*'
    Tungstenwt = '*'
    Tinwt = '*'
    Magnesiumwt = '*'
    Leadwt = '*'
    Zincwt = '*'
    Zirconiumwt = '*'
    OEwt = '*'
    OTwt = '*'
    Grade = '*'
    
    elemlist = [['Al','Al1'],['C','C1','C2'],['Cr'],['Co'],['Cu'],['H','H1','H2'],['Fe'],['Pb'],['Mg'],['Mn'],['Ni'],['N','N1','N2'],['O','O1','O2'],['P'],['Si'],['S'],['Sn'],['Ti'],['W'],['V'],['Y'],['Zn'],['Zr'],['OE'],['OT']]
    conclist = ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']
    
    page_counter = 0
    
    with open(path,'rb') as f:
        pdf = pdftotext.PDF(f)
    

    

        # Iterate over all the pages --------------------------------------------------
    for page in pdf:
        
        page_counter += 1
        
        #-------------------------------------------------------------------------
        
        #   Detecting compounds 
        
        #-------------------------------------------------------------------------
        
        lines = page.splitlines()
        linecounter = 0
        parameters = [0,0]
        for line in lines:
            
            if 'Element' in line or ('Element' in line and 'Sample' in line):        
                # print(line)
                parameters[0] = linecounter
            
            if 'Results' in line or 'weight percent' in line:        
                # print(line)
                parameters[1] = linecounter
                break
                
            linecounter += 1
        
        if parameters[1] == 0:
            parameters[1] = linecounter
        
        if parameters[0] == 0:
            parameters[1] = 0
            

        linecounter = 0

        for line in lines:
            if linecounter > parameters[0] and linecounter < parameters[1]:
                line = line.replace('Max.','')
                line = line.replace('Maximum','')
                line = line.replace('–','')
                wordlist = line.split()
                if len(wordlist) > 1 and len(wordlist) < 5:
                    for i in range(len(elemlist)):
                        if wordlist[0] in elemlist[i]:
                            conclist[i] = wordlist[1]
                            # print(elemlist[i][0] + '-' + conclist[i])
                
            linecounter += 1
        
        
    return(conclist)


        


