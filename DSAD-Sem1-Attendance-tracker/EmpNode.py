# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:06:31 2019

@author: DSAD Group 41
@contribution:
    Team Member     Roll Number
    ===========================
    Ankit Gupta     2019ad04026
    Hitesh Gupta	2019ad04027
    Aditya Mehta	2019ad04031
    Prateek Sirohi	2019ad04032
"""

class EmpNode:
    def __init__(self, EId):
        self.EmpId= EId #Employee ID
        self.attCtr= 1  #Attendance counter
        self.left = None
        self.right= None
    
    # Store new Employee record or increment the counter for existing Employee
    def RecordAttendance(self, EId):
        if self.EmpId:            
            if EId < self.EmpId:
                if self.left is None:
                    self.left = EmpNode(EId)
                else:
                    self.left.RecordAttendance(EId)
            elif EId > self.EmpId:
                if self.right is None:
                    self.right = EmpNode(EId)
                else:
                    self.right.RecordAttendance(EId)
            elif EId == self.EmpId:
                self.attCtr += 1
        else:
            self.EmpId = EmpNode(EId)
            
    def SearchEmp(self, EId):
        Emp = None
        
        if int(EId) == int(self.EmpId):
            Emp = self
        else:            
            if int(EId) < int(self.EmpId):
                if self.left is not None:
                    Emp = self.left.SearchEmp(EId)
            elif int(EId) > int(self.EmpId):
                if self.right is not None:
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