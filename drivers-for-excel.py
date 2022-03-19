#excel Drivers
import pandas as pd

def savetoexcel(mat:dict):
    withitems=pd.DataFrame(mat.items(),columns=['nombre','bot id'])
    withitems.to_excel('/home/pi/Desktop/saved_file.xlsx', index = False)

def readexcel():
    hardcodedPath="/home/pi/Desktop/saved_file.xlsx"
    dict = pd.read_excel(hardcodedPath)
    return dict

if __name__ == '__main__':
    #name 4 testing
    mydict={}
    mydict['manu']="5178063489"
    mydict['jose']="220619299"
    while True:
        a=readexcel()

#reads excel and adds value    
#hardcodedPath="/home/pi/Desktop/saved_file.xlsx"
#dict = pd.read_excel(hardcodedPath,usecols=['nombre','bot id'])

#print(dict.keys())
#mydict['new']="47686414"

#withitems=pd.DataFrame(mydict.items(),columns=['nombre','bot id'])
#withitems.to_excel('/home/pi/Desktop/saved_file.xlsx', index = False)