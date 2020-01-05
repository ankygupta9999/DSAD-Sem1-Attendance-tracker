# -*- coding: utf-8 -*-
#!/usr/bin/env python
# coding: utf-8

# Importing libraries
import EmpNode

class attendance_tracker:
    
    EmpId = None  #??? Doubt
    attCtr = None
    left = None
    right = None
    
    def _readEmployeesRec(self, eNode, Eid):
        '''This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises. 
        One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit). 
        The input data is used to populate the tree. If the employee id is already added to the tree, 
        then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file. 
        Use a trigger function to call this recursive function from the root node.
        '''
        # Initial node (root node) indicator
#        initialNode = True
        # Open Employeed Rec file
        attFile = open(r'..\data\inputPS1.txt','r')
        for line in attFile.readlines():
            print (line)
#            if initialNode:
#                EmpNode(line)
#            else:
            EmpNode.EmpNode.insert(self, int(line))
            
    

if __name__ == "__main__":
    eNode = 1 # Root node
    Eid = 0
    
#    emp = EmpNode(self, Eid)
    tracker = attendance_tracker()
    tracker._readEmployeesRec(eNode, Eid)
    