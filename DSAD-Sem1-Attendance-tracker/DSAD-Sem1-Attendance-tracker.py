# -*- coding: utf-8 -*-
#!/usr/bin/env python
# coding: utf-8
"""
@author: DSAD Group 41
"""
# Importing libraries
import EmpNode

class attendance_tracker:
    
    def _getAction(self, action):
        switcher = {
            "searchID": "_searchIDRec",
            "howOften": "_howOften_Rec",
            "range": "printRangePresent",
            }
        # Get the function from switcher dictionary
        func = switcher.get(action, lambda: "Invalid action")
        # Execute the function
        return func

    def _invokeMethod(self, argument, eNode, EId):
        """Dispatch method"""
        method_name = self._getAction(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid action")
        # Call the method as we return it
        return method(eNode, EId)

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
    
    def _getHeadcountRec(self, eNode):
        '''
        This function counts the number of unique IDs stored in the tree and prints the employee headcount for the day into the output.txt file as shown below.
        Total number of employees today: xx
        Use a trigger function to call this recursive function from the root node.
        '''
        print('Total number of employees today: ' + str(eNode.EmpCount()))
        
    
    def _searchIDRec(self, eNode, EId):
        '''
        This function searches whether a particular employee has attended today or not. The function reads the search id from the file promptsPS1.txt where the search id is mentioned with the tag as shown below.
        searchID:23
        searchID:22
        searchID:11
        The search function is called for every searchID tag the program finds in the promptsPS1.txt file.
        If the employee id is found it outputs the below string into the outputPS1.txt file
        Employee id xx is present today.
        If the employee id is not found it outputs the below string into the outputPS1.txt file
        Employee id xx is absent today.
        Use a trigger function to call this recursive function from the root node.
        '''
        Emp = eNode.SearchEmp(EId) 
        message = 'Employee id ' + str(EId).rstrip("\n\r") + ' is absent today.'
        if Emp is not None and Emp.EmpId is not None:
            message = 'Employee id ' + str(EId).rstrip("\n\r") + ' is present today.'
        print(message)

    def _howOften_Rec(self, eNode, EId):
        '''
        This function counts the number of times a particular employee swiped today and if the employee is currently in the office or outside.
        The function reads the id from the file promptsPS1.txt where the search id is mentioned with the tag as shown below.
        howOften:12
        howOften:22
        howOften:11
        The search function is called for every howOften tag the program finds in the promptsPS1.txt file.
        If the employee id is found with an odd attendance count the below string is output into the outputPS1.txt file
        Employee id xx swiped yy times today and is currently in office
        If the employee id is found with an even attendance count the below string is output into the outputPS1.txt file
        Employee id xx swiped yy times today and is currently outside office
        If the employee id is not found it outputs the below string into the outputPS1.txt file
        Employee id xx did not swipe today.
        '''
        message = 'Employee id ' + str(EId).rstrip("\n\r") + ' did not swipe today.'
        Emp = eNode.SearchEmp(EId) 
        if Emp is not None and Emp.EmpId is not None:
            message = 'Employee id ' + str(Emp.EmpId).rstrip("\n\r")
            message += ' swiped ' + str(Emp.attCtr).rstrip("\n\r") + ' times today'
            message += ' and is currently ' + ('outside'  if Emp.attCtr%2 == 0 else 'in') + ' office'
        print(message)
    
    def _frequentVisitorRec(self, eNode):
        '''
        This function searches for the employee who has swiped the most number of times and outputs the below string into the outputPS1.txt file.
        Employee id xx swiped the most number of times today with a count of yy
        Use a trigger function to call this recursive function from the root node. For the sake of the assignment, 
        you need to display any one of the employee ids if there are more than one employee who have entered maximum number of times. 
        For example, if employee id 22 and 23 have both visited 3 times, the output should show either 22 or 23.
        '''
        Emp = eNode.SearchEmpMostSwiped(0)
        if Emp is not None and Emp.EmpId is not None:
            message = 'Employee id ' + str(Emp.EmpId) + ' swiped the most number of times today with a count of ' + str(Emp.attCtr)
        else:
            message = 'No Employee swiped today.'
        print(message)
    
    def printRangePresent(self, StartId, EndId):
        '''
        This function prints the employee ids in the range StartId to EndId and how often they have entered the organization in a file name outputPS1.txt.
        The input should be read from the promptsPS1.txt file where the range is mentioned with the tag as shown below.
        range:23:125
        If Input range is given as 23 to 125 the output file should show:
        Range: 23 to 125
        Employee attendance:
        23, 1, in
        41, 3, in
        121, 2, out
        For this purpose, the tree needs to be inorder traversed and the id and frequency of the employees in the range must be printed into the file. 
        If the Id is found in the BT, its frequency cannot be zero as the person had entered the organization at least once.
        '''
        print ("Replace this with logic for range report")
           

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
    
    tracker._getHeadcountRec(eNode)
    # Reading promptsPS1.txt file to see what report is needed and accordingly call the respective function:
    rptFile = open(r'data\promptPS1.txt','r')
    for report in rptFile.readlines():
        rptCat = report.split(':',1)
        tracker._invokeMethod(rptCat[0], eNode, rptCat[1])
    tracker._frequentVisitorRec(eNode)
    print ("Replace this with call to headCount method here")