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
            
    def SearchEmp(self, EId):
        Emp = None
        if self is not None:
            if int(self.EmpId) == int(EId):
                Emp = self
            if Emp is None and self.left is not None:
                Emp = self.left.SearchEmp(EId)
            if Emp is None and self.right is not None:
                Emp = self.right.SearchEmp(EId)
        return Emp
 
 
    def EmpCount(self):
        count = 0
        if self is not None:
            count = 1
            if self.left is not None:
                count += self.left.EmpCount()
            if self.right is not None:
                count += self.right.EmpCount()
        return count
    
    
    def SearchEmpMostSwiped(self, count):
        Emp = None        
        if self is not None:
            if int(self.attCtr) > int(count):
                count = self.attCtr
                Emp = self
            if self.left is not None:
                Emp = self.left.SearchEmpMostSwiped(count) or Emp
            if self.right is not None:
                Emp = self.right.SearchEmpMostSwiped(count) or Emp
        return Emp
    
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