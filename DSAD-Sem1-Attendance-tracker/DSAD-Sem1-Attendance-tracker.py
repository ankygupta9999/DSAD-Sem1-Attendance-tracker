# -*- coding: utf-8 -*-
#!/usr/bin/env python
# coding: utf-8

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
    

if __name__ == "__main__":
    Eid = 0
    eNode = None
     # Root node
    
    tracker = attendance_tracker()
    attFile = open(r'data\inputPS1.txt','r')
    for employee in attFile.readlines():
        'print (employee)'
        eNode = tracker._readEmployeesRec(eNode, int(employee))
    eNode.PrintEmpList()