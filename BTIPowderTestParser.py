
import pdftotext
import re 
import pandas as pd
import os












########################################################################################

                                # FUNCTION DEFINITION
                                
########################################################################################




def PDFREADER_BTI(path):
    
    
    Burloak_Report_number = '-'
    Lot_number = '-'
    Recycle_count = '-'
    Material = '-'
    Machine = '-'
    Sieve = 0.0
    Carbonwt = 0.0
    Sulphurwt = 0.0
    Nitrogenwt = 0.0
    Oxygenwt = 0.0
    Hydrogenwt = 0.0
    Apparent_Density = '-'
    Tap_Density  = '-'
    Flow_rate = '-'
    Carney_flow = '-'
    d_10 = '-'
    d_50 = '-'
    d_90 = '-'
    Grade ='-'
    
    page_counter = 0

    with open(path,'rb') as f:
        pdf = pdftotext.PDF(f)
    
    pattern11 = r"(?:Apparent Density\: ).+\b"
    pattern10 = r"(?:Test \#\: ).+\b"  
    pattern9 = r"(?:Feedstock Lot \#\: ).+\b"
    pattern1 = r"(?:Tap Density\: ).+\b"
    pattern2 = r"(?:FRH\= ).+\b"
    pattern3 = r"(?:FRC\= ).+\b"
    pattern4 = r"(?:Oxygen).+\b"
    pattern5 = r"(?:Nitrogen).+\b" 
    pattern6 = r"(?:Carbon).+\b" 
    pattern7 = r"(?:Sulphur).+\b"
    pattern8 = r"(?:Hydrogen).+\b"  
    pattern12 = r"(?:10.00).+\b" 
    pattern13 = r"(?:50.00).+\b" 
    pattern14 = r"(?:90.00).+\b"
    pattern15 = r"(?:Material\: ).+\b"
    pattern16 = r"(?:Printing Platform\: ).+\b"
    pattern17 = r"(?:Sieve mesh size ).+\b"
    

    
    number = ''
    # Iterate over all the pages --------------------------------------------------
    for page in pdf:
        
        page_counter += 1
        
        
        valueTest = re.findall(pattern10,page)
        valueLot_no = re.findall(pattern9,page)
        valueTap_Density = re.findall(pattern1, page)
        valueApparent_Density = re.findall(pattern11, page)
        valueFR_Hall = re.findall(pattern2, page)
        valueFR_Carney = re.findall(pattern3, page)
        valueOxygen = re.findall(pattern4,page)
        valueNitrogen = re.findall(pattern5,page)
        valueCarbon = re.findall(pattern6,page)
        valueSulphur = re.findall(pattern7,page)
        valueHydrogen = re.findall(pattern8,page)
        value_d10 = re.findall(pattern12,page)  
        value_d50 = re.findall(pattern13,page) 
        value_d90 = re.findall(pattern14,page)
        value_material = re.findall(pattern15,page)
        value_machine = re.findall(pattern16,page)
        value_sieve = re.findall(pattern17,page)
        
        
    
        number = ''
        
        # Extracting Printer ---------------------------------------------
        if page_counter <= 1:
            try:
    
                stringTD = value_machine[0]
                number = ''
                word_list = stringTD.split()
                plat = False
                for wordstub in word_list:
                    if wordstub == r"Platform:":
                        plat = True
                        continue
                    
                    # if wordstub == r'Test' or wordstub == r'PO':
                    #     plat = False
                        
                    if plat == True:
                        try:
                            number += wordstub + ' '
                            # plat = False
                        except Exception:
                            pass
                    # if wordstub == r'Specimen:':
                        # plat = True
                        # continue
                    
                    
            except Exception:
                pass
        
            try:
                if number != '':
    
                    Machine = number
                    
            except Exception:
                pass
            
        number = ''  
        
        # Extracting Material ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_material:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Material:':
                            plat = True
                            continue
                        
                        if wordstub == r'Test' or wordstub == r'Work':
                            plat = False
                                                
                        if plat == True:
                            try:
                                number += wordstub + ' '
                            except Exception:
                                pass

                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        Material = number
                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting Sieve ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_sieve:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'size':
                            plat = True
                            continue
                        
                        if wordstub == r'Printing' or wordstub == r'Work':
                            plat = False
                                                
                        if plat == True:
                            try:
                                number += wordstub + ' '
                            except Exception:
                                pass

                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        Sieve = number
                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting Tap Density -------------------------------------------------------------------------------------------------------
        if valueTap_Density:
            try:
                Tap_Density = valueTap_Density[0].split()[2] + ' ' + valueTap_Density[0].split()[3]
            except:
                Tap_Density = valueTap_Density[0].split()[2]
        
        # Apparent Density -------------------------------------------------------------------------------------------------------
        if valueApparent_Density:
            try:
                Apparent_Density = valueApparent_Density[0].split()[2] + ' ' + valueApparent_Density[0].split()[3]
            except:
                Apparent_Density = valueApparent_Density[0].split()[2]
        
        # Carney Flow --------------------------------------------------------------------------------------------------------------------
        if valueFR_Carney:
            try:
                Carney_flow = (valueFR_Carney[0].split()[1] + ' ' + valueFR_Carney[0].split()[2] + ' ' + valueFR_Carney[0].split()[3])
            except:
                try:
                    Carney_flow = (valueFR_Carney[0].split()[1] + ' ' + valueFR_Carney[0].split()[2])
                except:
                    Carney_flow = (valueFR_Carney[0].split()[1])
        
        # Hall Flow -----------------------------------------------------------------------------------------------------------------------------------------------------------
        if valueFR_Hall:
            try:
                Flow_rate = (valueFR_Hall[0].split()[1] + ' ' + valueFR_Hall[0].split()[2] + ' ' + valueFR_Hall[0].split()[3])
            except:
                try:
                    Flow_rate = (valueFR_Hall[0].split()[1] + ' ' + valueFR_Hall[0].split()[2])
                except:
                    Flow_rate = (valueFR_Hall[0].split()[1])
        
        # value of da deez --------------------------------------------------------------------------------------------------------------
        if value_d10:
            d_10 = (value_d10[1].split()[1])
        
        if value_d50:
            d_50 = (value_d50[0].split()[1])
        
        if value_d90:
            d_90 = (value_d90[0].split()[1])
        
        # Extracting Carbon --------------------------------------------------------------------------------------------------------------
        
        if valueCarbon and Carbonwt == 0.0:
            if valueCarbon[-1].split()[1] == 'Not' or valueCarbon[-1].split()[1] == 'NT' :
                Carbonwt = '-'
            else:
                Carbonwt = (valueCarbon[-1].split()[1])

        # Extracting Oxygen --------------------------------------------------------------------------------------------------------------        
        if valueOxygen and Oxygenwt == 0.0:
            if valueOxygen[-1].split()[1] == 'Not' or valueOxygen[-1].split()[1] == 'NT':
                Oxygenwt = '-'
            else:
                Oxygenwt = (valueOxygen[-1].split()[1])
        
        # Extracting Nitrogen --------------------------------------------------------------------------------------------------------------        
        if valueNitrogen:
            if valueNitrogen[-1].split()[1] == 'Not' or valueNitrogen[-1].split()[1] == 'NT':
                Nitrogenwt = '-'
            else:
                Nitrogenwt = (valueNitrogen[-1].split()[1])
        
        # Extracting Hydrogen --------------------------------------------------------------------------------------------------------------        
        if valueHydrogen:
            if valueHydrogen[-1].split()[1] == 'Not' or valueHydrogen[-1].split()[1] == 'NT':
                Hydrogenwt = '-'
            else:
                Hydrogenwt = (valueHydrogen[-1].split()[1])
                
#--------------------------------------------------------------------------------------------------------------        
        
        if Material.split()[-1] == '5' and Material.split()[0] == 'Titanium':
            Grade = '5'
        elif Material.split()[0] == 'Titanium':
            Grade = '23'
    
        number = ''  
#--------------------------------------------------------------------------------------------------------------        

                
    enter_list = ['*',Burloak_Report_number,Lot_number,Recycle_count,Material,Machine,Sieve,Grade,Tap_Density,Apparent_Density,Carney_flow,Flow_rate,Carbonwt,Oxygenwt,Nitrogenwt,Hydrogenwt,d_10,d_50,d_90]
            
    return (enter_list)
    
# ########################################################################################

#                         # FUNCTION DEFINITION ENDING
                                
# ########################################################################################
# ########################################################################################

#                         # FUNCTION DEFINITION 
                                
# ########################################################################################
    

def PDFREADER_CMTL(path,name):
    
    
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
    OEwt = '*'
    OTwt = '*'
    Grade = '*'
    
    page_counter = 0
    elemlist = ['Aluminum','Vanadium','Iron','Chromium','Silicon','Yttrium','Tin','Sulphur','Nitrogen','Lead','Hydrogen','Tungsten','Manganese','Nickel','Zinc','Phosphorus','Cobalt']
    conclist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    with open(path,'rb') as f:
        pdf = pdftotext.PDF(f)
    
    patternID = r"(?:ID\:).+\b"  
    patternMaterial = r"(?:Specimen\:).+\b"  
    patternAluminum = r"(?:Aluminum).+\b"
    patternIron = r"(?:Iron).+\b"
    patternChromium = r"(?:Chromium).+\b"
    patternSilicon = r"(?:Silicon).+\b"
    patternYttrium = r"(?:Yttrium).+\b"
    patternCarbon = r"(?:Carbon).+\b"
    patternCopper = r"(?:Copper).+\b"
    patternSulphur = r"(?:Sulphur).+\b"
    patternNitrogen = r"(?:Nitrogen).+\b"
    patternOxygen = r"(?:Oxygen).+\b"
    patternHydrogen = r"(?:Hydrogen).+\b"
    patternZirconium = r"(?:Zirconium).+\b"
    patternNickel = r"(?:Nickel).+\b"
    patternManganese = r"(?:Manganese).+\b"
    patternMagnesium = r"(?:Magnesium).+\b"
    patternZinc = r"(?:Zinc).+\b"
    patternTitanium = r"(?:Titanium).+\b"
    patternTungsten = r"(?:Tungsten).+\b"
    patternCobalt = r"(?:Cobalt).+\b"
    patternTin = r"(?:Tin).+\b"
    patternLead = r"(?:Lead).+\b"
    patternPhosphorus = r"(?:Phosphorus).+\b"
    patternVanadium = r"(?:Vanadium).+\b"
    patternOE = r"(?:Others Each).+\b"
    patternOT = r"(?:Others Total).+\b"
    patternOthers = r"(?:Others include).+\b"
    
    

    
    number = ''
    # Iterate over all the pages --------------------------------------------------
    for page in pdf:
        
        page_counter += 1
        
        valueID = re.findall(patternID,page)
        valueMaterial = re.findall(patternMaterial,page)
        valueAluminum = re.findall(patternAluminum,page)
        valueIron = re.findall(patternIron,page)
        valueChromium = re.findall(patternChromium,page)
        valueSilicon = re.findall(patternSilicon ,page)
        valueYttrium = re.findall(patternYttrium,page)
        valueCarbon = re.findall(patternCarbon,page)
        valueCopper = re.findall(patternCopper,page)
        valueSulphur = re.findall(patternSulphur,page)
        valueNitrogen = re.findall(patternNitrogen,page)
        valueOxygen = re.findall(patternOxygen,page)
        valueHydrogen = re.findall(patternHydrogen,page)
        valueZirconium = re.findall(patternZirconium,page)
        valueNickel = re.findall(patternNickel,page)
        valueManganese = re.findall(patternManganese,page)
        valueMagnesium = re.findall(patternMagnesium,page)
        valueTitanium = re.findall(patternTitanium,page)
        valueTungsten = re.findall(patternTungsten,page)
        valueTin = re.findall(patternTin,page)
        valueLead = re.findall(patternLead,page)
        valueCobalt = re.findall(patternCobalt,page)
        valuePhosphorus = re.findall(patternPhosphorus,page)
        valueZinc = re.findall(patternZinc,page)
        valueVanadium = re.findall(patternVanadium,page)
        valueOE = re.findall(patternOE,page)
        valueOT = re.findall(patternOT,page)
        valueOthers = re.findall(patternOthers,page)

    
        number = ''
        
        # Extracting Work Order, BTI, Serial Number ---------------------------------------------
        if page_counter <= 1:
            try:
                for stringTD in valueID:
                    

                    wordstring = stringTD.replace("/", " ")
                    wordstring = wordstring.replace(",", " ")
                    wordstring = wordstring.replace(':', " ")
                    word_list = wordstring.split()
                                        
                    try:
                        number1 = word_list[1]
                        number2 = word_list[2]
                        number3 = word_list[3]
                        number4 = word_list[4]
                        if number4[-2] == '(' or number4[-3] == '(':
                            number4 += ')'
                        if number1[1] == 'T':
                            number4 = number3
                            number3 = number2
                            number2 = number1
                            number1 = "N/A"
                            
                    except Exception:
                        pass
                    
            except Exception:
                pass
        
            try:
                WorkOrder = number1
                BTI = number2
                PartNumber = number3
                SerialNumber = number4
            except Exception:
                pass
        
            number = ''    
        
        # Extracting Material ---------------------------------------------
        try:

            stringTD = valueMaterial[0]
            number = ''
            word_list = stringTD.split()

            plat = False
            for wordstub in word_list:
                if wordstub == r'Material:':
                    plat = True
                    continue
                
                if wordstub == r'Test' or wordstub == r'Chemistry' or wordstub == r'Coupon':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Specimen:':
                    plat = True
                    continue
                
                
        except Exception:
            pass
    
        try:
            if number != '':

                Material = number
        except Exception:
            pass
    
        number = ''  
        # Extracting Aluminum Value -------------------------------------------------
        try:
            stringTD = valueAluminum[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Aluminum':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Aluminumwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Iron Value -------------------------------------------------
        try:
            stringTD = valueIron[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Iron':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Ironwt = number
        except Exception:
            pass
        
        number = ''

        # Extracting Chromium Value -------------------------------------------------
        try:
            stringTD = valueChromium[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Chromium':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Chromiumwt = number                
        except Exception:
            pass
        
        number = ''
        
        # Extracting Copper Value -------------------------------------------------
        try:
            stringTD = valueCopper[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Copper':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Copperwt = number                
        except Exception:
            pass
        
        number = ''
        
        # Extracting Silicon Value -------------------------------------------------
        try:
            stringTD = valueSilicon[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Silicon':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Siliconwt = number              
        except Exception:
            pass
        
        number = ''
        
        # Extracting Yttrium Value -------------------------------------------------
        try:
            stringTD = valueYttrium[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Yttrium':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Yttriumwt = number            
        except Exception:
            pass
        
        number = ''
        
        # Extracting Carbon Value -------------------------------------------------
        try:
            stringTD = valueCarbon[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Carbon':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Carbonwt = number            
        except Exception:
            pass
        
        number = ''
                    
        # Extracting Sulphur Value -------------------------------------------------
        try:
            stringTD = valueSulphur[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Sulphur':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Sulphurwt = number             
        except Exception:
            pass
        
        number = ''
        
        # Extracting Nitrogen Value -------------------------------------------------
        try:
            stringTD = valueNitrogen[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Nitrogen':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Nitrogenwt = number               
        except Exception:
            pass
        
        number = ''
        
        # Extracting Oxygen Value -------------------------------------------------
        try:
            stringTD = valueOxygen[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Oxygen':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Oxygenwt = number                
        except Exception:
            pass
        
        number = ''
        
        # Extracting Hydrogen Value -------------------------------------------------
        try:
            stringTD = valueHydrogen[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Hydrogen':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Hydrogenwt = number           
        except Exception:
            pass
        
        number = ''
        
        # Extracting Manganese Value -------------------------------------------------
        try:
            stringTD = valueManganese[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Manganese':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Manganesewt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Nickel Value -------------------------------------------------
        try:
            stringTD = valueNickel[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Nickel':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Nickelwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Zinc Value -------------------------------------------------
        try:
            stringTD = valueZinc[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Zinc':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Zincwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Phosphorus Value -------------------------------------------------
        try:
            stringTD = valuePhosphorus[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Phosphorus':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Phosphoruswt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Cobalt Value -------------------------------------------------
        try:
            stringTD = valueCobalt[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Cobalt':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Cobaltwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Titanium Value -------------------------------------------------
        try:
            stringTD = valueTitanium[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Titanium':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Titaniumwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Tungsten Value -------------------------------------------------
        try:
            stringTD = valueTungsten[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Tungsten':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Tungstenwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Tin Value -------------------------------------------------
        try:
            stringTD = valueTin[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Tin':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Tinwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Magnesium Value -------------------------------------------------
        try:
            stringTD = valueMagnesium[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Magnesium':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Magnesiumwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Lead Value -------------------------------------------------
        try:
            stringTD = valueLead[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Lead':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Leadwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Vanadium Value -------------------------------------------------
        try:
            stringTD = valueVanadium[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Vanadium':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                Vanadiumwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Other Elements Value -------------------------------------------------
        try:
            stringTD = valueOE[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Each':
                    plat = True
                    continue
                if wordstub == r'%' or wordstub == r'Balance':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                OEwt = number
        except Exception:
            pass
        
        number = ''
        
        # Extracting Others Total Value -------------------------------------------------
        try:
            stringTD = valueOT[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Total':
                    plat = True
                    continue
                if wordstub == r'%':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
        except Exception:
            pass
    
        try:
            if number != '':
                OTwt = number             
        except Exception:
            pass
        


    enter_list = [name,WorkOrder,BTI,PartNumber,SerialNumber,Material,Aluminumwt,Carbonwt,Chromiumwt,Cobaltwt,Copperwt,Hydrogenwt,Ironwt,Leadwt,Magnesiumwt,Manganesewt,Nickelwt,Nitrogenwt,Oxygenwt,Phosphoruswt,Siliconwt,Sulphurwt,Tinwt,Titaniumwt,Tungstenwt,Vanadiumwt,Yttriumwt,Zincwt,OEwt,OTwt]
            
    return (enter_list)

# ########################################################################################

#                         # FUNCTION DEFINITION ENDING
                                
# ########################################################################################
# ########################################################################################

#                         # FUNCTION DEFINITION 
                                
# ########################################################################################
        
 
def PDFREADER_Chemistry(path):
    
    WorkOrder = ''
    BuildPlate = ''
    PartNumber = ''
    Temp = '*'
    Burloak_Report_number = '*'
    Lot_number = '*'
    Recycle_count = ''
    Material = '*'
    Machine = '*'
    Serial = '*'
    Carbonwt = 0.0
    Sulphurwt = 0.0
    Nitrogenwt = 0.0
    Oxygenwt = 0.0
    Hydrogenwt = 0.0
    Grade = '*'
    
    page_counter = 0

    with open(path,'rb') as f:
        pdf = pdftotext.PDF(f)
    

    pattern9 = r"(?:Feedstock Lot \#\: ).+\b"
    pattern18 = r"(?:Specimen).+\b"
    pattern4 = r"(?:Oxygen).+\b"
    pattern5 = r"(?:Nitrogen).+\b" 
    pattern6 = r"(?:Carbon).+\b" 
    pattern7 = r"(?:Sulphur).+\b"
    pattern8 = r"(?:Hydrogen).+\b"  
   
    pattern15 = r"(?:Material\: ).+\b"
    pattern16 = r"(?:built on ).+\b"

    

    
    number = ''
    for page in pdf:
        
        page_counter += 1
        
        valueLot_no = re.findall(pattern9,page)

        valueOxygen = re.findall(pattern4,page)
        valueNitrogen = re.findall(pattern5,page)
        valueCarbon = re.findall(pattern6,page)
        valueSulphur = re.findall(pattern7,page)
        valueHydrogen = re.findall(pattern8,page)
        value_info = re.findall(pattern18,page)
        value_material = re.findall(pattern15,page)
        value_machine = re.findall(pattern16,page)


        number1 = ''
        number2 = ''
        number3 = ''
        number4 = ''
        number = ''
        
        # Extracting Feedstock Lot ---------------------------------------------
        if page_counter <= 1:
            try:
                
                for stringTD in valueLot_no:
                    word_list = stringTD.split()
                    plat = False
                    write = False
    
                    
                    for wordstub in word_list:
                        if wordstub == r'#:':
                            plat = True
                            continue
                        
                        if write == True:
                            plat = False
                            
                        if plat == True:
                            try:
                                number = wordstub
                                write = True
                            except Exception:
                                pass
                        
                    
            except Exception:
                pass
            
            if 'BCP' not in number:
                Lot_number = number.split('-')[0]
                
                try:
                    for i in number.split('-')[1]:
                        if i.isdigit():
                            Recycle_count += i
                except:
                    pass
            
            else:
                Lot_number = number
            
            # try:
            #     Machine = number1 + ' ' + number2 + ' ' + number3 + ' ' + number4 + ' '
            # except Exception:
            #     pass
        
            number = '' 
            number1 = '*'    
            number2 = '*'
            number3 = '*'    
            number4 = '*'            
        # Extracting Work Order, BTI and Part number---------------------------------------------
        if page_counter <= 1:

            for stringTD in value_info:
                
                stringTD = stringTD.split('Job')[0]
                wordstring = stringTD.replace(",", " ")
                wordstring = wordstring.replace('-', " ")
                wordstring = wordstring.replace(':', " ")
                word_list = wordstring.split()
                
                mode = 0
            for i in range(len(word_list)):
                if word_list[i] == 'Specimen':
                    continue
                elif word_list[i] == 'ID':
                    continue
                elif 'BTI' in word_list[i]:
                    BuildPlate += word_list[i]
                    i += 1
                    BuildPlate += '-' + word_list[i] 
                    mode = 1
                    i += 1 
                    PartNumber += word_list[i]
                if mode == 1:
                    PartNumber += '-' + word_list[i]
                else:
                    WorkOrder += word_list[i]
        
        try:
            if PartNumber[-2] == '(' or PartNumber[-3] == '(' :
                PartNumber += ')'            
        
        except:
            pass
        
        
        number1 = ''
        number2 = ''
        number3 = ''
        number4 = ''
        number = ''
        # Extracting Machine and Serial---------------------------------------------
        if page_counter <= 1:
            try:
                for stringTD in value_machine:
                    

                    wordstring = stringTD.replace("/", " ")
                    wordstring = wordstring.replace(",", " ")
                    wordstring = wordstring.replace(':', " ")
                    word_list = wordstring.split()
                                        
                    try:
                        number1 = word_list[2]
                        number2 = word_list[3]
                        number3 = word_list[5]
                        number4 = word_list[7]
                        
                        
                    except Exception:
                        pass
                    
            except Exception:
                pass
        
            try:
                Machine = number1 + ' ' + number2 + ' '
                Serial = number3
                Temp = number4
            except Exception:
                pass
        
            number = ''    
        
        # Extracting Material ---------------------------------------------
        try:

            stringTD = value_material[0]
            number = ''
            word_list = stringTD.split()
            plat = False
            for wordstub in word_list:
                if wordstub == r'Material:':
                    plat = True
                    continue
                
                if wordstub == r'Test' or wordstub == r'PO':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Specimen:':
                    plat = True
                    continue
                
                
        except Exception:
            pass
    
        try:
            if number != '':

                Material = number
        except Exception:
            pass
        
        if Material.split()[-1] == '5' and Material.split()[0] == 'Titanium':
            Grade = '5'
        elif Material.split()[0] == 'Titanium':
            Grade = '23'
    
        number = ''  
        
        # Extracting Carbon Value -------------------------------------------------
        try:
            stringTD = valueCarbon[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Carbon':
                    plat = True
                    continue
                
                if plat == True:
                    number = wordstub
                    plat = False


        except Exception:
            pass
    
        try:
            if number != '':
                Carbonwt = number
                
        except Exception:
            pass
        
        number = ''
        
        # Extracting Oxygen Value -------------------------------------------------
        try:
            stringTD = valueOxygen[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Oxygen':
                    plat = True
                    continue
                
                if wordstub[0].isdigit() and plat == True:
                    number = wordstub
                    plat = False

        except Exception:
            pass
    
        try:
            if number != '':
                Oxygenwt = number
                
        except Exception:
            pass
        
        number = ''

        # Extracting Nitrogen Value -------------------------------------------------
        try:
            stringTD = valueNitrogen[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Nitrogen':
                    plat = True
                    continue
                
                if wordstub[0].isdigit() and plat == True:
                    number = wordstub
                    plat = False

        except Exception:
            pass
    
        try:
            if number != '':
                Nitrogenwt = number
                
        except Exception:
            pass
        
        number = ''
        
        # Extracting Hydrogen Value -------------------------------------------------
        try:
            stringTD = valueHydrogen[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Hydrogen':
                    plat = True
                    continue
                
                if wordstub[0].isdigit() and plat == True:
                    number = wordstub
                    plat = False

        except Exception:
            pass
    
        try:
            if number != '':
                Hydrogenwt = number
                
        except Exception:
            pass
        
        number = ''
        
        # Extracting Sulphur Value -------------------------------------------------
        try:
            stringTD = valueSulphur[0]
            number = ''
            word_list = stringTD.split()
            
            plat = False
            for wordstub in word_list:
                if wordstub == r'Sulphur':
                    plat = True
                    continue
                
                if wordstub[0].isdigit() and plat == True:
                    number = wordstub
                    plat = False

        except Exception:
            pass
    
        try:
            if number != '':
                Sulphurwt = number
        except Exception:
            pass
        
        number = ''

        

    if Recycle_count == '':
        Recycle_count = 'Vir'

    # print(WorkOrder)
    # print(BuildPlate)
    # print(PartNumber)
            
    enter_list = [Lot_number, Recycle_count, WorkOrder, BuildPlate, PartNumber, Material , Burloak_Report_number, Machine, Serial, Temp, Grade, Carbonwt , Sulphurwt , Nitrogenwt , Oxygenwt , Hydrogenwt ]
            
    return (enter_list)    

# ########################################################################################

#                         # FUNCTION DEFINITION ENDING
                                
# ########################################################################################

def PDFREADER_Density(path):
        
    
    Burloak_Report_number = '*'
    Lot_number = '*'
    Recycle_count = ''
    Material = '*'
    Machine = '*'
    Serial = '*'
    Density = []
    Grade = '*'
    Coupon = '*'
    Temp = '*'
    WorkOrder = '*'
    BuildPlate = '*'
    PartNumber = '*'
    HeatTreat = '*'
    
    page_counter = 0

    with open(path,'rb') as f:
        pdf = pdftotext.PDF(f)
    
    pattern = r"(?:Sample HT).+\b"
    pattern2 = r"(?:Heat Treatment).+\b"
    pattern9 = r"(?:Feedstock Lot \#\: ).+\b"
    pattern15 = r"(?:Material\: ).+\b"
    pattern16 = r"(?:built on ).+\b"
    pattern17 = r"(?:serial number ).+\b"
    pattern18 = r"(?:Specimen).+\b"

    
    number = ''
    for page in pdf:
        
        page_counter += 1
        

        valueHT = re.findall(pattern,page)
        valueHT2 = re.findall(pattern2,page)
        valueLot_no = re.findall(pattern9,page)
        value_material = re.findall(pattern15,page)
        value_machine = re.findall(pattern16,page)
        value_serial = re.findall(pattern17,page)
        value_info = re.findall(pattern18,page)
        
        #-------------------------------------------------------------------------
        
        #   Detecting Density 
        
        #-------------------------------------------------------------------------
        
        lines = page.splitlines()
        linecounter = 0
        parameters = [0,0]
        for line in lines:
            
            if 'Serial' in line or 'Final Density' in line:        
                # print(line)
                parameters[0] = linecounter
            
            if 'Environment at Testing' in line or 'Testing Environment' in line:        
                # print(line)
                parameters[1] = linecounter
                
            linecounter += 1
        
        if parameters[1] == 0:
            parameters[1] = linecounter
        
        linecounter = 0

        for line in lines:
            if linecounter > parameters[0] and linecounter < parameters[1]:
                wordlist = line.split()
                
                try:
                    if wordlist[-1][-1].isdigit():
                        Density.append(wordlist)
                        # print(wordlist)
                except:
                    pass
                
            linecounter += 1
        
        

        number = ''
        number1 = ''
        number2 = ''
        number3 = ''
        number4 = ''
        
        # Extracting Feedstock Lot ---------------------------------------------
        if page_counter <= 1:
            try:
                
                for stringTD in valueLot_no:
                    word_list = stringTD.split()
                    plat = False
                    write = False
    
                    
                    for wordstub in word_list:
                        if wordstub == r'#:':
                            plat = True
                            continue
                        
                        if write == True:
                            plat = False
                            
                        if plat == True:
                            try:
                                number = wordstub
                                write = True
                            except Exception:
                                pass
                        
                    
            except Exception:
                pass
            
            if 'BCP' not in number:
                Lot_number = number.split('-')[0]
                
                try:
                    for i in number.split('-')[1]:
                        if i.isdigit():
                            Recycle_count += i
                except:
                    pass
            
            else:
                Lot_number = number
            
            # try:
            #     Machine = number1 + ' ' + number2 + ' ' + number3 + ' ' + number4 + ' '
            # except Exception:
            #     pass
        
            number = '' 
            number1 = '*'    
            number2 = '*'
            number3 = '*'    
            number4 = '*'
            
        # Extracting WorkOrder Build Plate and Part Number ---------------------
        if page_counter <= 1:
            try:

                stringTD = value_info[0]
                

                wordstring = stringTD.replace("-", " ")
                wordstring = wordstring.replace(",", " ")
                wordstring = wordstring.replace(':', " ")
                word_list = wordstring.split()
                                    
                try:
                    number1 = word_list[1]
                    number2 = word_list[2]
                    number3 = word_list[3]
                    number4 = word_list[4]
                    # number5 = word_list[6]
                    
                except Exception:
                    pass
                
                    
            except Exception:
                pass
        
            try:
                WorkOrder = number1
                BuildPlate = number2 + '-' + number3
                PartNumber = number4
            except Exception:
                pass
        
            number1 = '*'    
            number2 = '*'
            number3 = '*'    
            number4 = '*'

        # Extracting Machine ---------------------------------------------
        if page_counter <= 2:
            try:

                stringTD = value_machine[0]
                

                wordstring = stringTD.replace("/", " ")
                wordstring = wordstring.replace(",", " ")
                wordstring = wordstring.replace(':', " ")
                word_list = wordstring.split()
                                    
                try:
                    number1 = word_list[2]
                    number2 = word_list[3]
                    # number3 = word_list[4]
                    # number4 = word_list[5]
                    # number5 = word_list[6]
                    
                except Exception:
                    pass
                
                    
            except Exception:
                pass
        
            try:
                Machine = number1 + ' ' + number2 + ' '     # + number3 + ' ' + number4 + ' ' + number5 + ' '
            except Exception:
                pass
        
            number1 = '*'    
            number2 = '*'
            
        # Extracting Serial ---------------------------------------------
        if page_counter <= 2:
            try:
                stringTD = value_serial[0]
                    
                
                wordstring = stringTD.replace("/", " ")
                wordstring = wordstring.replace(",", " ")
                wordstring = wordstring.replace(':', " ")
                word_list = wordstring.split()
                                    
                try:
                    number1 = word_list[2]

                    number2 = word_list[4]
                    
                except Exception:
                    pass
                    

                    
            except Exception:
                pass
        
            try:
                Serial = number1 + ' '         # + number2 + ' '  + number3 + ' ' + number4 + ' ' + number5 + ' '
            except Exception:
                pass
        
            try:
                if number2[1].isdigit():
                    Temp = number2
            except Exception:
                pass
            
            number1 = ''    
            number2 = ''
            
        # Extracting HT ---------------------------------------------
        try:

            stringTD = valueHT[0]
            number = ''
            word_list = stringTD.split()
            plat = False
            
            for wordstub in word_list:
                if r':' in wordstub :
                    plat = True
                    continue
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Condition:':
                    plat = True
                    continue
            
        except Exception:
            pass
        
        try:
            stringTD = valueHT2[0]
            word_list = stringTD.split()
            plat = False
            
            for wordstub in word_list:
                if r':' in wordstub :
                    plat = True
                    continue
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Treatment:':
                    plat = True
                    continue
            
        except Exception:
            pass
        
        try:
            if number != '':

                HeatTreat = number
        except Exception:
            pass
        
        # Extracting Material ---------------------------------------------
        try:

            stringTD = value_material[0]
            number = ''
            word_list = stringTD.split()
            plat = False
            for wordstub in word_list:
                if wordstub == r'Material:':
                    plat = True
                    continue
                
                if wordstub == r'Test' or wordstub == r'PO':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Specimen:':
                    plat = True
                    continue
                
                
        except Exception:
            pass
    
        try:
            if number != '':

                Material = number
        except Exception:
            pass
        
        if Material.split()[-1] == '5' and Material.split()[0] == 'Titanium':
            Grade = '5'
        elif Material.split()[0] == 'Titanium':
            Grade = '23'
    
        number = ''  
        


        

    if Recycle_count == '' or Recycle_count == '0' or Recycle_count == 0:
        Recycle_count = 'Vir'
        
   
     

    
    
    
    
    enter_list = [Lot_number, Recycle_count, WorkOrder, BuildPlate, PartNumber, HeatTreat, Material , Burloak_Report_number, Machine, Serial, Temp, Grade, Coupon, Density ]
            
    return (enter_list)    

    
# ########################################################################################

#                         # FUNCTION DEFINITION 
                                
# ########################################################################################

def PDFREADER_Hardness(path):
        
    
    Burloak_Report_number = '*'
    Lot_number = '*'
    Recycle_count = ''
    Material = '*'
    Machine = '*'
    Serial = '*'
    Hardness = []
    Grade = '*'
    Coupon = '*'
    Temp = '*'
    WorkOrder = ''
    BuildPlate = ''
    PartNumber = ''
    HeatTreat = '*'
    
    page_counter = 0

    with open(path,'rb') as f:
        pdf = pdftotext.PDF(f)
    
    pattern = r"(?:Sample HT).+\b"
    pattern2 = r"(?:Heat Treatment).+\b"
    pattern9 = r"(?:Feedstock Lot \#\: ).+\b"
    pattern15 = r"(?:Material\: ).+\b"
    pattern16 = r"(?:built on ).+\b"
    pattern17 = r"(?:serial number ).+\b"
    pattern18 = r"(?:Specimen).+\b"

    
    number = ''
    for page in pdf:
        
        page_counter += 1
        
        valueHT = re.findall(pattern,page)
        valueHT2 = re.findall(pattern2,page)
        valueLot_no = re.findall(pattern9,page)
        value_material = re.findall(pattern15,page)
        value_machine = re.findall(pattern16,page)
        value_serial = re.findall(pattern17,page)
        value_info = re.findall(pattern18,page)
        
        #-------------------------------------------------------------------------
        
        #   Detecting Hardness
        
        #-------------------------------------------------------------------------
        
        lines = page.splitlines()
        linecounter = 0
        parameters = [0,0]
        for line in lines:
            
            if 'Hardness' in line and ('Scale' in line or 'Serial' in line) :

                parameters[0] = linecounter
            
            if 'Environment at Testing' in line or 'Testing Environment' in line:        

                parameters[1] = linecounter
                
            linecounter += 1
        
        
        if parameters[1] == 0:
            parameters[1] = linecounter
        
        
        linecounter = 0

        for line in lines:
            if linecounter > parameters[0] and linecounter < parameters[1]:
                
                liner = line.replace(',',' ')
                wordlist = liner.split()
                Hardness.append(wordlist)

                
            linecounter += 1
        


        number = ''
        number1 = ''
        number2 = ''
        number3 = ''
        number4 = ''
        
        # Extracting Feedstock Lot ---------------------------------------------
        if page_counter <= 1:
            try:
                
                for stringTD in valueLot_no:
                    word_list = stringTD.split()
                    plat = False
                    write = False
    
                    
                    for wordstub in word_list:
                        if wordstub == r'#:':
                            plat = True
                            continue
                        
                        if write == True:
                            plat = False
                            
                        if plat == True:
                            try:
                                number = wordstub
                                write = True
                            except Exception:
                                pass
                        
                    
            except Exception:
                pass
            
            if 'BCP' not in number:
                Lot_number = number.split('-')[0]
                
                try:
                    for i in number.split('-')[1]:
                        if i.isdigit():
                            Recycle_count += i
                except:
                    pass
            
            else:
                Lot_number = number
            
            # try:
            #     Machine = number1 + ' ' + number2 + ' ' + number3 + ' ' + number4 + ' '
            # except Exception:
            #     pass
        
            number = '' 
            number1 = ''    
            number2 = ''
            number3 = ''    
            number4 = ''            
            
        # Extracting Work Order, BTI and Part number---------------------------------------------
        if page_counter <= 1:

            stringTD = value_info[0]
                
            stringTD = stringTD.split('Job')[0]
            wordstring = stringTD.replace(",", " ")
            wordstring = wordstring.replace('-', " ")
            wordstring = wordstring.replace(':', " ")
            word_list = wordstring.split()

                
            mode = 0
            for i in range(len(word_list)):
                if word_list[i] == 'Feedstock':
                    break
                if word_list[i] == 'Specimen':
                    continue
                elif word_list[i] == 'ID':
                    continue
                elif 'BTI20' in word_list[i]:
                    BuildPlate += word_list[i]
                    i += 1
                    BuildPlate += '-' + word_list[i] 
                    mode = 1
                    i += 1 
                    PartNumber += word_list[i]
                if mode == 1:
                    PartNumber += '-' + word_list[i]
                else:
                    WorkOrder += word_list[i]
        
        try:
            if PartNumber[-2] == '(' or PartNumber[-3] == '(' :
                PartNumber += ')'            
        
        except:
            pass
        
        
        number1 = ''
        number2 = ''
        number3 = ''
        number4 = ''
        number = ''
        # Extracting Machine and Serial---------------------------------------------
        if page_counter <= 1:
            try:
                for stringTD in value_machine:
                    

                    wordstring = stringTD.replace("/", " ")
                    wordstring = wordstring.replace(",", " ")
                    wordstring = wordstring.replace(':', " ")
                    word_list = wordstring.split()
                                        
                    try:
                        number1 = word_list[2]
                        number2 = word_list[3]
                        number3 = word_list[5]
                        number4 = word_list[7]
                        if number4 == 'at':
                            number4 = word_list[8]
                        if number3 == 'number':
                            number3 = word_list[6]
                        
                        
                        
                    except Exception:
                        pass
                    
            except Exception:
                pass
        
            try:
                Machine = number1 + ' ' + number2 + ' '
                Serial = number3
                Temp = number4
            except Exception:
                pass
        
            number = ''    
            
        # Extracting HT ---------------------------------------------
        try:

            stringTD = valueHT[0]
            number = ''
            word_list = stringTD.split()
            plat = False
            
            for wordstub in word_list:
                if r':' in wordstub :
                    plat = True
                    continue
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Condition:':
                    plat = True
                    continue
            
        except Exception:
            pass
        
        try:
            stringTD = valueHT2[0]
            word_list = stringTD.split()
            plat = False
            
            for wordstub in word_list:
                if r':' in wordstub :
                    plat = True
                    continue
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Treatment:':
                    plat = True
                    continue
            
        except Exception:
            pass
        
        try:
            if number != '':

                HeatTreat = number
        except Exception:
            pass
        
        # Extracting Material ---------------------------------------------
        try:

            stringTD = value_material[0]
            number = ''
            word_list = stringTD.split()
            plat = False
            for wordstub in word_list:
                if wordstub == r'Material:':
                    plat = True
                    continue
                
                if wordstub == r'Test' or wordstub == r'PO':
                    plat = False
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Specimen:':
                    plat = True
                    continue
                
                
        except Exception:
            pass
    
        try:
            if number != '':

                Material = number
        except Exception:
            pass
        
        if Material.split()[-1] == '5' and Material.split()[0] == 'Titanium':
            Grade = '5'
        elif Material.split()[0] == 'Titanium':
            Grade = '23'
    
        number = ''  
        


        

    if Recycle_count == '' or Recycle_count == '0' or Recycle_count == 0:
        Recycle_count = 'Vir'
        
   
     

    
    
    # print(Hardness)
    
    enter_list = [Lot_number, Recycle_count, WorkOrder, BuildPlate, PartNumber, HeatTreat, Material , Burloak_Report_number, Machine, Serial, Temp, Grade, Hardness ]
            
    return (enter_list)    

    
# ########################################################################################

#                         # FUNCTION DEFINITION 
                                
# ########################################################################################

def PDFREADER_Fatigue(path):
        
    
    WorkOrder = ''
    SpecimenID = ''
    SerialNumber = ''
    Printer = ''
    SurfaceFinish = ''
    HeatTreatment = ''
    Rq = ''
    AvgDiameter = ''
    Material = ''
    HIPHeatTreat = ''
    InitForce = ''
    R_Ratio= ''
    Frequency = ''
    Cyclespstep = ''
    ForceIncStep = ''
    MaxSafeLifeLoad = ''
    MaxFracLoad = ''
    Cycles = []
    FatigueLimit = ''
    
    page_counter = 0

    with open(path,'rb') as f:
        pdf = pdftotext.PDF(f)
    

    # left column    

    patternwo = r"(?:Work Order).+\b"
    patternsi = r"(?:Specimen ID).+\b"
    patternsn = r"(?:Serial Number).+\b"
    patternp = r"(?:Printer).+\b"
    patternsf = r"(?:Surface Finish).+\b"
    patternht = r"(?:Heat Treatment).+\b"
    
    # right column
    
    patternrq = r"(?:Rq).+\b"
    patternad = r"(?:Average Diameter).+\b"
    patternm = r"(?:Material).+\b"
    patternhht = r"(?:HIP & Heat Treatment).+\b"
    patterndet = r"(?:Details).+\b"    
    patternhed = r"(?:HIP'ed).+\b"    
    
    # Test Parameters
    
    patternif = r"(?:Initial Force).+\b"
    patternrr = r"(?:R Ratio).+\b"
    patternf = r"(?:Frequency).+\b"
    patterncps = r"(?:Cycles per Step).+\b"
    patternfips = r"(?:Force Increment per Step).+\b"
    patternmsl = r"(?:Max Safe Life Load).+\b"
    patternmfl = r"(?:Max Load at Fracture).+\b"

    
    number = ''
    for page in pdf:

        

        page_counter += 1
        
        value_workorder = re.findall(patternwo,page)
        value_specimenID = re.findall(patternsi,page)
        value_serial = re.findall(patternsn,page)
        value_printer = re.findall(patternp,page)
        value_surface = re.findall(patternsf,page)
        value_heattreat = re.findall(patternht,page)
        
        value_rq = re.findall(patternrq,page)
        value_avgdiameter = re.findall(patternad,page)
        value_material = re.findall(patternm,page)
        value_hipheattreat = re.findall(patternhht,page)
        value_details = re.findall(patterndet,page)
        value_hed = re.findall(patternhed,page)
        
        value_initforce = re.findall(patternif,page)
        value_rratio = re.findall(patternrr,page)
        value_frequency = re.findall(patternf,page)
        value_cycles = re.findall(patterncps,page)
        value_forceinc = re.findall(patternfips,page)
        value_maxsafe = re.findall(patternmsl,page)
        value_maxfrac = re.findall(patternmfl,page)
        
        

        
                        
        # Extracting Work Order ---------------------------------------------
        if page_counter <= 1:
            try:
    
                stringTD = value_workorder[0]
                number = ''
                word_list = stringTD.split()
                plat = False
                for wordstub in word_list:
                    if wordstub == r'Order':
                        plat = True
                        continue
                    
                    # if wordstub == r'Test' or wordstub == r'PO':
                    #     plat = False
                        
                    if plat == True:
                        try:
                            number = wordstub
                            plat = False
                        except Exception:
                            pass
                    # if wordstub == r'Specimen:':
                        # plat = True
                        # continue
                    
                    
            except Exception:
                pass
        
            try:
                if number != '':
    
                    WorkOrder = number
                    
            except Exception:
                pass
            
        number = ''  
        
        # Extracting Specimen ID ---------------------------------------------
        if page_counter <= 1:
            try:
    
                stringTD = value_specimenID[0]
                number = ''
                word_list = stringTD.split()
                plat = False
                for wordstub in word_list:
                    if wordstub == r'ID':
                        plat = True
                        continue
                    
                    if wordstub == r'Est.' or wordstub == r"Young's":
                        plat = False
                        
                    if plat == True:
                        try:
                            number += wordstub
                        except Exception:
                            pass
                    # if wordstub == r'Specimen:':
                        # plat = True
                        # continue
                    
                    
            except Exception:
                pass
        
            try:
                if number != '':
    
                    SpecimenID = number
                    
            except Exception:
                pass
            
        number = ''
        # Extracting Serial Number ---------------------------------------------
        if page_counter <= 1:
            try:
                stringTD = value_serial[0]
                number = ''
                word_list = stringTD.split()
                plat = False
                for wordstub in word_list:
                    if wordstub == r'Number':
                        plat = True
                        continue
                    
                    if wordstub == r'Est.' or wordstub == r"Yield":
                        plat = False
                        
                    if plat == True:
                        try:
                            number += wordstub
                        except Exception:
                            pass
                    # if wordstub == r'Specimen:':
                        # plat = True
                        # continue
                    
                    
            except Exception:
                pass
        
            try:
                if number != '':
    
                    SerialNumber = number
                    
            except Exception:
                pass
            
        number = ''
        
        # Extracting Printer ---------------------------------------------
        if page_counter <= 1:
            try:
                stringTD = value_printer[0]
                number = ''
                word_list = stringTD.split()
                plat = False
                for wordstub in word_list:
                    if wordstub == r'Printer':
                        plat = True
                        continue
                    
                    if wordstub == r'HIP' or wordstub == r"&":
                        plat = False
                        
                    if plat == True:
                        try:
                            number += (wordstub + ' ')
                        except Exception:
                            pass
                    # if wordstub == r'Specimen:':
                        # plat = True
                        # continue
                    
                    
            except Exception:
                pass
        
            try:
                if number != '':
    
                    Printer = number
                    
            except Exception:
                pass
            
        number = ''
        
        # Extracting Surface Finish ---------------------------------------------
        if page_counter <= 1:
            try:
                stringTD = value_surface[0]
                number = ''
                word_list = stringTD.split()
                plat = False
                for wordstub in word_list:
                    if wordstub == r'Finish':
                        plat = True
                        continue
                    
                    if wordstub == r'Details':
                        plat = False
                                        
                    if wordstub == r'Machined':
                        try:
                            number += (wordstub + ' ')
                        except Exception:
                            pass
                        plat = False
                        
                    if plat == True:
                        try:
                            number += (wordstub + ' ')
                        except Exception:
                            pass
                    # if wordstub == r'Specimen:':
                        # plat = True
                        # continue
                    
                    
            except Exception:
                pass
        
            try:
                if number != '':
    
                    SurfaceFinish = number
                    
            except Exception:
                pass
            
        number = ''
        
        # Extracting Heat Treatment ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_heattreat:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Treatment':
                            plat = True
                            continue
                        
                        if wordstub == r'(SR+HIP+SA+AGE':
                            number += wordstub + ')'
                            plat = False
                            continue
                        
                        if plat == True:
                            try:
                                number += wordstub + ' '
                            except Exception:
                                pass
                        
                        if wordstub == r'Annealed' or wordstub == r'Relieved':
                            plat = False
                            continue
                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        HeatTreatment = number

                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting Rq ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_rq:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Rq':
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub
                            except Exception:
                                pass

                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        Rq = number

                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting Average Diameter ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_avgdiameter:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Diameter':
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub
                            except Exception:
                                pass

                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        AvgDiameter = number

                except Exception:
                    pass
            
        number = ''
        
        # Extracting Material ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_material:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Material':
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub
                            except Exception:
                                pass

                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        Material = number
                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting HIP & Heat Treatment ---------------------------------------------
        if page_counter <= 1:

            for stringTD in value_hipheattreat:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Treatment':
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub + ' '
                            except Exception:
                                pass                                
                except Exception:
                    pass
            
            stringTD = value_details
            if stringTD:
                try:
                    word_list = stringTD[0].split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Details':
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub + ' '
                            except Exception:
                                pass  
                            
                    word_list = value_hed[0].split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r"HIP'ed":
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub + ' '
                            except Exception:
                                pass  
                              
                except Exception:
                    pass
        
            try:
                if number != '':
    
                    HIPHeatTreat = number

            except Exception:
                pass
            
        number = ''
        
        # Extracting Initial Force ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_initforce:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = 0
                    for wordstub in word_list:
                        
                        if wordstub == r'Force':
                            plat = 1
                            continue
                        
                        if plat == 2:
                            try:
                                number += ' ' + wordstub
                            except:
                                pass
                            break                        
                        
                        if plat == 1:
                            try:
                                number = wordstub
                            except Exception:
                                pass
                            plat = 2
            
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        InitForce = number
                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting R Ratio ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_rratio:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Ratio':
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub
                            except Exception:
                                pass
                            break

                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        R_Ratio = number
                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting Frequency ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_frequency:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = 0
                    for wordstub in word_list:
                        
                        if wordstub == r'Frequency':
                            plat = 1
                            continue
                        
                        if plat == 2:
                            try:
                                number += ' ' + wordstub
                            except:
                                pass
                            break                        
                        
                        if plat == 1:
                            try:
                                number = wordstub
                            except Exception:
                                pass
                            plat = 2
            
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        Frequency = number
                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting Cycles per Step ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_cycles:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = 0
                    for wordstub in word_list:
                        
                        if wordstub == r'Step':
                            plat = 1
                            continue
                        
                        if plat == 2:
                            try:
                                number += ' ' + wordstub
                            except:
                                pass
                            break                        
                        
                        if plat == 1:
                            try:
                                number = wordstub
                            except Exception:
                                pass
                            plat = 2
            
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        Cyclespstep = number
                        
                except Exception:
                    pass
            
        number = ''
        
        # Force Increment per step ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_forceinc:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = 0
                    for wordstub in word_list:
                        
                        if wordstub == r'Step':
                            plat = 1
                            continue
                                           
                        
                        if plat == 1:
                            try:
                                number = wordstub + ' %'
                            except Exception:
                                pass
                            plat = 2
            
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        ForceIncStep = number
                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting Max Safe life load ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_maxsafe:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Load':
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub + ' '
                            except Exception:
                                pass

                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        MaxSafeLifeLoad = number

                        
                except Exception:
                    pass
            
        number = ''
        
        # Extracting Max load at fracture ---------------------------------------------
        if page_counter <= 1:
            
            for stringTD in value_maxfrac:
                try:
                    number = ''
                    word_list = stringTD.split()
                    plat = False
                    for wordstub in word_list:
                        
                        if wordstub == r'Fracture':
                            plat = True
                            continue
                                                
                        if plat == True:
                            try:
                                number += wordstub + ' '
                            except Exception:
                                pass

                                                    
                except Exception:
                    pass
        
                try:
                    if number != '':
        
                        MaxFracLoad = number
                        
                except Exception:
                    pass
            
        number = ''
        
        #-------------------------------------------------------------------------
        
        #   fatigue life
        
        #-------------------------------------------------------------------------
        
        lines = page.splitlines()
        linecounter = 0
        parameters = [0,0]
        for line in lines:
            
            if 'Step' in line or 'Cycles' in line:        
                # print(line)
                parameters[0] = linecounter
            
            if 'Operated' in line or 'Approved' in line:        
                # print(line)
                parameters[1] = linecounter
                
            linecounter += 1
        
        if parameters[1] == 0:
            parameters[1] = linecounter
        
        linecounter = 0

        for line in lines:
            if linecounter > parameters[0] and linecounter < parameters[1]:
                wordlist = line.split()
                
                try:
                    if wordlist[-1][-1].isdigit():
                        Cycles.append(wordlist)
                except:
                    pass
                
            linecounter += 1
                
         
        maxstresssafe = float(Cycles[-2][-3])
        maxstressfrac = float(Cycles[-1][-3])
        cyclesafe = float(Cycles[-2][-1].replace(',',''))
        cyclefrac = float(Cycles[-1][-1].replace(',',''))
        
        
        fatiguelimit = maxstresssafe + ((maxstressfrac - maxstresssafe)*(cyclefrac/cyclesafe))
        
        FatigueLimit = str(fatiguelimit) + ' ' + MaxFracLoad.split()[-1]

        
        
    # if Recycle_count == '' or Recycle_count == '0' or Recycle_count == 0:
    #     Recycle_count = 'Vir'
    
    enter_list = ['',WorkOrder,SpecimenID,SerialNumber,Printer,SurfaceFinish,HeatTreatment,Rq,AvgDiameter,Material,HIPHeatTreat,InitForce,R_Ratio,Frequency,Cyclespstep,ForceIncStep,MaxSafeLifeLoad,MaxFracLoad,FatigueLimit]
            
    return (enter_list)    

def PDFREADER_HTpuller(path):
    
    HeatTreat = '*'
    page_counter = 0

    with open(path,'rb') as f:
        pdf = pdftotext.PDF(f)
    

    pattern = r"(?:Sample HT).+\b"
    pattern2 = r"(?:Heat Treatment).+\b"

    
    number = ''
    for page in pdf:
        
        page_counter += 1
        
        valueHT = re.findall(pattern,page)
        valueHT2 = re.findall(pattern2,page)
        
        # Extracting HT ---------------------------------------------
        try:

            stringTD = valueHT[0]
            number = ''
            word_list = stringTD.split()
            plat = False
            
            for wordstub in word_list:
                if r':' in wordstub :
                    plat = True
                    continue
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Condition:':
                    plat = True
                    continue
            
        except Exception:
            pass
        
        try:
            stringTD = valueHT2[0]
            word_list = stringTD.split()
            plat = False
            
            for wordstub in word_list:
                if r':' in wordstub :
                    plat = True
                    continue
                    
                if plat == True:
                    try:
                        number += wordstub + ' '
                    except Exception:
                        pass
                if wordstub == r'Treatment:':
                    plat = True
                    continue
            
        except Exception:
            pass
        
        print(number)
                
        