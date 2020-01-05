# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:06:31 2019

@author: DSAD Group 41
"""

class EmpNode:
    def __init__(self, EId):
        self.EmpId= EId #Employee ID
        self.attCtr= 1  #Attendance counter
        self.left = None
        self.right= None
        'print("inserting into parent node - " + str(EId))'
    
    # Store new Employee record or increment the counter for existing Employee
    def RecordAttendance(self, EId):
        " print('EId - ' + str(EId))"
        " print('EmpId - ' + str(self.EmpId))"
        if self.EmpId:            
            if EId < self.EmpId:
                if self.left is None:
                    'print("inserting into left node - " + str(EId))'
                    self.left = EmpNode(EId)
                else:
                    self.left.RecordAttendance(EId)
            elif EId > self.EmpId:
                if self.right is None:
                    'print("inserting into right node - " + str(EId))'
                    self.right = EmpNode(EId)
                else:
                    self.right.RecordAttendance(EId)
            elif EId == self.EmpId:
                self.attCtr += 1
                'print("Counter (" + str(self.attCtr) +")incremented for- " + str(EId))'
        else:
            self.EmpId = EmpNode(EId)
            " print ('1', self.EmpId, self.attCtr, self.left, self.right)"
            
    # Print the Employee List
    def PrintEmpList(self):
        if self.left:
            self.left.PrintEmpList()
        print(str(self.EmpId) + ", " + str(self.attCtr)),
        if self.right:
            self.right.PrintEmpList()
            
        # Print tree structure
    def PrintEmpTree(self,pTree,pos,spaces):
        if pos == "c":
            pTree = pTree + spaces + str(self.EmpId) + " [" + str(self.attCtr) + "]"
        elif pos == "l":
            pTree = pTree + "\n" + spaces + "/   " + "\n"
            spaces = spaces[4:]
            pTree = pTree + spaces + str(self.EmpId) + " [" + str(self.attCtr) + "]"
        elif pos == "r":
            pTree = pTree + "\n" + spaces + "\\"  + "\n"
            spaces = spaces + "  "
            pTree = pTree + spaces + str(self.EmpId) + " [" + str(self.attCtr) + "]"
        
        if self.left:
            pos = "l"
            self.left.PrintEmpTree(pTree, pos, spaces)

        if self.right:
            pos = "r"
            self.right.PrintEmpTree(pTree, pos, spaces)

        if (self.left == None) and (self.right == None):
            print ("==== Below is the Left (first) and then Right part of the tree built ====")
            print( pTree)

    def SearchEmployee(self, EId):
        if self is not None & self.EmpId == EId:
            return self
        if self.left is not None:
            return self.left.search(EId)
        if self.right is not None:
            return self.right.search(EId)
        return None
 
 
    def EmpCount(self):
        if self is None:
            return 0
        return 1 + EmpCount(self.left) + EmpCount(self.right)