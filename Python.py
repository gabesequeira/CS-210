import re
import string
from collections import Counter


def printList():
    openFile = open (os.path.join(sys.path[0], "my_file.txt"), "r")
    myList = openFile.read()
    openFile.close()
    
    # break the string into list of words 
    myList = myList.split()         
    emptyList = []
  
    # loop until string values present in list
    for i in myList:             
  
        # checking for duplicacy
        if i not in emptyList:
  
            # insert value in emptyList
            emptyList.append(i) 
              
    for i in range(0, len(emptyList)):
  
        # count the frequency of each word and print
        print(emptyList[i], myList.count(emptyList[i]))  


def freq(v):
    openFile = open (os.path.join(sys.path[0], "my_file.txt"), "r")
    myList = openFile.read()
    
    return myList.count(v);

def histo():
    openFile = open (os.path.join(sys.path[0], "my_file.txt"), "r")
    myList = openFile.read()
    wHistogram = open ("frequency.dat", "x")
    
    # break the string into list of words 
    myList = myList.split()         
    str2 = []
  
    # loop till string values present in list
    for i in myList:             
  
        # checking for duplicacy
        if i not in str2:
  
            # insert value in str2
            str2.append(i) 

    for i in range(0, len(str2)):
  
        # count the frequency of each word and write
        wHistogram.write(str2[i])
        wHistogram.write(" ")
        test = myList.count(str2[i])
        wHistogram.write(str(test))
        wHistogram.write("\n")
    
    # close the file
    wHistogram.close()

    # open the newly created file
    xHistogram = open("frequency.dat", "r")

    #loop and print histogram from file
    for i in range(0, len(str2)):
        rHistogram = xHistogram.readline()
        rHistogram = rHistogram.split()
        print(rHistogram[0], int(rHistogram[1]) * "*")

def inputValidation():
    # print message so user knows the correct input options
    print("Please enter your selection as a number 1, 2, 3, or 4")
