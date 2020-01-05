# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:06:31 2019

@author: agupt84
"""

class EmpNode:
    def __init__(self, EId):
        self.EmpId= EId #Employee ID
        self.attCtr= 1  #Attendance counter
        self.left = None
        self.right= None

    def insert(self, EId):
        if self.EmpId:
            if EId < self.EmpId:
                if self.left is None:
                    self.left = EmpNode(EId)
                else:
                    self.left.insert(EId)
            elif EId > self.EmpId:
                if self.right is None:
                    self.right = EmpNode(EId)
                else:
                    self.right.insert(EId)
            elif EId == self.EmpId:
                self.attCtr += 1
        else:
            self.EmpId = EmpNode(EId)
            print ('1', self.EmpId, self.attCtr, self.left, self.right)