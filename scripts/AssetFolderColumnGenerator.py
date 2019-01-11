import os
from os import listdir
from os.path import isfile,join
import csv
import unittest

CustomModulesFolderPath = '..\..\custom modules'

#Generates a CSV table with the module names and empty columns otherwise
def getCustomModulesList():
    resultFile=open("CustomModulesList.csv","w+")
    #Put the headers in this write statement.
    #Right now the header entry will be dumb, only as user inputs
    resultFile.write("asset folder,module name,source,profiles\n")
    directories = os.listdir(CustomModulesFolderPath)
    for item in directories:
        newLines= item+",,,[]\n"
        #print newLines
        resultFile.write(newLines)

    resultFile.close()
    print "A CSV table with 4 columns has been created.\n"
    print "You can find it in this directory as - CustomModulesList.csv\n"
#Should find all folders named 'custom_modules'
def findModuleFolders() :
    #NOTE: Change this to UniviewFolderPath='../../' for real implementation
    UniviewFolderPath = '../../../'
    os.chdir(UniviewFolderPath)
    #directories = filter(os.path.isdir, os.listdir('.'))
    allSubdirectories = os.walk(".", topdown=True)
    print type(allSubdirectories)

    customModuleFolderPaths=[]
    profileFolderPaths=[]
    #This is going to take a long time to scan ALL the folders in bcb/Uniview
    for root, directories, files in allSubdirectories:
        for name in directories:
            if name.lower()=='custom modules':
                customModuleFolderPaths.append(os.path.join(root,name))
            if name.lower()=='profiles':
                profileFolderPaths.append(os.path.join(root,name))
    #a list of all folders with custom modules
    print customModuleFolderPaths
    #a list of all folders name 'profiles'
    print profileFolderPaths
    
    #Walk through bcb/Uniview and
    #look for all folders called 'custom modules'
    #Create [] of such folder paths

    #For each folder path in [],
    #Get the module folder name,
    #If it already exists, add the folder path to csv[folder path]
    #If it doesn't exist, create a new csv row and fill in csv[asset folder] and csv [folder path]

    #Check for modules with description.html
    #Strip the module name if available, add to csv column (matching by folder name as key)
findModuleFolders()


#Should get the profiles where modules were used.
#def getProfiles():
    #Walk through bcb/Uniview and
    #Look for folders named 'profiles'
    #Create [] of such folder paths + /././Modules/autorun.mod
    #For each in [], check that there is an autorun.mod file
    #map [] so that only folder paths w autorun.mod are remaining
    #Get the asset folder names from the autorun.mod files
    #check csv if module exists in csv[asset folde]
    #if exists, write to csv[profiles]
    #if does not exist, create a new line with the module name and csv[profiles]

#def csvtoJS():
    #Convert the final CSV to JavaScript Object and output to the screen. 
    
#Prints out the JS object, ready to be pasted into the index.html table
    #Might be able to just delete this
"""
def convertCSVtoJSFormat():
    result=[]
    with open("CustomModulesList.csv", "rb") as f:
        eachline='var dataSet = [';
        reader=csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            eachline+=str(line)+",\n"
            #print '{},'.format(line)
            #print eachline
        #remove the last comma
        eachline=eachline[:-2]
        #Add in a closing bracket for the dataset
        eachline+="]"
        print eachline
"""

