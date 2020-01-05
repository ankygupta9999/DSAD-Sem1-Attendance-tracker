# -*- coding: utf-8 -*-
#!/usr/bin/env python
# coding: utf-8
"""
@author: DSAD Group 41
"""
# Importing libraries
import EmpNode

class attendance_tracker:
    
    
    def _readEmployeesRec(self, eNode, Eid):
        '''This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises. 
        One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit). 
        The input data is used to populate the tree. If the employee id is already added to the tree, 
        then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file. 
        Use a trigger function to call this recursive function from the root node.
        '''
        if(eNode is None):
            eNode = EmpNode.EmpNode(Eid)
        else:
            eNode.RecordAttendance(Eid)
        return eNode   
    
    def printRangePresent(self, StartId, EndId):
        '''This function prints the employee ids in the range StartId to EndId and 
        how often they have entered the organization in a file name outputPS1.txt.
        '''
        

if __name__ == "__main__":
    Eid = 0
    eNode = None
     # Root node
    
    # Creating instance of Main class
    tracker = attendance_tracker()
    
    # Reading inputPS1 file to load the day's swipe in/out data and populate the Binary Tree
    attFile = open(r'data\inputPS1.txt','r')
    for employee in attFile.readlines():
        'print (employee)'
        eNode = tracker._readEmployeesRec(eNode, int(employee))
    eNode.PrintEmpList()
    # Below is just to visualize the Tree 
    eNode.PrintEmpTree("","c","                      ")
    
    # Reading promptsPS1.txt file to see what report is needed and accordingly call the respective function:
    rptFile = open(r'data\promptPS1.txt','r')
    for report in rptFile.readlines():
        rptCat = report.split(':')
        if rptCat[0] == "range":
            print ("range report")
            tracker.printRangePresent(rptCat[1],rptCat[2])
        elif rptCat[0] == "searchID":
            print ("Replace this with call to search ID method here")
        elif rptCat[0] == "howOften":
            print ("Replace this with call to how Often method here")
        elif rptCat[0] == "frequentVisitor":
            print ("Replace this with call to frequentMethod method here")
        elif rptCat[0] == "headCount":
            print ("Replace this with call to headCount method here")